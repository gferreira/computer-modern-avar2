from importlib import reload
import xTools4.modules.xproject
reload(xTools4.modules.xproject)

import os
from xTools4.modules.xproject import xProject, DesignSpaceDocument


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

        self.designspace = DesignSpaceDocument()
        # self.addParametricAxes()
        self.addDefaultSource()
        # self.addParametricSources()
        self.addCustomKeysToLib()
        self.save()


if __name__ == '__main__':

    folder = os.path.dirname(os.getcwd())

    subFamily = ['Roman', 'Italic', 'Sans', 'Mono'][0]

    p = ComputerModernController(folder, 'Computer Modern', subFamily)
    # p.printSettings()

    parametricAxes = [
        'XOPQ',
        'XTRA',
        # 'YOPQ',
        # etc.
    ]
    p.createParametricSources(parametricAxes)

    p.buildDesignspace()

    # p.setSourceNamesFromMeasurements()
