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
        if self.verbose:
            print('\tbuilding blends file...')
        if os.path.exists(self.blendsPath):
            os.remove(self.blendsPath)
        shutil.copy(self.referenceBlendsPath, self.blendsPath)

    def patchBlendsFile(self):

        # import blends data
        with open(self.blendsPath, 'r', encoding='utf-8') as f:
            blendsDict = json.load(f)

        # import & apply patch data
        patchPath = self.blendsPath.replace('.json', '_patch.json')
        if not os.path.exists(patchPath):
            return

        with open(patchPath, 'r', encoding='utf-8') as f:
            patchDict = json.load(f)

        for key1, value1 in patchDict.items():
            if key1 not in blendsDict:
                print(f'{key1} not in blends dict')
                continue
            for key2, value2 in value1.items():
                if key2 not in blendsDict[key1]:
                    blendsDict[key1][key2] = {}
                for k, v in value2.items():
                    blendsDict[key1][key2][k] = v

        # save patched blends data
        with open(self.blendsPath, 'w', encoding='utf-8') as f:
            json.dump(blendsDict, f, indent=2)

    def buildDesignspace(self, patchBlends=True, tuning=False, instances=False):
        if self.verbose:
            print(f'building {os.path.split(self.designspacePath)[-1]}...')

        self.buildBlendsFile()
        if patchBlends:
            self.patchBlendsFile()

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

    subFamily = ['Roman', 'Italic', 'Sans', 'Mono'][1]

    parametricAxes = {
        'Roman'  : ['XOPQ', 'XTRA', 'YOPQ', 'XTSP', 'XSHA', 'YSHA', 'XSVA', 'YSVA', 'YTUC', 'YTLC', 'BRKT'],
        'Italic' : ['XOPQ', 'XTRA', 'YOPQ', 'XTSP', 'XSHA', 'YSHA', 'XSVA', 'YSVA', 'YTUC', 'YTLC'],
    }

    p = ComputerModernController(folder, 'Computer Modern', subFamily)

    # p.printSettings()
    # p.createParametricSources(['BRKT'], minSource=True, maxSource=False)

    p.cleanupSources(parametric=True, tuning=False)
    p.normalizeSources(parametric=True, tuning=False)

    # p.setSourceNamesFromMeasurements(preflight=False)
    
    # p.parametricAxes = parametricAxes[subFamily]
    # p.parametricAxesHidden = False
    # p.buildDesignspace(patchBlends=False)
