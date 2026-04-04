# menuTitle: correct contour directions while keeping measurements in sync

from importlib import reload
import xTools4.modules.measurements
reload(xTools4.modules.measurements)

import os, glob, json
from xTools4.modules.measurements import readMeasurements, convertMeasurementIndexesToIDs, convertMeasurementIDsToIndexes

subFamilyName = ['Roman', 'Italic'][0]
folder = os.path.dirname(os.getcwd())
sourcesFolder = os.path.join(folder, 'Sources', subFamilyName)
defaultPath = os.path.join(sourcesFolder, f'{subFamilyName}_wght400.ufo')
measurementsPath = os.path.join(sourcesFolder, 'measurements.json')

assert os.path.exists(defaultPath)
assert os.path.exists(measurementsPath)
    
defaultFont = OpenFont(defaultPath, showInterface=False)

measurements = readMeasurements(measurementsPath)
measurementsIDs = convertMeasurementIndexesToIDs(defaultFont, measurements)

allSources = glob.glob(f'{sourcesFolder}/*.ufo')

print(allSources)

for srcPath in allSources:
    src = OpenFont(defaultPath, showInterface=False)
    for g in src:
        g.correctDirection(trueType=True)
    src.save()

defaultFont = OpenFont(defaultPath, showInterface=False)
measurementsNew = convertMeasurementIDsToIndexes(defaultFont, measurementsIDs)

measurementsPathOld = measurementsPath.replace('.json', '_old.json')

os.rename(measurementsPath, measurementsPathOld)

with open(measurementsPath, 'w', encoding='utf-8') as f:
    json.dump(measurementsIDs, f, indent=2)
