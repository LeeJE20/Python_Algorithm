# 타뷸레이션
# 작은 하위 문제부터 차례대로 정답을 풀어나가며 큰 문제의 정답을 만든다.
def fib_tabulation(n):
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 메모이제이션
# 하위 문제에 대한 정답을 계산했는지 확인해가며 문제를 자연스럽게 재귀로 풀어나감
# 기존 재귀와 거의 동일, 이미 풀어봤는지 확인하며 재활용
def fib_memoization(n):
    if n <= 1:
        return n

    if dp[n]:
        return dp[n]

    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]