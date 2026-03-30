#!/bin/sh

echo "Building variable fonts..."

echo "  Building Computer Modern Roman (reference font)..."
fontmake -m Sources/Roman/reference/Roman.designspace -o variable --output-path Fonts/ComputerModern-Roman.ttf  --feature-writer None --no-generate-GDEF --keep-direction --verbose WARNING

# echo "  Building Computer Modern Italic (reference font)..."
# fontmake -m Sources/Italic/Italic.designspace -o variable --output-path Fonts/ComputerModern-Italic.ttf  --feature-writer None --no-generate-GDEF --keep-direction --verbose WARNING

# echo "  Building Computer Modern Sans (reference font)..."
# fontmake -m Sources/Sans/Sans.designspace -o variable --output-path Fonts/ComputerModern-Sans.ttf  --feature-writer None --no-generate-GDEF --keep-direction --verbose WARNING

echo "  Building Computer Modern Roman (avar2)..."
fontmake -m Sources/Roman/Roman.designspace -o variable --output-path Fonts/ComputerModern-Roman_avar2.ttf  --feature-writer None --no-generate-GDEF --keep-direction --verbose WARNING


echo "done!"
