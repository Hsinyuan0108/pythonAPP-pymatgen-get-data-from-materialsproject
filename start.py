from APP import *
from funcs_about_mp import * 
import sys
import getopt

def main( argv ):

    work_mod = ""
    file_name = ""
    try:
        opts, args = getopt.getopt( argv,'hm:f:', ["help"] )
    except getopt.GetoptError:
        print('format : start.py -m <work_mod>(APP or CMD) -f <file_name>(should be .txt)(not needed when work mod is app' )

        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('start.py -m <work_mod>(APP or CMD) -f <file_name>(should be .txt)(not needed when work mod is app')
            sys.exit()
        elif opt in ("-m"):
            work_mod = arg
        elif opt in ("-f"):
            file_name = arg

    if work_mod == 'APP':
        start_app()
        
    elif work_mod == 'CMD': 
        CMD_get_data( file_name )




if __name__ == "__main__":

    main(sys.argv[1:])



