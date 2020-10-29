# creates dataframe out of arff

import sys
import time
import pandas as pd
from scipy.io import arff


# to call: python src\arff_convert.py <input arff file> <output path>

def main():
    t0 = time.time()

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    data = arff.loadarff(input_dir)
    df = pd.DataFrame(data[0])

    df.to_csv(output_dir)

    print("The total time is:", time.time()-t0)

main()