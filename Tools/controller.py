from importlib import reload
import xTools4.modules.xproject
reload(xTools4.modules.xproject)

import os, shutil
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

    @property
    def referenceBlendsPath(self):
        return os.path.join(self.sourcesFolder, 'reference', self.blendsFile)

    def buildBlendsFile(self):
        if os.path.exists(self.blendsPath):
            os.remove(self.blendsPath)
        shutil.copy(self.referenceBlendsPath, self.blendsPath)

    def buildDesignspace(self, tuning=False, instances=False):
        if self.verbose:
            print(f'building {os.path.split(self.designspacePath)[-1]}...')

        self.buildBlendsFile()

        self.designspace = DesignSpaceDocument()
        self.addBlendedAxes()
        self.addParametricAxes()
        self.addBlendMappings()
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
                infoFamilyName=f'{self.familyName} {self.subFamily}',
        )


if __name__ == '__main__':

    folder = os.path.dirname(os.getcwd())

    subFamily = ['Roman', 'Italic', 'Sans', 'Mono'][0]

    parametricAxes = {
        'Roman'  : ['XOPQ', 'XTRA', 'YOPQ', 'XTSP', 'XSHA', 'YSHA'],
        'Italic' : ['XOPQ', 'YOPQ'],
    }

    p = ComputerModernController(folder, 'Computer Modern', subFamily)

    # p.printSettings()
    # p.createParametricSources(['YTLC'])

    p.cleanupSources(parametric=True, tuning=False)
    p.normalizeSources(parametric=True, tuning=False)

    # p.setSourceNamesFromMeasurements(preflight=True)
    
    # p.parametricAxes = parametricAxes[subFamily]
    # p.parametricAxesHidden = False
    # p.buildDesignspace()
