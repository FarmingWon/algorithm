MAX = 99999

def get_kruskal_arr():
    g = [6,10] # |vertex|, |edges|
    inp = [[0, 1, 8],  # start end weight 
        [0, 3, 2],
        [0, 4, 4],
        [1, 2, 1],
        [1, 3, 4],
        [1, 5, 2],
        [2, 5, 1],
        [3, 4, 3],
        [3, 5, 7],
        [4, 5, 9]]
    return g, inp

def get_prim_arr():
    g = [6, 10]
    inp = [[0, 3, 2],
        [0, 4, 4],
        [1, 0, 3],
        [1, 3, 4],
        [1, 5, 2],
        [2, 1, 1],
        [2, 5, 1],
        [3, 4, 5],
        [3, 5, 7],
        [4, 5, 9]]
    return g, inp

def weight_cal(T):
    sum = 0
    for t in T:
        sum = sum + t[2]
    return sum

#start end  
def if_cycle(parent, start, end):
    rootX = find(parent, start)
    rootY = find(parent, end)
    return rootX != rootY

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)   
    parent[rootY] = rootX

def Kruskal(G, T):
    result = []
    T.sort(key=lambda x:x[2])
    parent = [i for i in range(G[0])]

    while len(result) < G[0] - 1:
        li = T.pop(0)
        cycle = if_cycle(parent, li[0], li[1])
        if cycle:
            result.append(li)
            union(parent, li[0], li[1])
    return result

def Prim(G, T):
    p = 2 # start vertex
    D = [MAX for i in range(G[0])]
    D[p] = 0 # 시작점 초기화
    result_li = [None for i in range(G[0])]
    result_li2 = list()
    # 2~6
    tmp = [t for t in T  if t[0] == p or t[1] == p]
    for t in tmp:
        if t[0] == p:
            D[t[1]] = t[2]
            result_li[t[1]] = t
            result_li2.append(t)
        else:
            D[t[0]] = t[2]
            result_li[t[0]] = t
            result_li2.append(t)

    # mst 
    start_p = p
    result = [p]
    while len(result) < G[0]: 
        find_min = MAX
        for i in range(G[0]):
            if i not in result and D[i] < find_min:
                find_min = D[i]
                p = i
        result.append(p) # 가장 가까운 점 APPEND 
        v_min = [t for t in T  if t[0] == p or t[1] == p]
        for v in v_min:
            if v[0] == p and D[v[1]] > v[2] and v[1] not in result:
                D[v[1]] = v[2]
                result_li[v[1]] = v
                result_li2.append(v)
            elif v[1] == p and D[v[0]] > v[2] and v[0] not in result:
                D[v[0]] = v[2]
                result_li[v[0]] = v
                result_li2.append(v)

    result_li.pop(start_p)
    print(result_li2)
    return result_li


if __name__ == '__main__':
    G, T = get_kruskal_arr()
    print(f"input : {G} , {T}")
    kruskal_Result = Kruskal(G,T)
    print(f"Kruskal : {kruskal_Result}, weight sum : {weight_cal(kruskal_Result)}")
    print('---' * 43)
    G, T = get_prim_arr()
    print(f"input : {G} , {T}")
    prim_Result = Prim2(G,T)
    print((f"Prim : {prim_Result}, weight sum : {weight_cal(prim_Result)}"))
    