# N, M, K 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 정리하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second  # 두번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기

print(result)  # 최종 답안 출력

# 입력예시 5, 8, 3 (5개 숫자 입력, 8번 숫자 더하기, 3번 중복 가능)
# 입력예시 2 4 5 4 6

# 출력예시 46 (6+ 6+ 6+ 5+ 6+ 6+ 6+ 5) -> 36+ 10 -> 46
