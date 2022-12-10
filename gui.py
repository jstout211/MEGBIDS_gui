#!/usr/bin/env python
import argparse
from gooey import Gooey

@Gooey
def main():
    parser = argparse.ArgumentParser(description='Do stuff with numbers.')
    parser.add_argument('-o','--output', help="Enter output BIDS directory", type="str", required=False, nargs='+')
    parser.add_argument('-m','--MEG', help='Enter path of MEG folder', type="str", required=False, nargs='+')
    parser.add_argument('-n','--NIFTI', help='Enter path of NIFTI folder', type="str", required=False, nargs='+')
    parser.add_argument('-t','--transformatrix', help='Enter path of transform matrix', type="str", required=False, nargs='+')

    args = vars(parser.parse_args())

    if args['output']:
        bids_dir = args["output"]
        print("File output to selected BIDS directory")

    if args['MEG']:
        meg_file = args["MEG"]

    if args['NIFTI']:
        nifti_file = args["NIFTI"]

    if args['transformmatrix']:
        tm_file = args["transformmatrix"]
        
main()