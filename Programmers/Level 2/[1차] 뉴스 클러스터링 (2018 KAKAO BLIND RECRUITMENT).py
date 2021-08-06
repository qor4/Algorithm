def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    intersection = []
    sum_of_set = []
    str1_cut = []
    str2_cut = []
    for i in range(1, len(str1)):
        tmp = str1[i-1] + str1[i]
        if tmp.isalpha() :
            str1_cut.append(tmp)
    for i in range(1, len(str2)):
        tmp = str2[i-1] + str2[i]
        if tmp.isalpha() :
            str2_cut.append(tmp)
            
    for i in str1_cut[:]:
        if str2_cut.count(i) == 0:
            sum_of_set.append(i)
            str1_cut.remove(i)
        else:
            intersection.append(i)
            sum_of_set.append(i)
            str1_cut.remove(i)
            str2_cut.remove(i)
    for i in str2_cut[:]:
        if str1_cut.count(i) == 0:
            sum_of_set.append(i)
            str2_cut.remove(i)
        else:
            sum_of_set.append(i)
            intersection.append(i)
            str1_cut.remove(i)
            str2_cut.remove(i)
    if len(sum_of_set) != 0:
        return int((len(intersection)/len(sum_of_set)) * 65536)
    else:
        return 65536
      
 '''
 다른 사람 풀이 참고하기
    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)
'''
