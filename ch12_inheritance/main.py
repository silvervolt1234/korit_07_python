'''
상속

형식: 
class 슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스):
    본문
'''
class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} 이(가) {food}을(를) 먹습니다')

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    
    def study(self):
        print(f'{self.name}은(는) {self.school}에서 공부를 합니다')

    def eat(self, food):
        print(f'{self.school}에서', end=' ')
        super().eat(food)

# 객체 생성
potter = Student('해리포터','호그와트')
potter.eat('감자')
potter.study()
'''
1. 서브 클래스의 __init__()
    서브 클래스는 슈퍼 클래스가 없으면 존재할수 없고 생성자를 구현할때는
    반드시 슈퍼 클래스의 생성자를 먼저 호출 하는 코드를 작성
    
    super(). 에서 super -> 슈퍼 클래스를 의미. 이상의 코드에서 Student의 생성자를 호출하려면
    super().__init__(name)에 의해 슈퍼클래스인 Person의 생성자가 먼저 호출시 슈퍼 클래스의 객체 생성
    이후 슈퍼 클래스에서 생성된 인스턴스 변수인 name이 서브 클래스로 전달되고 이후 서브 클래스에서
    school 인스턴스 변수를 선언 및 초기화해 저장하며 서브 클래스의 인스턴스 생성
    
    생성자 호출시 객체가 생성되었다고 볼 수 있어서 부모 클래스 인스턴스와 자식 클래스의 인스턴스가 존재한다고 간주
    -> 별개의 객체인지는 슈뢰딩거
    
2. 서브 클래스의 인스턴스 자료형
    슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
    하지만 서브 클래스의 인스턴스는 서브 클래스의 인스턴스면서 동시에 슈퍼 클래스의 인스턴스
    Student 클래스의 객체는 Student의 인스턴스면서 Person의 인스턴스
    
    Java를 기준으로 instanceof 연산자 역할을 하는 함수가 python에도 있는데 -> isinstance() : 전부 소문저
    
    형식 :
        isinstance(객체명, 클래스명)   ->  boolean
'''
print(isinstance(potter, Person))       # 결과값 : True
print(isinstance(potter, Student))      # 결과값 : True
'''
3. 다음 지시 사항을 읽고 Hybrid 클래스 구현

지시 사항
1. 다음과 같은 슈퍼 클래스 Car를 가지는 Hybrid 클래스 구현
2. 서브 클래스 Hybrid는 다음과 같은 특징
    1) 최대 배터리 충전량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재. 최대 충전량은 초과 불가능하고 0보다 작은 값으로 충전 불가
    3) 현재 주유량과 충전량을 몯 확인 가능한 hybird_info() 메서드 존재
3. 다음과 같은 방식으로 전체 동작 확인 가능
car = Hybrid(oil = 0, amount = 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

하이브리드 차량이 생산되었습니다
기름을 50 주유했습니다
전기를 30 충전했습니다
현재 주유 상태 : 50
현재 충전 상태 : 30
'''
class Car:
    max_oil = 50                        # 클래스 변수
    def __init__(self, oil):    # 생성자 정의
        self.oil = oil                  # 속성

    def add_oil(self, oil):             # 메서드 # 1
        if oil <= 0:                    # 매개변수 oil이 0 이하면
            return                      # 메서드 종료
        self.oil += oil                 # 이상의 조건문이 실행 안되면 속성에다 oil만큼 추가
        if self.oil > Car.max_oil:      # self.oil의 현재 값이 50 초과면
            self.oil = Car.max_oil      # 최대치 설정값으로 고정

    def car_info(self):
        print(f'현재 주유 상태 : {self.oil}')

class Hybrid(Car):
    max_amount = 30                             # 부모 클래스 변수 접근 가능하니 추가 클래스 변수를 정의 및 초기화
    
    # 생성자 정의
    def __init__(self, oil, amount):
        super().__init__(oil)
        self.amount = amount
        print('하이브리드 차량이 생산되었습니다')
    
    # 부모 클래스의 메서드를 오버라이드
    def add_oil(self, oil):
        super().add_oil(oil)
        print(f'기름을 {self.oil}만큼 주유했습니다')
    
    # 자식 클래스의 고유 메서드
    def charge(self, amount):
        if amount <= 0:
            return
        self.amount += amount
        if self.amount > Hybrid.max_amount:
            self.amount = Hybrid.max_amount
        print(f'전기를 {self.amount}만큼 충전했습니다')

    def hybrid_info(self):
        # 오버라이드 없이 부모 메서드 호출
        super().car_info()
        print(f'현재 충전 상태 : {self.amount}')


car = Hybrid(oil=0, amount=0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()
'''
지시 사항
1. 슈퍼 클래스 Shape를 정의하시오
    - 생성자에 name을 인스턴스 변수로 설정
    - draw() 메서드를 정의해 self.name을 출력(call1() 유형)
2. Shape 클래스를 상속받는 서브 클래스 Circle을 정의
    - Circle은 radius(반지름) 속성을 추가로 가진다
    - 생성자에서 radius 추가
    - area() 메서드를 정의해 원의 넓이를 계산하고 return
        (넓이 = 3.14 * radius * radius)
3. Shape 클래스를 상속 받는 서브 클래스 Rectangle을 정의
    - Rectangle은 width(너비) / height(높이) 속성을 추가로 가진다
    - 생성자에서 width / height를 초기화
    - area() 메서드를 정의해 사각형의 넓이를 계산하고 return
        (넓이 = 너비 * 높이)
4. Circle과 Rectangle의 draw() 메서드를 오버라이딩해 각가의 넓이 출력

circle = Circle('원', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5인 원1이 생성되었습니다
이름이 원1인 원의 넓이는 78.5 입니다
원의 넓이  : 78.5
너비가 10, 높이가 8인 직사각형1이 생성되었습니다
이름이 직사각형1인 직사각형의 넓이는 80 입니다
직사각형의 넓이 : 80
'''
class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f'{self.name}이 생성되었습니다')

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def draw(self):
        print(f'반지름이 {self.radius}인', end=" ")
        super().draw()

    def area(self):
        if self.radius > 0:
            result =  self.radius ** 2 * 3.14
            print(f'이름이 {self.name}인 원의 넓이는 {result}입니다.')
            return result

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def draw(self):
        print(f'너비가 {self.width}, 높이가 {self.height}인', end=" ")
        super().draw()

    def area(self):
        if self.width > 0 and self.height > 0:
            result =  self.width * self.height
            print(f'이름이 {self.name}인 원의 넓이는 {result}입니다.')
            return result

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')