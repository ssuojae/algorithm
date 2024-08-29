def dfs(idx, current_value):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, current_value)
        min_result = min(min_result, current_value)
        return
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            
            if i == 0:  # 덧셈
                dfs(idx + 1, current_value + numbers[idx])
            elif i == 1:  # 뺄셈
                dfs(idx + 1, current_value - numbers[idx])
            elif i == 2:  # 곱셈
                dfs(idx + 1, current_value * numbers[idx])
            elif i == 3:  # 나눗셈
                if current_value < 0:
                    dfs(idx + 1, -(-current_value // numbers[idx]))
                else:
                    dfs(idx + 1, current_value // numbers[idx])
            operators[i] += 1  # 백트래킹

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')

dfs(1, numbers[0])

print(max_result)
print(min_result)
