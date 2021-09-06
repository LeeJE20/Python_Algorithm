# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 2021.08.12

# 내 풀이
def letterCombinations(self, digits: str) -> List[str]:
    """
    @param todo: 앞으로 더 탐색해야하는 횟수
    """
    def dfs(idx: int, todo: int, combination: str):
        # 종료 조건:
        if todo == 0:
            result.append(combination)
            return

        #단어 조합
        # 7과 9는 4개 있기 때문에 노가다로 안 함
        # dfs(idx+1, todo-1, combination + d[digits[idx]][0])
        # dfs(idx+1, todo-1, combination + d[digits[idx]][1])
        # dfs(idx+1, todo-1, combination + d[digits[idx]][2])

        for letter in d[digits[idx]]:
            dfs(idx+1, todo-1, combination + letter)
        
    

    d = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z'],
    }



    result = []
    
    if len(digits) == 0:
        return result

    dfs(0, len(digits), "")

    return result


# 풀이1: 모든 조합 탐색
def letterCombinations(self, digits: str) -> List[str]:
    def dfs(idx: int, path):
        # 끝까지 탐색하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return
        
        # 입력값 자릿수 단위 반복
        for i in range(index, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in dic[digits[i]]:
                dfs(i+1, path + j)

    

    # 예외처리
    if not digits:
        return []

    dic = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }

    result = []
    dfs(0, "")

    return result