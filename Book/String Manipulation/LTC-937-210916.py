"""
https://leetcode.com/problems/reorder-data-in-log-files/

937. Reorder Data in Log Files

난이도: Easy

시작: 21.09.16 10:48
끝: 21.09.16 11:35
성공: 1회 correct

메모리:  14.5 MB, less than 37.43%
시간:   28 ms, faster than 97.72%

[아이디어]
분리해서 문자, 숫자 따로 저장
문자는 정렬
합치기


[시간복잡도]
O(n)



"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        str_list = []
        num_list = []

        for log in logs:
            l = log.split()
            contents = ""
            is_number = True
            
            for i in range(1, len(l)):    
                if l[i].isalpha():
                    is_number = False
                contents += (" "+l[i])
                
            
            if is_number:
                num_list.append([l[0], contents])

            else:
                str_list.append([l[0], contents])


        str_list.sort(key = lambda x: (x[1], x[0]) )

        return list(map(lambda x: x[0]+x[1], str_list)) + list(map(lambda x: x[0]+x[1], num_list))