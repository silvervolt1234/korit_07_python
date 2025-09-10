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

logo = '''
░█▀▀░█▀█░█▀▀░█▀▀░█▀▀░█▀▀
░█░░░█░█░█▀▀░█▀▀░█▀▀░█▀▀
░▀▀▀░▀▀▀░▀░░░▀░░░▀▀▀░▀▀▀
'''

def is_resources_enough(order_ingredient):
    for i in order_ingredient :         # order_ingredient의 자료형:
        if order_ingredient[i] >= resources[i]:
            print(f'죄송합니다. {i}가 부족합니다.')
            return False
    return True

def process_coins():
    sum = 0
    sum += float(input('쿼터 개수 >>> '))*0.25
    sum += float(input('다임 개수 >>> '))*0.1
    sum += float(input('니켈 개수 >>> '))*0.05
    sum += float(input('페니 개수 >>> '))*0.01
    return sum

def is_transaction_successful(money_received, drink_cost):
    change = money_received - drink_cost
    if change >= 0:
        global profit   # 전역 변수인 profit을 함수 내부에서 사용하기 위한 키워드
        profit += drink_cost    # 함수 호출을 통한 전역 변수의 값 변화는 권장 x
        print(f'잔돈 ${change}을(를) 반환합니다')
        return True
    else:
        print(f'금액이 충분하지 않습니다. ${money_received}를 반환합니다.')
        return False

def make_coffee(drink_name, order_ingredient):
    for i in order_ingredient:            # resources가 아닌 order_ingrideent를 반복 돌리는 이유는 에스프레소에서 오류 발생 때문
        resources[i] -= order_ingredient[i]
    print(f'{choice}이(가) 나왔습니다. 맛있게 드세요')

is_on = True
while is_on:
    print(logo)
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ')
    if choice == 'off':
        is_on = False
        print('자판기 종료')
    elif choice == 'report':
        print(f'물 : {resources['물']}ml')
        print(f'우유 : {resources['우유']}ml')
        print(f'커피 : {resources['커피']}ml')
        print(f'수익 : {profit}$')
    elif choice in ('에스프레소', '라떼', '카푸치노'):
        drink = MENU[choice]
        if is_resources_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received=money_received, drink_cost=drink['가격']):
                make_coffee(drink_name=choice, order_ingredient=drink['재료'])
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요')