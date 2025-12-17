from collections import defaultdict, Counter
import numpy as np
import pandas as pd




def build_cooccurrence_matrix(terms, window_size=2):
    co_occ = defaultdict(Counter)


    for i, term in enumerate(terms):
        for j in range(max(0, i-window_size), min(len(terms), i+window_size+1)):
            if i != j:
                co_occ[term][terms[j]] += 1


    unique_terms = list(set(terms))
    idx = {t: i for i, t in enumerate(unique_terms)}
    matrix = np.zeros((len(unique_terms), len(unique_terms)), dtype=int)


    for t, neighbors in co_occ.items():
        for n, c in neighbors.items():
            matrix[idx[t]][idx[n]] = c


    return pd.DataFrame(matrix, index=unique_terms, columns=unique_terms)