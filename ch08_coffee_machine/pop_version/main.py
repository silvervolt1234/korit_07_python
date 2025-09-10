MENU = {
    '에스프레소' : {
        '재료' : {
            '물' : 50,
            '커피' : 18,
        },
        '가격' : 1.5,
    },
    '라떼' : {
        '재료' : {
            '물' : 200,
            '우유' : 150,
            '커피' : 24,
        },
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료' : {
            '물' : 250,
            '우유' : 100,
            '커피' : 24,
        },
        '가격' : 3.0,
    },
}
profit = 0
resources = {
    '물' : 300,
    '우유' : 200,
    '커피' : 100,
}

# 함수 정의 영역
def is_resources_enough(order_ingredient) : # 특정 함수/메서드 결과값이 boolean이면 대게 이러한 조건/반복문으로 작성(함수 프로그래밍 형식)
    """
    DocString : 함수 / 클래스 / 메서드가 어떤 작동을 하는지 설명하는 기능
    주문받은 음료를 resources에서 재료 차감 후 음료를 만들 수 있으면 True, 아니면 False
    :param : order_ingredient
    :return : True / False
    """
    for i in order_ingredient :         # order_ingredient의 자료형:
        if order_ingredient[i] >= resources[i]:
            print(f'죄송합니다. {i}가 부족합니다.')
            return False
    return True

def process_coins():
    """동전을 입력받아 전체 금액을 반환하는 함수 call3() 유형"""
    # 쿼터, 다임, 니켈, 페니 네 종류의 동전
    '''
    쿼터 = 0.25 달러    quarter
    다임 = 0.1 달러     dime
    니켈 = 0.05 달러    nickel
    페니 = 0.01 달러    penny
    '''
    sum = 0
    sum += float(input('쿼터 개수 >>> '))*0.25
    sum += float(input('다임 개수 >>> '))*0.1
    sum += float(input('니켈 개수 >>> '))*0.05
    sum += float(input('페니 개수 >>> '))*0.01
    return sum
#todo - 6: 해당 총합을 가지고 총합이 선택한 음료 가격보다 높으면 다음 단계로
def is_transaction_successful(money_received, drink_cost):
    """process_coins()의 결과값과 음료 가격을 매개변수로 받은 동전의 총합이 음료 가격보다 높으면 True / 아니면 False 반환. 
    True라면 profit에 음료 가격만큼 추가하고 False는 받은 동전들을 반환하는 안내문 출력"""
    change = money_received - drink_cost
    if change >= 0:
        # 음료 제조 과정 및 profit 추가
        global profit   # 전역 변수인 profit을 함수 내부에서 사용하기 위한 키워드
        profit += drink_cost    # 함수 호출을 통한 전역 변수의 값 변화는 권장 x
        print(f'잔돈 ${change}을(를) 반환합니다')
        return True
    else:
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다.')
        return False    # 실행 x

def make_coffee(drink_name, order_ingredient):
    """
    resources에 있는 재료에서 메뉴['음료명']['재료']들을 차감
        -> 차감은 is_resources_enough()이 True였기에 무조건 0 이상
    :param drink_name:
    :param order_ingredient:
    :return: none -> call2() 유형으로 작성
    """
    for i in order_ingredient:            # resources가 아닌 order_ingrideent를 반복 돌리는 이유는 에스프레소에서 오류 발생 때문
        resources[i] -= order_ingredient[i]
    print(f'{choice}이(가) 나왔습니다. 맛있게 드세요')

#todo - 1: 커피 머신이 반복적으로 돌아가나 off 입력시 종료

# 관련 변수 선언 및 초기화
is_on = True
while is_on:
    # 반복문 내부에서 입력받아야 하기에 선언 및 초기화
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ')
    #todo -2 : choice 변수에 들어간 데이터가 off면 반복문 종료
    if choice == 'off':
        is_on = False
        print('자판기 종료')
    #todo -3 : 사용자가 프롬프트에 report를 입력시 현재 자원값 보고서 생성
    elif choice == 'report':
        print(f'물 : {resources['물']}ml')
        print(f'우유 : {resources['우유']}ml')
        print(f'커피 : {resources['커피']}ml')
        print(f'수익 : {profit}$')
    #todo -4 : choice == 에스프레소 / 라떼 / 카푸치노 중 하나일 때 계산식
    elif choice in ('에스프레소', '라떼', '카푸치노'):
        # 자판기에서 정확한 음료 이름 입력시 처리 과정
        # 1. 자원이 충분한지 확인
        # 2. T라면 돈을 입력 받게 -> 동전을 입력해 합연산 후 음료의 가격 이상인지 확인해 T / F 출력
        # 3. T면 음료를 반환해야하니 resources의 수량을 감소하고 profit에는 음료 가격만큼 증가. 그리고 동전 받은것에서 음료 가격 빼고 반환
        if is_resources_enough(MENU[choice]['재료']):
            # 이상의 조건식이 True면 동전 처리
            money_received = process_coins()
            # money_received는 전역 변수고 process_coins()의 결과값을 변수에 저장
            if is_transaction_successful(money_received=money_received, drink_cost=MENU[choice]['가격']):
                # 음료 제조 과정을 작성
                # 재료를 실질적으로 차감하고 음료를 만들어 사용자에게 제공
                # 재료 차감 파트를 is_resources_enough() 함수를 참조해 작성
                # 해당 작성 결과를 함수화하게
                # resources['물'] -= MENU[choice]['재료']['물']
                # resources['우유'] -= MENU[choice]['재료']['우유']
                # resources['커피'] -= MENU[choice]['재료']['커피']
                # print(f'{choice}이(가) 나왔습니다. 맛있게 드세요')
                make_coffee(drink_name=choice, order_ingredient=MENU[choice]['재료'])

    #todo -5 : choice가 이상의 조건이 아니면 잘못 입력하셨습니다. 다시 입력하세요 를 출력
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요')
