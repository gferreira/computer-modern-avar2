# menuTitle: extract parametric blends from ComputerModernPS

from importlib import reload
import xTools4.modules.measurements
reload(xTools4.modules.measurements)

import os, glob, json
from xTools4.modules.measurements import extractMeasurements

subFamilyName    = ['Roman', 'Italic', 'Sans'][0]
baseFolder       = os.path.dirname(os.path.dirname(os.getcwd()))
sourcesFolder    = os.path.join(baseFolder, 'Sources', subFamilyName, 'reference')
measurementsPath = os.path.join(sourcesFolder, 'measurements.json')
blendsPath       = os.path.join(sourcesFolder, 'blends.json')
parametricAxes   = ['XOPQ', 'XTRA', 'YOPQ', 'XTSP', 'XSHA', 'YSHA', 'XSVA', 'YSVA'] # XOUC XOLC XOFI YOUC YOLC YOFI XTUC XTLC XTFI YTUC YTLC YTAS YTDE YTFI XUCS XLCS XFIR XSHU YSHU XSHL YSHL XSVU YSVU'.split()

assert os.path.exists(sourcesFolder)
assert os.path.exists(measurementsPath)

# define blended axes

axes = {
    "opsz" : {
      "name"    : "Optical size",
      "default" : 10,
      "minimum" : 5,
      "maximum" : 17,
    },
}

# extract measurements from ComputerModernPS instances

ufos = [f for f in glob.glob(f'{sourcesFolder}/*.ufo')]

sources = extractMeasurements(ufos, measurementsPath, parametricAxes)

# save measurements to JSON blends file

blendsDict = {
    'axes'    : axes,
    'sources' : sources,
}

print('saving blended axes and measurements to blends.json...\n')

with open(blendsPath, 'w', encoding='utf-8') as f:
    json.dump(blendsDict, f, indent=2)

print('...done!\n')
