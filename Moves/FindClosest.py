"""#
# Find the closest object in a forward arc and stare at it.
#"""

#imports
from basic_moves import scanDistance
import time

ranges = scanDistance(160)
closest = ranges[0]

hexy.neck.set(closest[0])
time.sleep(.3)