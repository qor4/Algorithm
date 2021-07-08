def solution(priorities, location):
    print_list=[]
    answer = 0
    for i in range(len(priorities)):
        print_list.append((i,priorities[i]))
    while(len(print_list)!=0):
        tmp = print_list[0]
        for i in range(1, len(print_list)):
            tmp2 = print_list[i]
            if tmp[1] < tmp2[1]:
                del print_list[0]
                print_list.append(tmp)
                break
        else:
            del print_list[0]
            answer +=1
            if tmp[0] == location:
                return answer
