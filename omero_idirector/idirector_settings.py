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
IDIRECTOR_SETTINGS_MAPPING = {
    'omero.web.idirector.prefix':
        ['IDIRECTOR_PREFIX', 'idirector', str,
         'Application prefix for idirector URLs'],
    'omero.web.idirector.types':
        ['IDIRECTOR_TYPES', [], json.loads,
         ('List of OMERO types (e.g. ["Screen", "Project"]) to be searched '
          'for automatic shortened lookups. Order is important, the first '
          'type with a match will be returned. Required.')],
    'omero.web.idirector.validre':
        ['IDIRECTOR_VALIDRE', '.+', str,
         ('Regular expression that shortened link must match to be considered '
          'for automatic lookups. Example: `\d{4}` means links must be '
          'exactly 4 digits')],
    'omero.web.idirector.match':
        ['IDIRECTOR_MATCH', '{u}', str,
         ('HQL "like" string to match names against. Must contain `{u}` '
          'which will be replaced by the short-link passed by the client. '
          'For example, `idr{u}-%` will search for names beginning '
          '`idrNNNN-` where `NNNN` is the short link. Default is to '
          'exactly match the OMERO name against the short link')],
}


process_custom_settings(sys.modules[__name__], 'IDIRECTOR_SETTINGS_MAPPING')
report_settings(sys.modules[__name__])
