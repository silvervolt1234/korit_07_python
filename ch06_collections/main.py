'''
python 대표 collections
1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능 / 순서 있음
2. tuple 튜플 : 추가 / 수정 / 삭제가 불가능 / 순서 있음
3. set 세트 : 중복된 값의 저장이 불가능 / 순서 없음
4. dict 딕셔너리 : 키 + 값으로 관리
'''
import numbers

# list_example = [30, 40, '김이', [100, '김삼']]
# tuple_example = (10, 20, 30, '김사')
# set_example = {100, 200, 300, 400, '김오'}
# dictionary_example = {'이름': '김일', '나이': 20, '학교': '코리아아이티'}
#
# print(list_example)
# print(tuple_example)
# print(set_example)
# print(dictionary_example)
'''
1. list 
    여러 값을 저장할 떄 가장 많이 사용. 자료형이 다르더라도 하나의 리스트에 저장 가능
    하나의 배열(파이썬에서 리스트와 비슷한 개념)에 동일한 자료형만 저장 가능한 
    C, Java에 비해 python의 장점 중 하나(그 외에는 JS)
'''
# list의 선언 및 초기화
li1 = [1, 2, 3, '김사']
'''
    1-1. list의 index / slice
        list는 str과 동일한 index / slicing을 지원
        1) 인덱스 / 마이너스 인덱스
'''
print(li1[0])
print(li1[1])
print(li1[2])
print(li1[3])
print(li1[-1])
print(li1[-2])
print(li1[-3])
print(li1[-4])
'''
        2) slicing
        str의 슬라이싱처럼 '시작인덱스:종료인덱스:증갑값' 구성
'''
li2 = [100, 3.14, 'hello']  # list 선언 및 초기화 방법 # 1
li3 = list([4,5,6,7,8,9,0])    # list 선언 및 초기화 방법 # 2
print(li3[0:4:2])   # 0번지부터 4번지 앞까지 2씩 증가시키며   # 결과값: [4, 6]
'''
li3을 Java 버전으로 생각하면
String strExample = new String("안녕하세요"); 와 동일
String strExample = "안녕하세요"의 형식을 쓰지 않는다
        3) list element의 추가와 삭제
        list에 새로운 요소를 추가할 때는 .append() / .insert() 메서드 사용 가능
        기존 요소 삭제시 .pop() 메서드 사용
        
        .append() - 항상 마지막 인덱스에 element 추가
        .insert(위치, 값) - 정채진 위치(인덱스)에 해당 값 추가
'''
scores = [30, 40, 50]
print(scores)
scores.append(100)
print(scores)
scores.insert(0, 90)
print(scores)
''' 
        .pop()의 경우 빈 괄호로 사용시(call3 유형인 경우) 맨 마지막 요소 삭제
        .pop(인덱스넘버)로 작성하면 해당 인덱스 마지막 요소 삭제
'''
print(scores.pop()) # .pop()는 call3() 유형으로 return값이 있는데 그 삭제한 element가 return되기에
                    # print(scores.pop())은 연해 scores의 마지막 element인 100을 출력
print(scores.pop(0))    # 결과값 :90
'''
추가 삭제 메서드 : .remove(값)을 사용시 list 내에서 해당 값을 삭제(argument로 인덱스 넘버 요구가 아닌 데이터 요구)
'''
print(scores.remove(50))        # 결과값 : None / 특정값을 삭제했기에
print(scores)                   # 결과값 : [30, 40]
'''
li4 리스트를 선언하고 1부터 10까지 삽입
print(li4) 결과값은 [1,2,3,4,5,6,7,8,9,10]
'''
li4 = []
for i in range(1, 11):
    li4.append(i)
# for i in range(10):
#     li4.append(i+1)
print(li4)

'''
각 list 내의 element를 뽑아서 * 2
일반 for문 형식으로 하나
enhanced-for문 형식으로 하나 해서 첫 element를 4로 만들기
'''
for i in range(len(li4)):
    new_element = li4[i] * 2
    li4[i] = new_element
print(li4)
for i, j in enumerate(li4):
   new_element = j * 2
   li4[i] = new_element
print(li4)

'''
2. tuple
    저장된 값을 변경할 수 없는 list. 순서는 있어서 index 넘버와 slicing은 가능하나 저장된 값 이외에 추가 / 수정 / 삭제 불가능
    소괄호를 이용해 생성
'''
tu1 = (1,2,3)       # 튜블 생성 방법 # 1  # 주로 사용 방법
tu2 = tuple((4,5,6))  # 튜플 생성 방법 # 2
tu3 = 7, 8, 9       # 튜블 생성 방법 # 3  # 변수 하나에 데이터 여러개

