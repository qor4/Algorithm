def solution(clothes):
    answer = 0
    kind=[i[1] for i in clothes]
    num = []
    count = 0
    kind.sort()
    name = kind[0]
    print(kind)
    for i in kind:
        print(i)
        if name == i:
            print("if", name)
            count += 1
        else:
            print("else", count)
            num.append(count)
            name = i
            count = 1
    num.append(count)
    answer = sum(num)        
    return answer
