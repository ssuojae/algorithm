# 1. 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면
# 2. 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. 
# 3. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다
# 4. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

from itertools import combinations

# N번째 감소하는 수를 찾는 함수
def find_nth_decreasing_number(n):
    # 0부터 9까지의 숫자 중에서 감소하는 숫자를 만들 수 있음
    decreasing_numbers = []
    
    # 각 자릿수 조합을 구함 (1자리, 2자리, ... 10자리)
    for i in range(1, 11):
        for comb in combinations(range(10), i):
            # 각 조합을 역순으로 정렬해서 감소하는 수를 만듦
            decreasing_numbers.append(int(''.join(map(str, sorted(comb, reverse=True)))))
    
    # 감소하는 수들을 정렬
    decreasing_numbers.sort()
    
    # n번째 감소하는 수가 있으면 출력, 없으면 -1 출력
    if n >= len(decreasing_numbers):
        return -1
    else:
        return decreasing_numbers[n]

# 입력 받기
n = int(input())

# N번째 감소하는 수 출력
print(find_nth_decreasing_number(n))
