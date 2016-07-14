import os

dirs = os.listdir('.')

for x in dirs:
    os.rename(x, x.lower())
