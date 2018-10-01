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
import shrtn_settings
from copy import deepcopy

logger = logging.getLogger(__name__)


def match_object_name(u, conn):
    if (shrtn_settings.SHRTN_AUTO_TYPES and
            shrtn_settings.SHRTN_MATCHRE and
            shrtn_settings.SHRTN_VALIDRE and
            re.match(shrtn_settings.SHRTN_VALIDRE, u)):
        rematch = shrtn_settings.SHRTN_REMATCH.format(u=u)
        for t in shrtn_settings.SHRTN_AUTO_TYPES:
            for obj in conn.getObjects(t):
                if re.match(rematch, obj.name):
                    objtype = t.lower()
                    if objtype == 'acquisition':
                        objtype = 'run'
                    dest = '%s?show=%s-%d' % (
                        reverse('webindex'), objtype, obj.id)
                    return dest


@login_required()
def unshrtn(request, u, conn=None, **kwargs):
    """
    Look up a shortened link by:
    - Looking for a regular expression match for defined object types
    - searching MapAnnotations in a namespace, if a key matching the request
      is found redirects to the URL in the value

    @param request: The Django L{django.core.handlers.wsgi.WSGIRequest}
                    - u: The short path
    @return: A redirect to the unshortened URL
    """
    if not u:
        raise Http404("No short URL provided")

    dest = match_object_name(u, conn)
    if dest:
        logger.debug('Redirecting omero-shrtn %s to %s', u, dest)
        return redirect(dest)

    qs = conn.getQueryService()
    params = omero.sys.ParametersI()
    params.page(0, 1)
    params.addString('ns', rstring(shrtn_settings.SHRTN_NAMESPACE))
    params.addString('u', rstring(u))
    service_opts = deepcopy(conn.SERVICE_OPTS)
    service_opts.setOmeroGroup(-1)
    q = ("SELECT mv.value FROM MapAnnotation ma JOIN ma.mapValue as mv "
         "WHERE ma.ns = :ns AND mv.name = :u "
         "ORDER BY id DESC ")

    r = unwrap(qs.projection(q, params, service_opts))
    logger.debug('Query: "%s" ns:%s u:%s result:%s',
                 q, shrtn_settings.SHRTN_NAMESPACE, u, r)
    if not r:
        raise Http404("Short URL not found")

    dest = r[0][0]
    return redirect(dest)
