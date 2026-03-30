import os
from xTools4.modules.normalization import cleanupSources, normalizeSources

baseFolder = os.path.dirname(os.path.dirname(os.getcwd()))
subFamilyName = ['Roman', 'Italic', 'Sans'][1]
sourcesFolder = os.path.join(baseFolder, 'Sources', subFamilyName)
referenceFolder = os.path.join(sourcesFolder, 'reference')

assert os.path.exists(referenceFolder)

preflight = False

ignoreFontLibs = [
    'com.typemytype.robofont.italicSlantOffset',
    'com.typemytype.robofont.segmentType',
]

ignoreLayers = [
    'foreground',
    'background',
]

cleanupSources(referenceFolder,
        clearFontLibs=True,
        clearGlyphLibs=True,
        clearFontGuides=True,
        clearGlyphGuides=True,
        clearMarks=True,
        clearLayers=True,
        preflight=preflight,
        ignoreFontLibs=ignoreFontLibs,
        ignoreLayers=ignoreLayers,
        # verbose=self.verbose
    )

normalizeSources(referenceFolder)
