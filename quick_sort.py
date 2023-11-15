import pandas as pd
import time 

def Quick_sort(A, left ,right): # median_of_three pivot
    if left < right:
        pivot = median_of_three(left,(left+right)//2 ,right, A)
        A[left], A[pivot] = A[pivot], A[left]
        cur_left = left+1 
        cur_right = right
        while cur_left < cur_right:
            while A[left] >= A[cur_left]:
                cur_left = cur_left + 1
            while A[left] <= A[cur_right]:
                cur_right = cur_right - 1
            if cur_left < cur_right:
                A[cur_left], A[cur_right] = A[cur_right], A[cur_left]
        A[left], A[cur_left-1] = A[cur_left-1], A[left]
        Quick_sort(A, left, cur_left-1)
        Quick_sort(A, cur_left, right)
        return A
    
def Quick_sort_mid_pivot(A, left ,right): # mid pivot
    if left < right:
        pivot = (left+right)//2
        A[left], A[pivot] = A[pivot], A[left]
        cur_left = left+1 
        cur_right = right
        while cur_left < cur_right:
            while A[left] >= A[cur_left]:
                cur_left = cur_left + 1
            while A[left] <= A[cur_right]:
                cur_right = cur_right - 1
            if cur_left < cur_right:
                A[cur_left], A[cur_right] = A[cur_right], A[cur_left]
        if A[left] > A[cur_left-1]:   
            A[left], A[cur_left-1] = A[cur_left-1], A[left]
        elif A[left] > A[cur_left]:
            A[left], A[cur_left] = A[cur_left], A[left]
        Quick_sort(A, left, cur_left-1)
        Quick_sort(A, cur_left, right)
        return A
        
def median_of_three(first, mid, last, A):
    if A[first] <= A[mid] and A[mid] <= A[last]:
        return mid
    if A[last] <= A[mid] and A[mid] <= A[first]:
        return mid
    if A[first] <= A[last] and A[last] <= A[mid]:
        return last
    if A[mid] <= A[last] and A[last] <= A[first]:
        return last
    return first

def read_xlsx(path): # read xlsx
    df = pd.read_excel(path)
    df = df.values.tolist()
    li = [i[0] for i in df]
    return li

def read_data(path): # read txt
    f = open(path, 'r')
    lines = f.readlines()
    li = [int(i) for i in lines]
    return li
        

def eval(quick_sorted, GT):
    if quick_sorted == GT:
        return "두 함수의 비교 결과 같습니다."
    else:
        return "두 함수 비교 결과 다릅니다."

if __name__ == "__main__":
    path = "C:/Users/DSL/Desktop/python/data/inupt_quick_sort.txt"
    A = read_data(path)
    B = A.copy()

    Result = Quick_sort(A, 0, len(A)-1)
    B.sort()
    print(f"Quick, 내장 sort 후 비교{eval(Result,B)}")

    print()

    # -----시간 측정 -----------
    start = time.time_ns()
    for i in range(1000):
        C = read_data(path)
        C.sort()
    end = time.time_ns()
    print(f"내장 Sort :%7dns" %(end-start))

    print('------'*20)

    start = time.time_ns()
    for i in range(1000):
        A = read_data(path)
        result1=  Quick_sort(A, 0, len(A)-1)
    end = time.time_ns()
    print(f"Quick Sort : left, mid, right를 기준으로 중앙값 pivot: %7dns" %(end-start))

    print('------'*20)
    start = time.time_ns()
    for i in range(1000):
        B = read_data(path)
        result2=  Quick_sort_mid_pivot(B, 0, len(B)-1)
    end = time.time_ns()
    print(f"Quick Sort : mid값 pivot :%7dns" %(end-start))
