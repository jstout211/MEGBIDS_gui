#!/usr/bin/env python
import argparse
from gooey import Gooey

@Gooey
def main():
    parser = argparse.ArgumentParser(description='Do stuff with numbers.')
    parser.add_argument('-o','--output', help="Enter output BIDS directory", type="str", required=False, nargs='+')
    parser.add_argument('-m','--meg', help='Enter path of MEG folder', type="str", required=False, nargs='+')
    parser.add_argument('-n','--nifti', help='Enter path of NIFTI folder', type="str", required=False, nargs='+')
    parser.add_argument('-t','--transformatrix', help='Enter path of transform matrix', type="str", required=False, nargs='+')

    args = vars(parser.parse_args())

    if args['output']:
        print("File output to selected BIDS directory")

        
main()