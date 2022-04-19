# https://en.wikipedia.org/wiki/Command-line_argument_parsing

import sys

def ArguementParsing() :
    if len(sys.argv) > 1 :                          # not > 0; sys.argv[0] is the script file name
        for arg in sys.argv :
            print(arg)
    else :
        print("No arguments has been received.")

# test
def test() :
    for arg in list(sys.argv) :
        print(arg)

if __name__ == "__main__" :
    ArguementParsing()
    # test()                                        # 0(path) 1 2 3