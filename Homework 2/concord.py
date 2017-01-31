import sys
from concordance import concordance

sys.argv.sort()

for arg in sys.argv:
    print(arg)
    print(concordance("file.txt"))