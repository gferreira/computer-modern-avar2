import os, glob
from xTools4.modules.unicode import autoUnicode, unicodesExtra

baseFolder = os.path.dirname(os.getcwd())
subFamilyName = ['Roman', 'Italic', 'Sans'][2]
sourcesFolder = os.path.join(baseFolder, 'Sources', subFamilyName)
referenceFolder = os.path.join(sourcesFolder, 'reference')

ufoPaths = glob.glob(f'{referenceFolder}/*.ufo')

for ufoPath in ufoPaths:
    f = OpenFont(ufoPath, showInterface=False)
    for g in f:
        autoUnicode(g)
    f.save()