a, b, c = 7, 8, 9   # 복수의 변수 선언 및 초기화 -> 변수 개수와 데이터 개수가 같으면 가능
print(a)
print(b)
print(c)

tu4 = 0
print(type(tu4))    # 결과값 : <class 'int'>
# tu4라고 해서 튜플로 생각하고 변수명을 지었지만 실제로는 그냥 int 변수명

tu5 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(type(tu5))
'''
element 추출 및 slicing은 동일
tuple의 특성상 element의 추가 /수정 / 삭제 역시 불가
'''
tu6 = 'hello.', 'good morning.', 'my name is', 'kim-il', 'i am', '20', 'years old.'
for i in tu6:
    print(i.title(), end=' ')   # 결과값 : Hello. Good Morning. My Name Is Kim-Il I Am 20 Years Old.
print()
print(tu6)
'''
collection의 개볌과 내부 element의 자료형은 서로 다르다
tuple의 정의는 내부 element의 추가 / 수정 / 삭제가 불가능한 colleciton이지만 element들은 가공이 가능
가공해서 tuple에 대입 역시 불가능
'''

'''
3. set
    수학에서의 집합 개념. Java와 동일
'''
set1 = {1, 2, 3}   # 세트 생성 방법 # 1
set2 = set({4, 5, 6})   # 세트 생성 방법 # 2
print(set1)
print(set2)

# 1/2 로 구분한 이유 : 빈 list / tuple / set 생성 방법
li = []
tu = ()
se = {}

print(type(li))     # 결과값: <class 'list'>
print(type(tu))     # 결과값: <class 'tuple'>
print(type(se))     # 결과값: <class 'dict'>
'''
    se = {} 형태로 비어있는 set을 생성할 경우 se는 <class 'dict'>로 dictionary 자료형으로 출력
    그래서 빈 set을 생성하려면 2번 형태가 필수
'''
se2 =set({})
print(type(se2))    # 결과값: <class 'set'>
'''
    list / tuple은 index가 존재하는데 이 둘을 sequence라고 하고
    set / dictionary의 경우 index가 없어서 비시퀀스라는 표현 사용(슬라이싱 x)
        
        element 관련 메서드
            1. .add() - set에 새로운 element 추가
            2. .remove() - 기존 element 삭제
            3. .discard() - 기존 element 삭제
'''
se3 = {10, 20, 30}
se3.add(50)
print(se3)  # 결과값 : {10, 20, 50, 30}
se3.remove(30)  # 순서가 없어서 값을 정확하게 입력
print(se3) # 결과값 : {10, 20, 50}

# remove() vs. discard()
# se3.remove(70)    # 오류 발생 - 갑을 정확하게 입력해야만 함
se3.discard(70)      # 오류 x. discard는 element 정확한 값 없으면 종료
print(se3)

# 향상된 for문으로 element 추출 가능하나 순서 보장 안됨
for element in se3:
    print(element)

''' 
4. dict(ionary) - Java에서의 Map / JS에서의 Object / JSON과 같은 형식                 
'''
dict1 = {
    '이름':'김일',
    '나이':20,
    '주소':['서울특별시','마포구','목동'],
}
'''
    주소 라인 까지 key-value pair가 존재하는데 마지막 property에 콤마 찍어주는게 매너
    
    딕셔너리에 인덱스는 존재하지 않지만 key를 인덱스와 유사하게 사용. 즉 key를 알면 값을 확인 가능
'''
# list의 element 추출 반복문 작성
li01 = [10,20,30,40]
for num in li01:
    print(num)

# dictionary에서 같은 방식의 반복문을 활용하게 될 때
# dictionary / JS Object에서 향상된 for문으로 반복문을 돌리면 key가 나오기에
# 딕셔너리명[key]로 작성해야 value 조회 가능
for key in dict1:
    print(dict1[key])

# key들만 추출하는 메서드
print(dict1.keys())           # 결과값: dict_keys(['이름', '나이', '주소'])
print(type(dict1.keys()))     # 결과값: <class 'dict_keys'>

# value들만 추출하는 메서드
print(dict1.values())         # 결과값: dict_values(['김일', 20, ['서울특별시', '마포구', '목동']])
print(type(dict1.values()))   # 결과값: <class 'dict_values'>

