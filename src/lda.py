# take input data, create topics

import sys
import time
import pickle
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation


# to call: python src\lda.py <input data file> <output path>

def main():
    t0 = time.time()

    input_file = sys.argv[1]
    topics_output_path = sys.argv[2]
    model_output_path = sys.argv[3]

    # load in data
    df = pd.read_csv(input_file, index_col=0)

    # get target column and training matrix
    target = df.iloc[:, -1][0]
    df = df.iloc[:, :-1]

    lda_model = LatentDirichletAllocation(n_components=50, learning_method='batch', max_iter=100, n_jobs=-1, verbose=1)
    lda_output = lda_model.fit_transform(df)

    print(lda_output.shape)

    cols = ["topic_"+str(i+1) for i in range(50)]
    df = pd.DataFrame(lda_output, columns=cols)
    df["sentiment"] = target

    df.to_csv(topics_output_path)

    print("Total time:", time.time()-t0)


main()
