'''
클래스 정의 형식 :

class 클래스명(파스칼케이스로):
    본문

객체 생성 형식 :
객체 이름 = 클래스명()
'''

# 클래스 정의 형식 예시
class WaffleMachine:
    pass

# 객체 생성 예시
waffle = WaffleMachine()
print(waffle)   # 결과값 : <__main__.WaffleMachine object at 0x000001C815C296A0>

'''
클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 보유
    객체를 생성하기 위해서는 객체가 지녀야 할 값과 기능 필요
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 속성은 두 가지로 구분
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
        (Java에서는 static 변수)
        2) 인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
    
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드
    가 있는데 Java에서 정적 메서드 분류가 클래스 메서드에 해당되고 정적 메서드는 또 따로 있다고 볼 수 있고 Java의 정적 메서드가 파이썬 클래스의 정적 메서드라고 볼 수 있음
    
    그리고 Java에서 this를 사용했는데(아직 생성되지 않은 객체명을 도입 할 수 없어서 사용하는 키워드 python은 self 사용
    
    self 키워드
    인스턴스 변수에서 각각의 객체를 의미하기 위해 self 키워드 사용
    인스턴스 메서드에서의 첫 매개변수로 항상 self 추가
'''
# 클래스 정의
class Person:
    # 메서드 정의(함수가 클래스 내에 존재하기에)
    def set_info(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'연락처 : {self.tel}')
        print(f'주소 : {self.address}')

    def show_info2(self):
        return f'제 이름은 {self.name}이고, {self.age}살입니다.\n연락처는 {self.tel}이며, {self.address}에 살고 있습니다.'
# 객체 생성
person01 = Person()
# Person 클래스의 메서드 호출
person01.set_info('김일',20,'010-1234-5678','서울특별시 마포구')
person01.show_info()

# person02 객체를 생성하고 person2.set_info()를 활용해 이름 나이 연락처 주소를 입력하고
# display_info2()(call3()으로 작성)를 정의해 다음 실행예 완성
# 실행 예
# 제 이름은 ____이고, __살입니다.
# 연락처는 ______며, _____에 살고 있습니다.
# 코드 실행
# print(person02.show_info())
person02 = Person()
person02.set_info('서문성',22,'010-3997-7652','부산광역시 금정구')
print(person02.show_info2())