'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행(조건문이 false가 될 때까지)
형식 :
while 조건식1:
    반복실행문

특정 시점에 while 반복문이 종료되게 지정
'''
n1 = 1
while n1 < 11:
    print(n1)
    n1 += 1         # python은 ++ 없음
'''
예제
10부터 1까지 역순 출력
'''
n2 = 10
while n2 > 0:
    print(n2)
    n2 -= 1
    while n2 > 0:
        print(n2)
        n2 -= 1
'''
중첩 while 문 (while문 뿐만 아니라 내부에 if문 사용 가능)
중첩 while 및 f-string을 활용해 
'''

dan = 2
while dan < 10:
    num = 1
    while num < 10:
        print(f"{dan} x {num} = {dan * num}")
        num += 1
    dan += 1