'''
1. 클래스 변수 vs. 인스턴스 변수
    인스턴스 변수 : 인스턴스마다 서로 다른 값을 가지는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지는 변수(Java는 정적 변수)

    인스턴스 변수 :
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근 방식 - 인스턴스 접근(o)
                - 클래스 접근(x)

    클래스 변수 :
        목적 - 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                - 클래스 접근(o)
'''
# 클래스 변수 예시
class Korean:
    country = '한국'      # 클래스 변수 # 1
    # 인스턴스 변수는 생성자 내부에 있었는데(__init__)
    # 클래스 변수는 클래스 내부에 선언하고 초기화

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# 객체 생성
man1 = Korean('김일', 21, "서울특별시 종로구")
print(man1.name)        # 인스턴스 변수 참조
print(man1.age)
print(man1.address)

print(man1.country)     # 결과값 : 한국
print(Korean.country)   # 결과값 : 한국

'''
객체명.클래스 변수를 통해서 클래스 변수에 접근이 가능하나 클래스 내부의 코드를 들여다보기 전까지는 
country라는 변수가 인스턴스인지 클래스 변수인지 알 방법이 없다

그래서 클래스 변수를 확인할 떄는 객체명.클래스변수보다는 클래스명.클래스변수를 권장

2. 클래스 메서드 : 클래스 변수를 사용하는 메서드
'''
class Korean2:
    country = '대한민국'    # 클래스 변수의 선언 및 초기화
    
    # 클래스 메서드 정의 방법
    @classmethod                                    # @classmethod 데코레이터로 클래스 메서드로 인지
    def trip(cls, traveling_site):
        if cls.country == traveling_site:           # 그 결과 첫 매개변수가 self가 아닌 cls
            print(f'{traveling_site} 여행중입니다.')
        else:
            print('해외 여행입니다.')

Korean2.trip('대한민국')
Korean2.trip('미국')
man2 = Korean2()
man2.trip('일본')
# 클래스 변수와 마찬가지로 객체명.클래스메서드명()으로 호출이 가능하지만
# 마찬가지로 인스턴스 메서드인지 알 바가 아니기에 클래스메서드 호출시 클래스명.클래스메서드 권장

'''
특징 :
    1) 인스턴스 / 클래스로 호출 가능 -> 하지만 클래스로 호출하게 권장
    2) 생성된 인스턴스가 없어도 호출 가능(클래스로 호출 가능)
    3) @classmethod 데코레이터(decorator)를 표시하고 작성
    4) 매개변수 cls를 사용 -> self는 객체를 의미하고 cls는 클래스를 의미
    
3. 정적 메서드(static method)
    : 정적 메서드 또한 self를 사용하지 않음 -> 즉 인스턴스 변수에 접근해 사용하는것이 불가능
      self. 속성명을 사용해 인스턴스 변수의 값을 참조하는데 
      정적 메서드는 아예 첫 번째 매개변수가 고정이 아님 - 클래스 메서드와의 공통점 # 1
      인스턴스를 생성하지 않아도 사용 가능 - 클래스 메서드와의 공통점 # 2
      
    특징 :
        1) 인스턴스 / 클래스로 호출 가능 -> 클래스 메서드와의 공통점
        2) 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 공통점
        3) @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점 # 1
        4) 반드시 작성해야 할 매개변수(self / cls)가 없음 -> 클래스 메서드와의 차이점 # 2

이러한 이유로 정적 메서드는 self / cls 둘 다 사용하지 않아서 인스턴스 / 클래스 변수를 모두 사용하지 않는 메서드 정의에 적합
정적 메서드는 클래스에 소속되있지만 인스턴스에 영향 없음

즉 Java에서의 정적 메서드 = 파이썬의 클래스 메서드 + 정적 메서드
'''
class Korean3:
    country = '한국'  # 클래스 변수

    @staticmethod
    def slogan():
        print('Imagine Your Korea!')

    @staticmethod
    def slogan2(str_example):
        """"일반 매개변수"""
        print('Imagine Your Korea!' + str_example)

