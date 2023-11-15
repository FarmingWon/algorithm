def inp():
    li = [['주석',50000, 50],
          ['백금',600000, 10],
          ['은',100000, 25],
          ['금',750000, 15]]
    
    return li

def knapsack(inp, Weight):
    weights = [[l[0],l[1], l[2], l[1]/l[2]] for l in inp]
    weights.sort(key=lambda x : x[3], reverse=True)
    L = [] # 담은 List
    w = 0 # 무게
    v = 0 # Value 

    while w + weights[0][2] <= Weight:
        x = weights.pop(0)
        L.append(x)
        w = w + x[2]
        v = v + x[1]
    
    if Weight - w > 0:
        x = weights.pop(0)
        tmp_w = Weight - w 
        w = w + tmp_w
        L.append([x[0], x[1] *((tmp_w) / x[2]), tmp_w, x[3]])
    print(L)
    print(w)
    print(v)
    

if __name__ == "__main__":
    inp = inp()
    knapsack(inp, 7) 