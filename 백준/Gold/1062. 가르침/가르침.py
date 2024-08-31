# 문제
# 남극에 사는 김지민 선생님은 학생들이 되도록이면 많은 단어를 읽을 수 있도록 하려고 한다.
# 김지민은 K개의 글자를 가르칠 시간 밖에 없다
# 김지민이 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다.
# 김지민은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민
# 남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다
# 남극언어에 단어는 N개 밖에 없다고 가정한다
# 김지민이 K개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값 출력

from itertools import combinations

n, k = map(int, input().split())
words = []
additional_letters = set()

# 단어 입력 및 처리
for _ in range(n):
    word = input()
    word_set = set(word[4:-4])  # "anta"와 "tica"를 제외한 나머지 문자만 추출
    words.append(word_set)
    additional_letters.update(word_set)

# 필수 요소 설정
essential = {'a', 'n', 't', 'i', 'c'}

# K가 5보다 작으면 어떤 단어도 읽을 수 없음
if k < 5:
    print(0)
else:
    # 필수 요소와 추가로 가르칠 수 있는 문자의 개수
    additional_letters = list(additional_letters - essential)
    
    # 만약 가르칠 수 있는 문자 수가 K - 5보다 적다면:
    if len(additional_letters) <= k - 5:
        # 모든 단어를 읽을 수 있음
        print(n)
    else:
        max_count = 0
        # 추가로 가르칠 수 있는 문자들의 조합을 생성
        for comb in combinations(additional_letters, k - 5):
            comb_set = essential | set(comb)  # 필수 문자와 결합
            count = 0
            
            # 각 단어에 대해, 해당 조합으로 읽을 수 있는지 확인
            for word in words:
                if word <= comb_set:
                    count += 1

            max_count = max(max_count, count)

        print(max_count)