# key들만 뽑아서 list를 만들거나 / values만 뽑아서 list를 만들려면 형변환 함수 사용

keys = list(dict1.keys())
values = list(dict1.values())
print(keys)                     # 이제 인덱스로 추출 가능
print(values)

'''
collections에서 중요한 것은 list만 고려하는게 아니라 
set, tuple, dictionary 로 자료형 변경 / 가능 방식 / 쓸 상황등 종합적인 고려하는 역량이 중요
'''
# dictironary에서 property 추가 / 삭제
dict1['직업'] = '웹 퍼블리셔'      # 기존에 없는 키를 입력하고 value 지정
print(dict1)
dict1['직업'] = '웹 개발자'       # key 하나당 value는 고정이기에 재대입 발생
print(dict1)
# 삭제 방법
dict1.pop('직업')                # key를 알아야 삭제 가능 / .pop()의 return 특성 중요
print(dict1)

'''
응용 예제

list [10, 20, 30, 40, 50, 60, 70, 80, 90,100]의 3번째 요소부터 7번째 요소까지만 추출하고 
그 리스트에서 2번째 요소를 출력하는 프로그램 작성

실행 예
3 번째 요소부터 7 번째 요소 = [30, 40, 50, 60, 70, 80, 90, 100]
3 번째 요소부터 7 번째 요소 중 2번째 요소 = 40
'''
li001 = []
for i in range(10, 101, 10):
    li001.append(i)
print(li001)
li001_sliced = li001[2:7]
print(f"3 번째 요소부터 7 번째 요소 = {li001_sliced}")
print(f"3 번째 요소부터 7 번째 요소 중 2번째 요소 = {li001_sliced[1]}")
print()
print(f"3 번째 요소부터 7 번째 요소 = {li001[2:7]}")
print(f"3 번째 요소부터 7 번째 요소 중 2번째 요소 = {li001[2:7][1]}")

'''
사용자로부터 1에서 12까지 월을 입력받아 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성(윤년 무시)

실행 예
1 ~ 12 사이의 월을 입력하시오 >>> 2
2월은 28일까지입니다.
'''
# 1. dictionary 이용 방법
cal1 = {
    '1':'31',
    '2':'28',
    '3':'31',
    '4':'30',
    '5':'31',
    '6':'30',
    '7':'31',
    '8':'31',
    '9':'30',
    '10':'31',
    '11':'30',
    '12':'31',
}

num1 = input('1 ~ 12 사이의 월을 입력하시오 >>> ')
print(f'{num1}월은 {cal1[num1]}일까지입니다.')


# 2. list를 사용(마지막 날짜 입력)
cal2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num2 = int(input('1 ~ 12 사이의 월을 입력하시오 >>> '))
print(f'{num2}월은 {cal2[num2-1]}일까지입니다.')

# 3. list를 사용(28, 30, 31만 사용)-1
cal3 = [28, 30, 31]
num3 = int(input('1 ~ 12 사이의 월을 입력하시오 >>> '))
if num3 <= 7:
    if num3 % 2 == 1 :
        print(f'{num3}월은 {cal3[2]}일까지입니다.')
    elif num3 % 2 == 0:
         if num3 != 2:
            print(f'{num3}월은 {cal3[1]}일까지입니다.')
         else:
            print(f'{num3}월은 {cal3[0]}일까지입니다.')
elif num3 >= 8:
    if num3% 2 == 0 :
        print(f'{num3}월은 {cal3[2]}일까지입니다.')
    elif num3% 2 == 1:
        print(f'{num3}월은 {cal3[1]}일까지입니다.')

# 4. list를 사용(28, 30, 31만 사용)-1
cal4 = [28, 30, 31]
num4 = int(input('1 ~ 12 사이의 월을 입력하시오 >>> '))
if num4 == 2:
    cal4date = cal4[0]
elif num4 == 4 or num4 == 6 or num4 == 9 or num4 == 11:
    cal4date = cal4[1]
elif num4 == 1 or num4 == 3 or num4 == 5 or num4 == 7 or num4 == 8 or num4 == 10 or num4 == 12:
    cal4date = cal4[2]
print(f'{num4}월은 {cal4date}일까지입니다.')

