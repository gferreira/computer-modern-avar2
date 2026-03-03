from importlib import reload
import xTools4.modules.xproject
reload(xTools4.modules.xproject)

import os
from xTools4.modules.xproject import xProject

folder = os.path.dirname(os.getcwd())

p = xProject(folder, 'Computer Modern', subFamilyName='Roman')
p.defaultName = 'wght400'
p.parametricAxes = 'XOPQ XTRA YOPQ XTSP'.split()

# print(p.sourcesFolder, os.path.exists(p.sourcesFolder))
# print(p.sources)
# print(p.designspaceFileName)
# print(p.designspacePath)

p.build()
