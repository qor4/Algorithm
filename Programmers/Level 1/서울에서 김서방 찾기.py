def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 " + str(i) +"에 있다"
            
            
 '''
 index 함수 사용
 def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))
 '''
