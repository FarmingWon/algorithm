import pandas as pd

def get_graph_DP():
    G = [5, 14]
    E = [[1,2,4], # start, end, weight
         [1,3,2],
         [1,4,5],
         [2,3,1],
         [2,5,4],
         [3,1,1],
         [3,2,3],
         [3,4,1],
         [3,5,2],
         [4,1,-2],
         [4,5,2],
         [5,2,-3],
         [5,3,3],
         [5,4,1]] 
    return G,E

def get_graph_Greedy():
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
def Floyd_Warshall(G, E):
    # Graph 구축
    MAX = 99999
    D = [[MAX  if i != j else 0 for j in range(G[0]) ] for i in range(G[0])]
    for e in E:
        D[e[0]][e[1]] = e[2] 
        D[e[1]][e[0]] = e[2]
    #print 
    # print("초기 Graph")
    # print(D)
    # print("---"*40)

    #Floyd Warshall Algirothm
    for k in range(G[0]):
        for i in range(G[0]):
            if i != k:
                for j in range(G[0]):
                    if j!= k and j!=i:
                        D[i][j] = min(D[i][k]+D[k][j], D[i][j])
    # print("All Paris Shortest Paths")
    # print(D)
    return D



if __name__ == "__main__":
    G,E = get_graph_Greedy()
    D = Floyd_Warshall(G,E)
    cols = ['-', '서울', '원주', '강릉', '천안', '논산', '대전', '대구', '포항', '광주', '부산']
    for i_idx, d in enumerate(D):
        for j_idx in range(len(d)):
            if i_idx >= j_idx:
                D[i_idx][j_idx] = ""
        D[i_idx].insert(0, cols[i_idx+1])
    df = pd.DataFrame(D)
    df.to_csv("Floyd_Warshall.csv", index=False, header=cols, encoding="cp949")
