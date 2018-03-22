#-----------------------------------------------------------------------------
# Copyright (c) 2013-2018, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


# This runtime hook installs the default reactor for twisted based app.
# Twisted library inserts detected reactor implementation directly
# to sys.modules['twisted.internet.reactor'].
#
# Applications importing module twisted.internet.reactor might otherwise fail
# with error like:
#
#     AttributeError: 'module' object has no attribute 'listenTCP'
#
# Tested with   Twisted 12.3.0

import sys

# This creates module: sys.modules['twisted.internet.reactor']
if sys.platform in ['win32']:
    from twisted.internet.iocpreactor import reactor as _iocpreactor
    _iocpreactor.install()
else:
    from twisted.internet import default
    default.install()