'''
이상의 코드에서 중점은 in으로 in 두이ㅔ는 반복 가능객체(iterable)가 올 수 있다
그래서
elif num3 in [1,3,5,7,8,10,12]:
    cal3date = cal3[2]
의 해석은 in 다음 list를 초기화해 num3가 임의의 list의 element값을 가지고 있는지 여부를 조건 검토

(1,3,5,7,8,10,12)로 초기화 해도 무관
'''

'''
응용 예제
수학 여행을 어디로 갈 건지 결정하기 위해 학생들이 희망하는 모든 수학여행 장소를 조사하기로 했는데
학생들이 원하는 장소를 입력받아 동일한 입력을 무시하고 모든 입력을 저장할 때
학생을 3명으로 가정하고 실행 예처럼 동작하는 프로그램 작성

실행 예

희망하는 수학 여행지를 입력하세요 >>> 제주
희망하는 수학 여행지를 입력하세요 >>> 제주
희망하는 수학 여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.
'''
place1 = set({})
place2 = []
stu = int(input('학생 수를 입력하세요 >>> '))
for i in range(stu):
    want = input('희망하는 수학 여행지를 입력하세요 >>> ')
    if want not in place1:
        place1.add(want)
    if want not in place2:
        place2.append(want)
print(f'조사된 수학여행지는 {place1}입니다.')
print(f'조사된 수학여행지는 {place2}입니다.')
'''
짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력받고 그 정수만큼 숫자를 입력 받아 list에 저장
이후 새 list에 저장해 출력 프로그램을 작성

실행 예
몇 개의 숫자를 입력할까요 >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력받은 숫자는 [10, 15, 20, 25, 30]입니다.
입력받은 숫자들 중 짝수는 [10, 20, 30]입니다.
'''
s_num1 = []
s_num2 = []
insert_num = input('몇 개의 숫자를 입력할까요 >>> ')
for i in range(int(insert_num)):
    target_num = int(input(f'{i+1}번째 숫자를 입력하세요 >>> '))
    s_num1.append(target_num)
    if target_num % 2 ==0:
        s_num2.append(target_num)
print(f'입력받은 숫자는 {s_num1}입니다.')
print(f'입력받은 숫자 중 짝는 {s_num2}입니다.')
'''
딕셔너리 기반 연락처 관리

사용자로부터 3 명의 이름과 전화번호를 입력받아 딕셔너리에 저장하고 입력한 정보 추출 프로그램 작성

실행 예
1 번째 사람의 이름을 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름을 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번째 사람의 이름을 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 {'김일':'010-1234-5678','김이':'010-2345-6789','김삼':'010-3456-7890'}입니다.
'''
call_book = {}

call_call = 3
for i in range(3):
    call_member = input(f'{i+1} 번째 사람의 이름을 입력하세요 >>> ')
    call_num = input(f'{i+1} 번째 사람의 연락처를 입력하세요 >>> ')
    call_book[call_member] = call_num
print()
print(f'입력 받은 연락처는 {call_book}입니다.')
'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 numbers1을 선언하고 그 안에 입력받은 횟수만큼 숫자를 추가

함수 정의 : add_numbers
매개변수 : 정수 n

함수 호출 
add_numbers1(last_num)  # call2() 유형
print(add_numbers2(last_num) # call4() 유형

실행 예
숫자 몇까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
'''
numbers1 = []
numbers2 = []
numbers3 = []
last_num = int(input('숫자 몇까지 입력하시겠습니까? >>> '))
# 함수 정의 영역 # 1
def add_numbers1(n):
    for i in range(n):
        numbers1.append(i+1)
    print(numbers1)

# 함수 호출 영역 # 1
add_numbers1(last_num)

# 함수 정의 영역 # 2
def add_numbers2(n):
    pass
    for i in range(n):
        numbers2.append(i+1)
    return numbers2

# 함수 호출 영역 # 2
print(add_numbers2(last_num))

hello = ['안','녕','하','세','요']
def add_numbers3(n, temp_list):
    pass
    for i in range(n):
        numbers3.append(i+1)
    numbers3.extend(temp_list)
    print(numbers3)

add_numbers3(last_num, hello)
'''
짝수와 홀수의 개수 세기
list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성

함수 정의
함수 이름 : count_even_odd
매개변수 : list_numbers(요소는 모두 정수)

함수 호출
count_even_odd([1,2,3,4,5,6,7,8,9,10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
'''
odd = []
even = []
def count_even_odd(list_numbers):
    for i in range(len(list_numbers)):
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    print(f'짝수의 개수 : {len(odd)}개')
    print(f'홀수의 개수 : {len(even)}개')
count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])