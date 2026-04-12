import os
from fontTools.designspaceLib import DesignSpaceDocument

# code copied from the Batch extension:
# http://github.com/typemytype/batchRoboFontExtension/blob/84d0348b26bd9ec5aeaf5be2e7a0c75c1882006d/source/lib/batchGenerators/variableFontsGenerator/__init__.py#L203

class CompatibleContourPointPen(object):

    def __init__(self, types):
        self.types = list(types)

    def addPoint(self, pt, segmentType=None, *args, **kwargs):
        self.contour.append((pt, segmentType, args, kwargs))

    def beginPath(self):
        self.contour = list()

    def endPath(self):
        # lets start
        newContour = []
        for i, ((x, y), segmentType, args, kwargs) in enumerate(self.contour):
            if self.types:
                # if there is segmentType
                if segmentType is not None:
                    # check with the given list of segmentTypes
                    if segmentType != self.types[0]:
                        # its different
                        # get the previous point
                        (px, py), _, _, _ = self.contour[i - 1]
                        # calculate offcurve points
                        # on 1/3 of the line segment length
                        dx = x - px
                        dy = y - py

                        nx1 = px + dx * 0.333
                        ny1 = py + dy * 0.333

                        nx2 = px + dx * 0.666
                        ny2 = py + dy * 0.666
                        # add it to the new contour
                        newContour.append(((nx1, ny1), None, [], {}))
                        newContour.append(((nx2, ny2), None, [], {}))
                        segmentType = self.types[0]
                    # remove the first given segmentType
                    self.types.pop(0)
            # add the point
            newContour.append(((x, y), segmentType, args, kwargs))
        # set the contour
        self.contour = newContour

    def drawPoints(self, pointPen, roundCoordinates=1):
        pointPen.beginPath()
        for (x, y), segmentType, args, kwargs in self.contour:
            kwargs["identifier"] = None
            pointPen.addPoint((x, y), segmentType, *args, **kwargs)
        pointPen.endPath()

def makeGlyphOutlinesCompatible(glyphs):
    if len(glyphs) <= 1:
        return
    # map all segment type for the given glyphs by contour index
    glyphSegmentTypeMap = {}
    for glyph in glyphs:
        for i, contour in enumerate(glyph):
            types = [point.segmentType for point in contour if point.segmentType]
            if i not in glyphSegmentTypeMap:
                glyphSegmentTypeMap[i] = list()
            glyphSegmentTypeMap[i].append((types, glyph))
    for contourIndex, contourTypes in glyphSegmentTypeMap.items():
        # collect all segment types for a single glyph
        pointTypes = None
        for types, glyph in contourTypes:
            if pointTypes is None:
                pointTypes = list(types)
            else:
                for i, t in enumerate(types):
                    if t in ("curve", "qcurve"):
                        pointTypes[i] = t

        font = glyph.font
        # check if they are different
        for types, glyph in contourTypes:
            if types == pointTypes:
                continue
            # add missing off curves
            contour = glyph[contourIndex]
            pen = CompatibleContourPointPen(pointTypes)
            contour.drawPoints(pen)
            contour.clear()
            pen.drawPoints(contour)


from string import ascii_lowercase, ascii_uppercase

folder = os.path.dirname(os.path.dirname(os.getcwd()))
subFamilyName = ['Roman', 'Italic', 'Sans'][2]
sourcesFolder = os.path.join(folder, 'Sources', subFamilyName)
designspacePath = os.path.join(sourcesFolder, 'reference', f'{subFamilyName}.designspace')

glyphNames = ['acute']

assert os.path.exists(designspacePath)

D = DesignSpaceDocument()
D.read(designspacePath)

sources = [OpenFont(src.path, showInterface=False) for src in D.sources]

for glyphName in glyphNames:
    glyphs = [src[glyphName].naked() for src in sources if glyphName in src]
    makeGlyphOutlinesCompatible(glyphs)

for src in sources:
    src.save()
