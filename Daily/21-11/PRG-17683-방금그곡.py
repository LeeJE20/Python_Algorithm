'''idea
https://programmers.co.kr/learn/courses/30/lessons/17683
21.11.06 10:23 시작
11:41 끝

오류 참고:
https://programmers.co.kr/questions/14064

'''
# strr = "abc"
# strr = strr.replace('ab', '3')
# print(strr)

# code = {
#     'C':'1',
#     'D':'2',
#     'E':'3',
#     'F':'4',
#     'G':'5',
#     'A':'6',
#     'B':'7',
# }
# m = 'CA#BCC#BCC#BCC#B'
# shop_index = m.find('#')
# while shop_index != -1:
#     m = m[0:shop_index-1] + code[m[shop_index-1]] + m[shop_index+1:]
#     shop_index = m.find('#')
# print(m)

# a = "a, b, c"
# b = a.split(',')
# print(b)

# musicinfos = ["11:59,12:14,HELLO,CDEFGAB", "23:00,00:00,WORLD,ABCDEF"]
# m_info = []
# # 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열
# for i in musicinfos:
#     m_info.append(i.split(','))
# print(m_info)
# for idx, item in enumerate(m_info):
    
#         start = list(map(int, item[0].split(':')))
#         end = list(map(int, item[1].split(':')))
#         if end == [0,0]:
#             end = [24,0]
#         print(start)
#         print(end)
#         time = end[1]-start[1] + 60*(end[0]-start[0])
#         m_info[idx] = [time]+item[2:]
# print(m_info)





code = {
        'C':'1',
        'D':'2',
        'E':'3',
        'F':'4',
        'G':'5',
        'A':'6',
        'B':'7',
    }

# sheet = 'ab'
# length = len(sheet)
# time = 5
# iter, left = divmod(time, length)
# print(iter)
# print(left)
# note = sheet*iter + sheet[:left]
# print(note)

# #이 붙어있는 것은 한 음이므로, 알파벳과 분리하면 안 됨..
# cdefgab 에 #이 붙은 것은 숫자로 변환
# 1234567
def change_code(m):
    global code
    shop_index = m.find('#')
    while shop_index != -1:
        m = m[0:shop_index-1] + code[m[shop_index-1]] + m[shop_index+1:]
        shop_index = m.find('#')
    return m

def solution(m, musicinfos):
    m = change_code(m)
    m_info = []
    # 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 ','로 구분된 문자열 분리
    for i in musicinfos:
        m_info.append(i.split(','))
    
    for idx, item in enumerate(m_info):
        # 재생 시간(분 길이) 구하기
        start = list(map(int, item[0].split(':')))
        end = list(map(int, item[1].split(':')))
        # if end == [0,0]:
        #     end = [24,0]
        time = int(end[1]-start[1] + 60*(end[0]-start[0]))
        
        # 들려준 음악 구하기 (곡이 끝나면 이어서, 중간에 끊기면 끊긴 대로)
        sheet = item[-1]
        sheet = change_code(sheet)
        length = len(sheet)
        iter, left = divmod(time, length)
        note = sheet*iter + sheet[:left]

        # 재생시간, 순서, 제목, 들려준 음악으로 정보 변환
        m_info[idx] = [time, idx, item[2], note]


    print(m_info)
    # 문자열에서 기억하고 있는 것 구하기
    answer = []
    for i in m_info:
        note = i[-1]
        if m in note:
            answer.append(i)
    
    if not answer:
        return "(None)"
    answer = sorted(answer,key = lambda x: (-x[0], x[1]))
    # print(answer)

    
    return answer[0][2]

m = "ABCDEFG"
musicinfos = ["23:59,00:00,HELLO,ABC#DEFGAB", "11:00,00:00,WORLD,ABCDEF"]
ans = solution(m, musicinfos)
print(ans)