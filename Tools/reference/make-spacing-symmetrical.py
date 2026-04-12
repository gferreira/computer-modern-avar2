# menuTitle: make Italic spacing symmetrical based on /H margins 

import os, glob

baseFolder = os.path.dirname(os.path.dirname(os.getcwd()))
sourcesFolder = os.path.join(baseFolder, 'Sources', 'Italic') # 'reference')

assert os.path.exists(sourcesFolder)

angled = True

ufoPaths = glob.glob(f'{sourcesFolder}/*.ufo')

for ufoPath in ufoPaths:
    f = OpenFont(ufoPath, showInterface=False)
    glyph = f['H']
    if angled:
        bothMargins = glyph.angledLeftMargin + glyph.angledRightMargin
        shiftX = bothMargins / 2 - glyph.angledLeftMargin
    else:
        bothMargins = glyph.leftMargin + glyph.rightMargin
        shiftX = bothMargins / 2 - glyph.leftMargin

    print(f'shifting all glyphs in {os.path.splitext(os.path.split(ufoPath)[-1])[0]} by {shiftX}...')

    for g in f:
        g.moveBy((shiftX, 0))
    
    f.save()
