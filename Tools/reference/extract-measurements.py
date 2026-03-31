# menuTitle: extract parametric blends from ComputerModernPS

from importlib import reload
import xTools4.modules.measurements
reload(xTools4.modules.measurements)

import os, glob, json
from xTools4.modules.measurements import extractMeasurements

subFamilyName    = ['Roman', 'Italic', 'Sans'][1]
baseFolder       = os.path.dirname(os.path.dirname(os.getcwd()))
sourcesFolder    = os.path.join(baseFolder, 'Sources', subFamilyName, 'reference')
measurementsPath = os.path.join(sourcesFolder, 'measurements.json')
blendsPath       = os.path.join(sourcesFolder, 'blends.json')

assert os.path.exists(sourcesFolder)
assert os.path.exists(measurementsPath)

parametricAxes = {
    'Roman'  : ['XOPQ', 'XTRA', 'YOPQ', 'XTSP', 'XSHA', 'YSHA', 'XSVA', 'YSVA', 'YTUC', 'YTLC', 'BRKT'],
    'Italic' : ['XOPQ', 'XTRA', 'YOPQ', 'XTSP', 'XSHA', 'YSHA', 'XSVA', 'YSVA', 'YTUC', 'YTLC'],
}

# define blended axes

axes = {
    "opsz" : {
      "name"    : "Optical size",
      "default" : 10,
      "minimum" : 5,
      "maximum" : 17 if subFamilyName == 'Roman' else 12,
    },
}

if subFamilyName == 'Roman':
    axes["wght"] = {
      "name"    : "Weight",
      "default" : 400,
      "minimum" : 400,
      "maximum" : 700,
    }    

# extract measurements from ComputerModernPS instances

ufos = [f for f in glob.glob(f'{sourcesFolder}/*.ufo')]

sources = extractMeasurements(ufos, measurementsPath, parametricAxes[subFamilyName])

# save measurements to JSON blends file

blendsDict = {
    'axes'    : axes,
    'sources' : sources,
}

print('saving blended axes and measurements to blends.json...\n')

with open(blendsPath, 'w', encoding='utf-8') as f:
    json.dump(blendsDict, f, indent=2)

print('...done!\n')
