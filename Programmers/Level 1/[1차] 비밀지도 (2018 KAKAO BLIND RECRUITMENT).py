def solution(n, arr1, arr2):
    answer = [] 
    tmp = ''
    for i in range(n):
        arr1[i] = bin(arr1[i])
        arr1[i] = arr1[i][2:]
        arr1[i] = ('0' * (n - len(arr1[i]))) + arr1[i]
        arr2[i] = bin(arr2[i])
        arr2[i] = arr2[i][2:]
        arr2[i] = ('0' * (n - len(arr2[i]))) + arr2[i]
    
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
        tmp = ''
    return answer
  
  '''import re sub 공부'''
