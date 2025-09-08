'''
Java의 사례처럼 속성값을 대입하지 않은 객체를 생성한 후 속성값을 집어넣기

매개변수 생성자를 정의하면 객체 생성시 속성값을 넣을 수 있음
'''

# 클래스 정의
class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고 색깔은 {self.color}입니다.')

# 객체 생성(빈 객체 -> 속성값 대입 -> 속성값 출력))
satang = Candy()
satang.set_info('구형', '갈색')
satang.show_info()
'''
속성값에 대한 제한이 있지 않으면 빈 객체를 생성하고 거기에 값 대입이 비효율적이니 생성자를 동비

Java / JS 등에서는 생성자 명은 클래스명과 동일하거나 constructor이지만 python은 다른 형태의 생성자 사용
'''
class Candy2:
    # 생성자 정의
    def __init__(self, shape, color):   # __init__ : 생성자
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고 색깔은 {self.color}입니다.')

# 객체 생성방식에서 차이 존재
satang2 = Candy2('정육면체', '흰색')
satang2.show_info()

class Sample:
    # 생성자 정의
    def __init__(self):
        print('인스턴스가 생성되었습니다.')
    # 소멸자 정의
    def __del__(self):
        print('인스턴스가 소멸되었습니다.')

# 객체 생성
sample = Sample()
print()
# 객체 소멸자 호출 방법
del sample      # del 객체명
print('객체 지운 후의 코드라인')
'''
소멸자가 필요한 이유 -> 객체가 생성되면 메모리 공간을 차지해서 객체가 호출될때 마다 소환되는데

하지만 특정 객체가 일정 코드라인 이후로 전혀 사용되지 않을 때에도 여전히 메모리를 차지하기 때문에
소멸자를 통해서 강제로 객체를 삭제하면 메모리 관리에 용이

기본 예제

생성자를 통해 용량을 가진 usb 인스턴스를 만드는 프로그램 작성

지시 사항
1. 클래스 USB를 정의
2. 생성자를 정의하여 매개변수로 capacity를 받기
3. get_info() 메서드 정의

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
USB 객체가 생성되었습니다.
64GB USB
'''
class USB:
    def __init__(self, capacity):
        print('USB 정보가 생성되었습니다.')
        self.capacity = capacity
    def get_info(self):
        print(f'{self.capacity}GB')
usb = USB(64)
usb.get_info()
'''
응용 예제

1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스 생성

지시 사항

1. 다음 방법으로 man, woman 인스턴스 생성
man = Person('james')
woman = Person('emily')
2. man과 woman 인스턴스가 생성되면 다음과 같은 메세지 출력
james is born.
emily is born.
3. 다음 방식으로 man 인스턴스 삭제
del man
4. 인스턴스 삭제시 다음과 같은 메세지를 출력하게 작성
james is dead.
'''
class Person:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} is born.')
    def __del__(self):
        print(f'{self.name} is dead.')

man = Person('james')
woman = Person('emily')

del man
'''
james is born.
emily is born.
james is dead.
emily is dead.
라는 결과값의 이유는 모든 코드 블럭이 다 읽어지면 메모리에 할당된 객체는 자동 소멸
그래서 강제 emily is dead. 출력을 막으려면
'''
# input('소멸자 호출을 막는 중입니다.')

'''
python판 getter / setter

setter는 call2() -> 매개변수 o / 리턴 x
getter는 call3() -> 매개변수 o / 리턴 x
'''
class Student:
    # setter들 정의
    def set_name(self, name):
        self.name = name
    # getter 예시
    def get_name(self):
        return self.name

'''
지시 사항 age / address / score 속성을 setter로 추가
이상의 속성에 맞는 getter도 추가

student1 객체를 생성하고
김일, 20, 4.5를 각각 이름 / 나이 / 점수에 대입

getter를 활용해
김일 학생의 나이는 20살로 파이썬 과목의 점수는 4.5점입니다 출력

Java를 기준으로 보면 setter 내부에 비즈니스 로직이 들어갈수 있는데
set_age()의 경우 내부에 로직으로 0살 미만 200살 초과는 입력 불가능하게 하기
set_score()도 0.0 미만과 4.5 초과는 입력 불가능하게 비즈니스 로직 작성
'''
class Student:
    # setter 예시
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        # 0 미만 200 초과 입력 불가능
        if age < 0 or age > 200:
            print('불가능한 나이 입력입니다')
            return  # 메서드에 return하고 비우면 메서드 종료
        self.age = age


    def set_address(self, address):
        self.address = address

    def set_score(self, score):
        if score < 0 or score > 4.5:
            print('불가능한 점수 입력입니다')
            return
        self.score = score


    # getter 예시
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_score(self):
        return self.score

# 객체 생성
student1 = Student()
student1.set_name('김일')
student1.set_age(20)
student1.set_score(4.5)

print(f'{student1.get_name()} 학생의 나이는 {student1.get_age()} 살로, 파이썬 과목의 점수는 {student1.get_score()}점입니다.')