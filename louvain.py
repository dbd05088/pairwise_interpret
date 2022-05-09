import community as community_louvain
import networkx as nx
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import pickle

file_name = "label_2_df.pkl"
with open(file_name,'rb') as f:
    df = pickle.load(f)
print(df.head())

#edges = df[['source','target']].values.tolist()
#weights = df['weight'].values.tolist

# graph 생성
G = nx.Graph()

# edge weight 추가
for i in range(len(df)):
    data = df.iloc[i]
    G.add_edge(data[0], data[1], weight = data[2])

print("partitioning 시작")
partition = community_louvain.best_partition(G, weight='weight')

print(partition)
with open('label2_partition_all.pkl','wb') as f:
    pickle.dump(partition,f)


'''
pos = nx.spring_layout(G)
cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=30,
                       cmap=cmap, node_color=list(partition.values()))
nx.draw_networkx_edges(G, pos, alpha=0.5)
plt.show()
'''