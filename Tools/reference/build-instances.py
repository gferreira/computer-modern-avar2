import os
from ufoProcessor.ufoOperator import UFOOperator

designspacePath = '/Users/gferreira/fontbureau/computer-modern/Sources/Roman/reference/Roman.designspace'

operator = UFOOperator(designspacePath)
operator.generateUFOs()
