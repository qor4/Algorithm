def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer+='*'
    answer += phone_number[-4:]
    return answer
  
  '''
  answer*(len(phone_number)-4) 하면 됨
  
  def solution(phone_number):
    answer = ''
    answer ='*'*(len(phone_number)-4) + phone_number[-4:]
    return answer
 '''
