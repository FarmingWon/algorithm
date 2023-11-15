import pandas as pd

def get_graph():
    g = [10, 14]
    e = [[0,1,15],
         [1,2,21],
         [0,3,12],
         [3,4,4],
         [3,5,10],
         [4,5,3],
         [5,6,10],
         [1,6,7],
         [2,7,25],
         [6,7,19],
         [4,8,13],
         [8,9,15],
         [6,9,9],
         [7,9,5]]
    return g,e

def dijkstra(G, E):
    MAX = 999999
    graph = [[-1 for j in range(G[0])] for i in range(G[0])]
    for e in E:
        x,y = e[0], e[1]
        graph[x][y] = e[2]
        graph[y][x] = e[2]
    graphs = list()
    for i in range(G[0]):
        start = i # start vertex 
        D = [MAX for i in range(G[0])]
        D[start] = 0
        vertexs = []
        result = [MAX for i in range(G[0])]
        result[start] = 0 
        v_min = None
        while len(vertexs) != G[0] :
            MIN = MAX
            for i in range(G[0]):
                if i not in vertexs and D[i] < MIN:
                    MIN = D[i]
                    v_min = i 
            vertexs.append(v_min)
            #간선 완화
            w_s  = [v for v in range(G[0]) if  graph[v][v_min] != -1]
            for w in w_s:
                if D[w] > D[v_min] + graph[w][v_min]:
                    D[w] = graph[w][v_min] + D[v_min]
                    result[w] = (v_min, w, graph[w][v_min])
        print(result)
        graphs.append(D)        
    return graphs

if __name__ == "__main__":
    g,e = get_graph()
    D = dijkstra(g,e)
    cols = ['-', '서울', '원주', '강릉', '천안', '논산', '대전', '대구', '포항', '광주', '부산']
    for i_idx, d in enumerate(D):
        for j_idx in range(len(d)):
            if i_idx >= j_idx:
                D[i_idx][j_idx] = ""
        D[i_idx].insert(0, cols[i_idx+1])
    df = pd.DataFrame(D)
    df.to_csv("dijkstra.csv", index=False, header=cols, encoding="cp949")
