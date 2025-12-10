import os, glob

folder = '/Users/gferreira/hipertipo/fonts/fontbureau/computer-modern/Roman'

pfbPaths = glob.glob(f'{folder}/*.pfb')
print(pfbPaths)

for pfbPath in pfbPaths:
    f = OpenFont(pfbPath, showInterface=False)
    ufoPath = pfbPath.replace('.pfb', '.ufo')
    f.save(ufoPath)
    f.close()
