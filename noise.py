import matplotlib.pyplot as plt
import numpy as np
import os
import random
import scipy
import sklearn
from skimage import io
import sys

def is_noisy_image(data, threshold):
    if data <= (threshold * 10**8):
        return True
    else: 
        return False

def output_txt(nonzero_data, threshold, outfile='output.txt'):
    with open(outfile, 'w') as f:
        for file, count in nonzero_data.items():
            f.write(file + ',' + str(is_noisy_image(count, threshold)))

        f.close()
    return

def get_files(inputfile):
    file_list = []
    with open(inputfile) as f:
        lines = f.readlines()
        for line in lines:
            file_list.append(line.strip())
        f.close()
    return file_list

if __name__=="__main__":
    # Get the command-line arguments
    # Format: 0: input file, 1: threshold, 2: 2D or 3D ,3: output filename
    infile = sys.argv[1]
    threshold = float(sys.argv[2])
    dim_mode = sys.argv[3]
    outfile = sys.argv[4]

    files = get_files(infile)

    nonzero_data={}
    for file in files:
        # Load the image and count the number of non-zero values per image
        img=io.imread(file)
        if dim_mode == '3D':
            img = img[:,40:,:320,:]

        count=np.count_nonzero(img)
        nonzero_data[file]=count

    output_txt(nonzero_data, threshold, outfile)
