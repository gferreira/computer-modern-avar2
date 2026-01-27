#!/bin/sh

echo "Building variable fonts..."

echo "  Building Computer Modern Roman..."
fontmake -m Sources/Roman/Roman.designspace -o variable --output-path Fonts/ComputerModern-Roman.ttf  --feature-writer None --no-generate-GDEF --keep-direction --verbose WARNING

echo "  Building Computer Modern Italic..."
fontmake -m Sources/Italic/Italic.designspace -o variable --output-path Fonts/ComputerModern-Italic.ttf  --feature-writer None --no-generate-GDEF --keep-direction --verbose WARNING

echo "  Building Computer Modern Sans..."
fontmake -m Sources/Sans/Sans.designspace -o variable --output-path Fonts/ComputerModern-Sans.ttf  --feature-writer None --no-generate-GDEF --keep-direction --verbose WARNING

echo "done!"
