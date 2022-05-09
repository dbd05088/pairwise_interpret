import pickle
import pandas as pd

file_name = "label2_partition_all.pkl"
with open(file_name,'rb') as f:
    dic = pickle.load(f)

print(len(dic.keys()))
keys = dic.keys()

df_list = []
for key in keys:
    data = {}
    data['node'] = key
    data['partition'] = dic[key]
    df_list.append(data)

df = pd.DataFrame(df_list)
print(set(df['partition'].values.tolist()))
#print(df[df['partition']==0])
