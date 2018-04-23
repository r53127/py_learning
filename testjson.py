import json
a={'a': '1111', 'b': '2222','c': '3333', 'd': '4444'}
with open('emb_json.json','w') as f:
    json.dump(a,f)
print(a)

name_emb = {'e': '5555', 'f': '6666'}

with open('emb_json.json','r') as fr:
    m = json.load(fr)
    print(type(m))
    print(m)


for i in name_emb:
    print(i)
    print(name_emb[i])
    m[i] = name_emb[i]
    print(m[i])

with open('emb_json.json', "w") as fw:
    json.dump(m,fw)
    fw.close()
