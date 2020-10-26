# this file is supposed to create a d x t matrix

import os
import pandas as pd
import pickle
import sys

'''
to call: python src\parse_data.py data\processed_acl
'''

def main():
    print("hello world")

    input_dir = sys.argv[1]

    # read in data for parsing

    file_paths = []  # collect file paths for reviews
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file != "unlabeled.review":
                file_paths.append(os.path.join(root, file))

    reviews = []  # read in every positive and negative review as an element of this list
    for item in file_paths:
        with open(item, "r") as f:
            contents = [item for item in f.read().split("\n") if item != ""]
            reviews += contents

    # plan
    # take union of all words found in all reviews
    # create pandas dataframe with documents as rows and terms as columns

main()