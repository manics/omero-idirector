#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import redirect

from omeroweb.webclient.decorators import login_required

import logging
import omero
from omero.rtypes import rstring, unwrap, wrap
#from django.conf import settings
import shrtn_settings
from copy import deepcopy

logger = logging.getLogger(__name__)


@login_required()
def unshrtn(request, u, conn=None, **kwargs):
    """
    Look up a shortened link by searching MapAnnotations in a namespace
    If a key matching the request is found redirects to the URL in the value

    @param request: The Django L{django.core.handlers.wsgi.WSGIRequest}
                    - u: The short path
    @return: A redirect to the unshortened URL
    """
    if not u:
        raise Http404("No short URL provided")

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
