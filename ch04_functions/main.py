'''
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 매서드(methods)
    3) 사용자 정의 함수
2. 함수 용어 정리
    1) 함수 정의 : 사용자 함수를 새로 만드는 것(def: define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변숴
    4) 반환값 / 결과값 / 리턴값 : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것
3. (사용자) 함수의 형식 :
def 함수_이름(매개변수1, 매개변수2):
    실행문
    return문

변수 =  함수_이름(argument1, argument2)
'''

# 함수 정의
def display_name(name):
    print(f'당신 이름은 {name}입니다.')

# 함수 호출
display_name('김일')

def display_name_age(name, age):
    print(f'당신 이름은 {name}이고 나이는 {age}살입니다.')

display_name_age('김이', 30)
display_name_age(age=23, name='김삼')     # keyword argument

'''
예를 들어 input('이름을 입력하세요 >>> ')로 name이라는 변수에 담았다고 가정하면
name = input('이름을 입력하세요 >>> ')라고 작성

이는 input()이라는 파이썬 내장 함수를 사용하고 있었다고 볼 수 있는데 
파이썬 내장 함수는 이미 정의가 되어 있어서 호출만으로 해결되는 문제들

사용자 정의 함수는 개발자 자신이 함수를 정의하고 그 후에 호출까지 하는 과정

내장 함수 예시
print() / type() / int() / float() / input()

2. 메서드(methods) : 특정 객체가 가지고 있는 함수로서 특정 자료형에 포함된 함수
   함수와 메서드는 동일한 개념이지만 호출에 있어서 차이 존재

함수는 독립적 사용 가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''
# 메서드의 예시
# eng_name = input('당신의 이름을 영어로 입력하세요 >>> ').capitalize()
# print(eng_name)
'''
이러한 코드는 함수 호출로 결과값을 eng_name이라는 변수에 담았다고 볼 수 있고 결과값 자료형은 str
'''
# print(eng_name)
# eng_name = eng_name.upper()
# print(eng_name)
'''
eng_name.upper()의 경우 .upper()가 메서드에 해당하고 해당 메서드는 str 자료형에 종속됬다고 볼 수 있는데
그 결과값을 다시 eng_name에 담아서 두 결과값의 차이 발생

함수(메서드)의 유형
'''
# 매개 변수 x / 리턴 x
def call1():
    print('[x | x]')

# 매개 변수 o / 리턴 x
def call2(unknown_parameter):
    print('[o | x]')
    print(f'{unknown_parameter}라고 입력')

# 매개 변수 x / 리턴 o
def call3():
    print('[x | o]')
    return 1

# 매개 변수 o / 리턴 o
def call4(unknown1, unknown2):
    print('[o | o]')
    return unknown1 + unknown2

call1()
call2('오늘 날씨는 시원한 편')
call2(123456)
call3()     # 결과값 : [x | o]
print(call3())
print(call4('안녕', '하세요'))
print(call4(unknown2=1234, unknown1=5678))

'''
700원짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하고 돈을 넣으면 몇잔의 음료가 나오는지 잔돈은 얼마인지 모든 경우의 수 출력

함수 정의 
- 반횐값 : 없음(call1~call4 유형 고민)
- 함수 이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성
def vending_machine():
    # 함수 구현
    
vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''

def vending_machine(money):
    cost = 700
    drink = 0
    while drink * cost < money:
        change = money - drink * cost
        print(f'음료수 = {drink}개, 잔돈 = {change}원')
        drink += 1
vending_machine(3000)


def vending_machine2(money):
    cost = 700
    drink = money // cost
    for i in range(drink+1):
        change = money - i * cost
        print(f'음료수 = {i}개, 잔돈 = {change}원')
        drink += 1
vending_machine2(3000)

'''
예제 : 구구단 출력하기 
함수 정의  :
함수 이름 : multiply
매개변수 : 정수 n
리턴값 : 없음

함수 호출 : 
multiply(dan)    # argument를 dan

실행 예
몇 단을 출력하시겠습니까? >>> 3
3 x 1 = 3
....
3 x 9 = 27
'''
# def multiply(dan):
#     for i in range(1, 10):
#         print(f'{dan} x {i} = {dan * i}')
#
# num = int(input('몇 단을 출력하시겠습니까? >>> '))
# multiply(num)

'''
range 함수의 parameter 적용 순서
1개 : 한계값
2개 : 시작값, 한계값
3개 : 시작값, 한계값, 증감값

multiply를 call2() 유형으로 정의 했는데 call1() 유형으로 정의하면

multiply2를 call1() 유형으로 정의했을 때
실행 예
몇 단을 출력하시겠습니까? >>> 3
5 x 1 = 5
....
5 x 9 = 45
'''
def multiply(dan):
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')

num = int(input('몇 단을 출력하시겠습니까? >>> '))
multiply(num)

def multiply2():
    dan = int(input('몇 단을 출력하시겠습니까? >>> '))
    for i in range(1, 10):
        print(f'{dan} x {i} = {dan * i}')
multiply2()

# call3: 매개변수 없음 / 리턴 있음
def multiply3():
    dan = int(input('몇 단을 출력하시겠습니까? >>> '))
    result = []
    for i in range(1, 10):
        result.append(f'{dan} x {i} = {dan * i}')
    return result

gu_gu = multiply3()
for line in gu_gu:
    print(line)

# call4: 매개변수 있음 / 리턴 있음
def multiply4(dan):
    result = []
    for i in range(1, 10):
        result.append(f'{dan} x {i} = {dan * i}')
    return result

dan_num = int(input('몇 단을 출력하시겠습니까? >>> '))
gu_gu = multiply4(dan_num)
for line in gu_gu:
    print(line)