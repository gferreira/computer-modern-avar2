from importlib import reload
import xTools4.modules.xproject
reload(xTools4.modules.xproject)

import os
from xTools4.modules.xproject import *


class ComputerModernController(xProject):
    
    def __init__(self, folder, familyName, subFamily):
        self.baseFolder = folder
        self.familyName = familyName
        self.subFamily  = subFamily

    @property
    def designspaceFile(self):
        return f"{self.subFamily.replace(' ', '')}.designspace"

    @property
    def sourcesFolder(self):
        return os.path.join(self.baseFolder, self.sourcesFolderName, self.subFamily)

    @property
    def defaultSourcePath(self):
        return os.path.join(self.sourcesFolder, f"{self.subFamily.replace(' ', '')}_{self.defaultName}.ufo")

    @property
    def varFontFile(self):
        fileName = f"{self.familyName}-{self.subFamily}.ttf"
        return fileName.replace(' ', '')

    def buildDesignspace(self, tuning=False, instances=False):
        if self.verbose:
            print(f'building {os.path.split(self.designspacePath)[-1]}...')
        self.designspace = DesignSpaceDocument()
        self.addParametricAxes()
        self.addDefaultSource()
        self.addParametricSources()
        self.addCustomKeysToLib()
        self.save()

    def setSourceNamesFromMeasurements(self, preflight=True, ignoreTags=['wght']):
        setSourceNamesFromMeasurements(
                self.sourcesFolder,
                self.subFamily,
                self.measurementsPath,
                preflight=preflight,
                ignoreTags=ignoreTags,
                infoFamilyName=self.familyName,
        )

if __name__ == '__main__':

    folder = os.path.dirname(os.getcwd())

    subFamily = ['Roman', 'Italic', 'Sans', 'Mono'][0]

    p = ComputerModernController(folder, 'Computer Modern', subFamily)

    # p.printSettings()
    # p.createParametricSources(['XTSP'])

    # p.cleanupSources(parametric=True, tuning=False)
    # p.normalizeSources(parametric=True, tuning=False)

    # p.setSourceNamesFromMeasurements(preflight=True)
    
    # p.parametricAxes = ['XOPQ', 'XTRA', 'YOPQ', 'XTSP']
    # p.buildDesignspace()

