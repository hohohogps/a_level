from math import floor

def merge(A: list, B: list) -> list:
    result = []
    while A and B:
        if A[0] > B[0]:
            result.append(B.pop(0))
        else:
            result.append(A.pop(0))

    result.extend(A)
    result.extend(B)

    return result
    
def merge_sort(C:list) -> list:
    if len(C) < 2:
        return C
    mid = len(C) // 2 
    A = merge_sort(C[:mid])
    B = merge_sort(C[mid:])
    return merge(A,B)

C = [3,2,1,4,5,9,13,58,94,35,83,13,3]
print(merge_sort(C))