

# 와일드카드 패턴 w가 문자열 s에 대응되는지 여부를 반환
def match(w: string, s: string)-> bool:
    # w[pos]와 s[pos]를 맞춰나간다.
    pos: int = 0
    while (pos < len(s) and pos < len(w) and (w[pos] == '?' or w[pos] == s[pos])):
        pos+= 1
    

    # 더이상 대응할 수 없으면 왜 while문이 끝났는지 확인
    # 2. 패턴 끝에 도달해서 끝난 경우: 문자열도 끝났어야 대응됨
    if (pos == len(w)):
        return pos == len(s)
    
    # 4. *를 만나서 끝난 경우: *에 몇 글자를 대응해야 할지 재귀 호출하면서 확인
    if w[pos] == '*':
        skip: int = 0
        while (pos + skip <= len(s)):
            if (match(w[pos+1:], s[pos+skip])):
                return True
            skip += 1
    
    # 이 외의 경우에는 모두 대응되지 않음
    return false