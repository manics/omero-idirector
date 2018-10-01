#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import sys

from omeroweb.settings import process_custom_settings, report_settings


# load settings
SHRTN_SETTINGS_MAPPING = {
    'omero.web.shrtn.namespace':
        ['SHRTN_NAMESPACE', 'openmicroscopy.org/omero/web/shrtn', str,
         'Shrtn map-annotation namespace'],
    'omero.web.shrtn.prefix':
        ['SHRTN_PREFIX', 'shrtn', str,
         'Application prefix for shrtn URLs'],
    'omero.web.shrtn.auto.types':
        ['SHRTN_AUTO_TYPES', [], json.loads,
         ('List of OMERO types (e.g. ["Screen", "Project"]) to be searched '
          'for automatic shortened lookups')],
    'omero.web.shrtn.auto.validre':
        ['SHRTN_VALIDRE', '', str,
         ('Regular expression that shortened link must match to be considered '
          'for automatic lookups')],
    'omero.web.shrtn.auto.matchre':
        ['SHRTN_MATCHRE', '', str,
         ('Regular expression containing the shortened link that OMERO '
          'object names will be matched against. Must contain `{u}` which '
          'will be replaced by the short-link passed by the client')],
}


process_custom_settings(sys.modules[__name__], 'SHRTN_SETTINGS_MAPPING')
report_settings(sys.modules[__name__])
