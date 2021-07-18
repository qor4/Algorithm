def solution(record):
    answer = []
    user = {}
    for i in record:
        if i[0] == "E":
            action, uid, name = i.split()
            user[uid] = name
        elif i[0] == "C":
            action, uid, name = i.split()
            user[uid] = name
    for i in record:
        if i[0] == "L":
            action, uid = i.split()
            answer.append(user[uid]+"님이 나갔습니다.")
        elif i[0] == "E":
            action, uid, name = i.split()
            answer.append(user[uid]+"님이 들어왔습니다.")
    return answer
