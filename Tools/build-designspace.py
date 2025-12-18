import os, glob
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor

folder = '/Users/gferreira/hipertipo/fonts/fontbureau/computer-modern/Sans'

familyName = 'Computer Modern Sans'

ufoPaths = glob.glob(f'{folder}/*.ufo')

designspacePath = os.path.join(folder, f"{familyName.replace(' ', '-')}.designspace")

defaultValue = 8

opszSources = {}
for ufoPath in ufoPaths:
    styleName = os.path.splitext(os.path.split(ufoPath)[-1])[0].split('_')[-1]
    tag, value = styleName[:4], styleName[4:]
    opszSources[value] = ufoPath

opszValues = [int(k) for k in opszSources.keys()]

D = DesignSpaceDocument()

a = AxisDescriptor()
a.name    = 'opsz'
a.tag     = 'opsz'
a.minimum = min(opszValues)
a.maximum = max(opszValues)
a.default = 10
D.addAxis(a)

for opszValue, ufoPath in opszSources.items():
    print(opszValue, ufoPath)

    src = SourceDescriptor()
    src.path       = ufoPath
    src.familyName = familyName
    src.location   = { 'opsz' : int(opszValue) }
    D.addSource(src)

print(designspacePath)
D.write(designspacePath)
