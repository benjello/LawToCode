# -*- coding: utf-8 -*-


# law-to-code -- Extract formulas from laws
# By: Emmanuel Raviart <emmanuel@raviart.com>
#
# Copyright (C) 2013 OpenFisca Team
# https://github.com/openfisca/law-to-code
#
# This file is part of law-to-code.
#
# law-to-code is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# law-to-code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Setup commands"""


import logging
import os

import setuptools
import webassets.script

from . import environment


class BuildAssets(setuptools.Command):
    """Build assets for production deployment."""
    description = "Precompile WebAssets environment."
    user_options = []

    def finalize_options(self):
        pass

    def initialize_options(self):
        pass

    def run(self):
        assets = environment.configure_assets(
            debug = False,
            static_dir = os.path.join(os.path.dirname(__file__), 'static'),
            )

        log = logging.getLogger('webassets')
        log.addHandler(logging.StreamHandler())
        log.setLevel(logging.DEBUG)

        command_line_environment = webassets.script.CommandLineEnvironment(assets, log)
        command_line_environment.build()
