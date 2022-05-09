import pickle
import os
import numpy as np
import pandas as pd

graph_list = []
# pickle load

i = 2
file_name = "pairwise_scores" + str(i) + ".txt"
print("file_name", file_name)
with open(file_name,'rb') as f:
    lines = f.readlines()
    for line in lines:
        dic  = {}
        line = line.decode('utf-8')
        dic['source'] = int(line.split()[0])
        dic['target'] = int(line.split()[1])
        dic['weight'] = float(line.split()[2])
        graph_list.append(dic)

graph_df = pd.DataFrame(graph_list)
print(len(graph_df))
print(graph_df.head())
graph_df.to_pickle("label_2_df.pkl")
        
