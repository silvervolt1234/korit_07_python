print("Hello Python")

# 주석(comment) - 한 줄 주석 / 파이썬 인터프리터가 코드로 인식 X

# 사후 주석 -> ctrl + /

'''
다중 주석 처리
'''

print(1)    # 숫자 자료형
print('1')  # 문자열 자료형

print(1+2)      # 결과값 : 3
print('1'+'2')  # 결과값 : 12

print(type('1'))    # 결과값 : <class 'str'>
print(type(1))      # 결과값 : <class 'int'>
print(type(1.1))    # 결과값 : <class 'float'>

'''
print() : 콘솔에 출력하는 함수
type() : 소괄호 내에 있는 데이터(argument)가 어떤 자료형인지 알려주는 명령어
    - JS에서는 typeof가 하수가 아닌 연산자
'''
print('python 수업을 시작했습니다')
print('''
다중 작성시 \'\'\'\'\'\'로도 작성 가능.
Java에서는 줄 넘어갈때마다 + 연결 필요했지만 파이썬은 무관
''')

'''
이상에서 알 수 있는거는 print()가 System.out.println()처럼 자동 개행 가능

변수(Variable) : 데이터를 저장하는 바구니
'''
# 변수 선언 및 초기화
## 변수명 = 데이터
name = '김일'
print(name)
age = 20
print('안녕하세요 제 이름은 ' + name + '입니다. 나이는 ' + str(age) + '살입니다')

'''
python에서 Java나 JS처럼 맨 처음이 str이면 뒤의 int/float를 알아서 바꾸는 일 없음

그떄 사용하는게 형변환(conversion) 함수로 

str() : 다른 데이터를 문자열 자료형으로 바꾸는 함수
int() : 문자열/실수 자료형을 정수형으로 바꾸는 함수 / Java : (int)"1.3";
float() : 실수 자료형으로 바꾸는 함수

하지만 f-string으로 사용 빈도 낮음
'''
print(f'안녕하세요 제 이름은 {name}이고, 나이는 {age}살입니다.')
'''
console.log('안녕하세요, 제 이름은 ${name}이고, 나이는 ${age}살입니다.'); 의 파이썬버전

Java에서의 Scanner 같은 기능을 하는 함수 : input()
'''
name2 = input('이름을 입력하세요 >>> ')
print(name2)