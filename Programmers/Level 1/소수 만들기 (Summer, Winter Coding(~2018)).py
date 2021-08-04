def solution(nums):
    answer = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                for l in range(2, nums[i] + nums[j] + nums[k]):
                    if (nums[i] + nums[j] + nums[k]) % l == 0:
                        break
                else:
                    answer += 1
                        
    return answer


''' 
다른 사람의 풀이 : 리스트의 모든 조합을 구하는 라이브러리 from itertools import combinations as cb
'''