Korean3.slogan()
Korean3.slogan2(' 너무 춥다')
'''
기본 예제

가방을 만들때마다 현재 만들어진 가방이 몇개인지 계산 가능한 Bag 클래스 정의
'''
# 클래스 정의
class Bag:
    # 클래스 변수의 선언 및 초기화
    count = 0

    def __init__(self): # 생성자 호출 및 인스턴스 변수들 정의. 생성자 역시 인스턴스 변수
        Bag.count += 1  # 생성자 호출때마다(=객체 생성마다) 클래스 변수인 count 1 씩 증가
                        # cls.count가 아닌 클래스명.count에 주목
        print('가방 객체가 생성되었습니다')

    # 클래스 메서드 정의
    @classmethod
    def sell(cls):
        print('가방이 팔렸습니다')
        cls.count -= 1
        # 클래스 메서드가 클래스 변수에 접근한것이니 Bag.count가 아닌 cls

    @classmethod
    def remain_bags(cls):
        return cls.count

print(f'현재 가방 재고 : {Bag.count}')
print(f'현재 가방 재고 : {Bag.remain_bags()}')

# 객체 생성
bag1 = Bag()
print(f'현재 가방 재고 : {Bag.remain_bags()}')
bag2 = Bag()
bag3 = Bag()
print(f'현재 가방 재고 : {Bag.remain_bags()}')
bag1.sell()     # 실제 bag1 객체 삭제 x
print(f'현재 가방 재고 : {Bag.remain_bags()}')
Bag.sell()
print(f'현재 가방 재고 : {Bag.remain_bags()}')
'''
응용 예제
1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 작성

지시사항
1) 다음과 같은 방법으롷 man/woman 인스턴스 작성
man = Person('김일')
woman = Person('김이')

2) man과 woman 인스턴스가 생성되면 다음과 같은 메세지를 출력
김일이(가) 태어났습니다
김이이(가) 태어났습니다

3) 다음 코드를 통해 전체 인구수 조회
print(f'전체 인구수 : {Person.get_population()}')

4) 다음과 같은 명령어로 man 인스턴스 삭제

5) man 인스턴스 삭제시 다음과 같음 메세지 출력하게 소멸자 정의
RIP 김일
'''
class Person:
    # 클래스 변수의 선언 및 초기화
    population = 0
    
    @classmethod
    def get_population(cls):
        return f'전체 인구수 : {cls.population}'
    
    def __init__(self,name):
        self.name = name
        Person.population +=1    # 인스턴스 메서드를 통해 클래스 변수를 변화시킨거니 클래스명.클래스변수명
        print(f'{self.name}이(가) 태어났습니다.')

    def __del__(self):
        Person.population -= 1
        print(f'RIP {self.name}')

man = Person('김일')
woman = Person('김이')
print(f'전체 인구수 : {Person.get_population()}')
del man
print(f'전체 인구수 : {Person.get_population()}')
print('프로그램 종료')
'''
다음 지시 사항에 따라 가게의 매출을 구하는 Shop 클래스를 작성

지시 사항
1. Shop 클래스는 다음과 같은 변수를 보유
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 dictionary 요소를 가진 list
    
    menu_list = [{'떡볶이':3000},{'순대':4000},{'튀김':5000},{'김밥':2000}]

2. 매출이 생기면 다음과 같은 방식으로 판매량 작성
Shop.sales('떡볶이',1)    # 떡볶이을(를) 1개 판매
Shop.sales('김밥', 2)     # 김밥을(를) 2개 판매
Shop.sales('튀김', 5)     # 튀김을(를) 5개 판매

3. 모든 매출을 작성한 뒤 다음 방식으로 전체 매출액 확인
print(f'매출 : {Shop.get_total()}원')
'''
class Shop:
    total = 0
    menu_list = [{'떡볶이':3000},{'순대':4000},{'튀김':5000},{'김밥':2000}]

    @classmethod
    def sales(cls, item, count):
        for i in cls.menu_list:
            if item in i:
                price = i[item]
                cls.total += price*count
                return

    @classmethod
    def get_total(cls):
        return cls.total

Shop.sales('떡볶이',1)
Shop.sales('김밥', 2)
Shop.sales('튀김', 5)

print(f'매출 : {Shop.get_total()}원')