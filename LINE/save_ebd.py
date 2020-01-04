import torch
import numpy as np

embed = torch.load('bit_model.pth').contextnodes_embeddings

feat = embed.weight.data.numpy()
print(feat.shape)
np.save('embedings', feat)
# for idx in range(embeddings.num_embeddings):
#     vector = embeddings.weight[idx].data
