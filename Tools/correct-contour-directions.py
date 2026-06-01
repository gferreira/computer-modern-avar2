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

### 1. convert measurements from indexes to IDs

defaultFont = OpenFont(defaultPath, showInterface=False)
measurements = readMeasurements(measurementsPath)
measurementsIDs = convertMeasurementIndexesToIDs(defaultFont, measurements)
defaultFont.save()

### 2. correct contour direction in all sources

allSources = glob.glob(f'{sourcesFolder}/*.ufo')

for srcPath in allSources:
    src = OpenFont(srcPath, showInterface=False)
    for g in src:
        g.correctDirection(trueType=True)
    src.save()

### 3. convert measurements from IDs to indexes

defaultFont = OpenFont(defaultPath, showInterface=False)
measurementsNew = convertMeasurementIDsToIndexes(defaultFont, measurementsIDs)

### 4. save new measurements / keep old ones in renamed file

measurementsPathOld = measurementsPath.replace('.json', '_old.json')
os.rename(measurementsPath, measurementsPathOld)
with open(measurementsPath, 'w', encoding='utf-8') as f:
    json.dump(measurementsIDs, f, indent=2)
