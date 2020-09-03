a   =   int ( 입력 ()) # 수를 입력받음

count = 1 #1번 그룹

while a - count > 0:
    a = a - count
    count += 1

if count % 2 == 0: #짝수번째 그룹일 경우
    print(a, "/", (count + 1) - a, sep = "")
else: #홀수번째 그룹일 경우
    print((count + 1) - a, "/", a, sep = "")
