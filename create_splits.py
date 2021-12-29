import argparse
import glob
import os
import random
import shutil

import numpy as np

from utils import get_module_logger


def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
          
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    
    source = data_dir + str("/training_and_validation/")
    dest_train = data_dir + str("/train/")
    dest_val = data_dir + str("/val/")
        
    get_files = os.listdir(source)                     
    j=0       
    for i in get_files:
        if j<10:
            shutil.move(source + i, dest_val) 
        else:    
            shutil.move(source + i, dest_train) 
        j = j+1

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data-dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)
