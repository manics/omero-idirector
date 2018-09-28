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

import sys
import os

from django.conf import settings
from omeroweb.settings import process_custom_settings, report_settings


# load settings
SHRTN_SETTINGS_MAPPING = {
    'omero.web.shrtn.namespace':
        ['SHRTN_NAMESPACE', 'openmicroscopy.org/omero/web/shrtn', str, None],
    'omero.web.shrtn.prefix':
        ['SHRTN_PREFIX', 'shrtn', str, None],
}


process_custom_settings(sys.modules[__name__], 'SHRTN_SETTINGS_MAPPING')
report_settings(sys.modules[__name__])
