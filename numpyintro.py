from sklearn.datasets import load_breast_cancer
import pandas as pd
import numpy as np

def answer_one():
    cancer = load_breast_cancer()

    dfcancer=pd.DataFrame(data=np.c_[cancer['data'], cancer['target']], columns=np.append(cancer["feature_names"],["target"]))
    return(dfcancer.keys(), dfcancer.index)

answer_one()

def answer_two():
    cancer = load_breast_cancer()
    cancerdf = pd.DataFrame(data=np.c_[cancer['data'], cancer['target']], columns=np.append(cancer["feature_names"],["target"]))
    print(cancer.target_names)

answer_two()