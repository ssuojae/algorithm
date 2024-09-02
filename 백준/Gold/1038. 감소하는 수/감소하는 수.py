# 내가 풀었던 답... 시간초과 아오지납리ㅏㅂㅈ러댜ㅓㄹ빋ㄹㅎ
def main2():
    input_num = int(input())
    # 0에서 9까지는 그대로 출력
    if 0 <= input_num <= 9:
        print(input_num)
        return

    count = 9  # 0에서 9까지는 이미 카운트된 상태로 시작
    # 주어진값 최대: 1,000,000
    for num in range(10, 9876543210):
        if is_decrement(num):
            count+=1
            if count==input_num:
                print(num)
                return

    
    # 만약 N번째 감소하는 수가 존재하지 않는다면 -1 출력
    print(-1)

def is_decrement(num):
    str_num = str(num)
    for digit in range(len(str_num)-1):
        if int(str_num[digit]) <= int(str_num[digit+1]):
            return False
    return True


# 해답지 복사 이분은 조합으로 푸셨네..
from itertools import combinations

N = int(input())

result = []
for i in range(1, 11):
	for j in combinations(range(10), i):
		num = ''.join(list(map(str, reversed(list(j)))))
		result.append(int(num))

result.sort()
if N >= len(result):
	print(-1)
else:
	print(result[N])

