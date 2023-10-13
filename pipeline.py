import numpy
import sys


if __name__=="__main__":

    with open(sys.argv[1],'w') as f:
        f.write(numpy.__version__)
