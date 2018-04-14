import pickle

a='中国人'
with open("d:/a.txt", "bw") as f:
    pickle.dump(a, f)