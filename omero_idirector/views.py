#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404
# Importing django.shortcuts.reverse breaks the app whereas
# django.core.urlresolvers seems to work
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from omeroweb.webclient.decorators import login_required

import logging
import omero
from omero.rtypes import rstring, unwrap
import re
import idirector_settings
from copy import deepcopy

logger = logging.getLogger(__name__)


@login_required()
def idirector(request, u, conn=None, **kwargs):
    """
    Attempt to match a shortlink against an OMERO object name.
    If there are multiple matches for the same object type return the one
    with the lowest ID.

    @param request: The Django L{django.core.handlers.wsgi.WSGIRequest}
                    - u: The short path
    @return: A redirect to the unshortened URL
    """
    if not re.match(idirector_settings.IDIRECTOR_VALIDRE, u):
        raise Http404('Invalid short URL')

    qs = conn.getQueryService()
    for objtype in idirector_settings.IDIRECTOR_TYPES:
        match = idirector_settings.IDIRECTOR_MATCH.format(u=u)
        params = omero.sys.ParametersI()
        params.page(0, 1)
        params.addString('match', rstring(match))
        service_opts = deepcopy(conn.SERVICE_OPTS)
        service_opts.setOmeroGroup(-1)
        q = 'SELECT id FROM %s WHERE name LIKE :match ORDER BY id' % objtype
        r = unwrap(qs.projection(q, params, service_opts))
        logger.debug('query:"%s" match:%s results:%s', q, match, r)

        if r:
            objid = r[0][0]
            dest = '%s?show=%s-%d' % (
                reverse('webindex'), objtype.lower(), objid)
            logger.debug('Redirecting %s to %s', u, dest)
            return redirect(dest)

    raise Http404('No match found for short URL')
