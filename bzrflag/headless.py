# Bzrflag
# Copyright 2008-2011 Brigham Young University
#
# This file is part of Bzrflag.
#
# Bzrflag is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Bzrflag is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# Bzrflag.  If not, see <http://www.gnu.org/licenses/>.
#
# Inquiries regarding any further use of Bzrflag, please contact the Copyright
# Licensing Office, Brigham Young University, 3760 HBLL, Provo, UT 84602,
# (801) 422-9339 or 422-3821, e-mail copyright@byu.edu.

"""headless.py

Defines a Display class and an Input class
for a headless station.

"""
__author__ = "BYU AML Lab <kseppi@byu.edu>"
__copyright__ = "Copyright 2008-2011 Brigham Young University"
__license__ = "GNU GPL"

import asyncore
import logging

import server
import constants
import config
import graphics 
from constants import LOOP_TIMEOUT  

logger = logging.getLogger('headless.py')


class Display(graphics.Display):

    def update(self):
        """Pass"""
        pass
        
    def setup(self):
        """Pass"""
        pass


class Input:
    """The server input class."""
    
    def __init__(self, game):
        self.game = game
        self.servers = {}
        for color,team in self.game.map.teams.items():
            self.servers[color] = server.Server(
                    ('0.0.0.0', config.config[color+'_port']),team)
            print 'port for %s: %s' % (color, self.servers[color].get_port())
        print

    def update(self):
        asyncore.loop(LOOP_TIMEOUT, count = 1)
