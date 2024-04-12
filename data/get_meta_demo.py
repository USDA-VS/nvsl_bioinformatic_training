#!/usr/bin/env python

__version__ = "0.0.1"

import os
import sys
import re
import shutil
import glob
import argparse
import textwrap
import pandas as pd


class Update_Names():
    ''' 
    '''

    def __init__(self, excel=None):
        '''
        Start at class call
        '''
        df = pd.read_excel(excel)
        d = df.to_dict('list')
        keys = d['sample name']
        values = d['metadata']
        dd = dict(zip(keys, values))
        self.dd = dd

    def run(self, in_file=None):
        '''
        description
        '''
        sample_name = re.sub('[_.].*', '', in_file)
        sample_meta = self.dd[sample_name]
        return sample_meta


if __name__ == "__main__": # execute if directly access by the interpreter
    parser = argparse.ArgumentParser(prog='PROG', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\

    ---------------------------------------------------------
    Usage:
    Files: nvsl_bioinformatic_training/data/sample_naming_and_metadata
    ./get_meta_demo.py -f a.txt -e metadata.xlsx

    '''), epilog='''---------------------------------------------------------''')

    parser.add_argument('-f', '--in_file', action='store', dest='in_file', required=True, help='Required: In file')
    parser.add_argument('-e', '--excel', action='store', dest='excel', required=True, help='Required: 2 column Excel file')
    parser.add_argument('-v', '--version', action='version', version=f'{os.path.basename(__file__)}: version {__version__}')
    args = parser.parse_args()
    
    print(f'\n{os.path.basename(__file__)} SET ARGUMENTS:')
    print(args)
    print("\n")

    update_names = Update_Names(excel=args.excel)
    sample_meta = update_names.run(in_file=args.in_file)
    print(f'{args.in_file} --> {sample_meta}\n')

# Created 2023 by Tod Stuber
