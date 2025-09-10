from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# python 객체 만드는 방식
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# coffee_maker / menu / money_machine을 건드리지 않고 main으로만 coffe machine 작동
is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까 ({menu.get_items()}) >>> ')

    if choice == 'off':
        is_on = False
        print('자판기가 종료되었습니다')

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    
    else:
        # if choice not in ['espresso', ' cappuccino', 'latte']:      # 메뉴 추가시마다 수정해야함
        #     continue
        drink = menu.find_drink(choice)
        if drink == None:       # choice에 오타가 있을 경우 None이 반환되서 고전적 예외 처리
            continue            # continue가 실행되면 이 이하의 코드라인은 실행되지 않고
                                # while 반복문의 가장 앞부분으로 돌아가 다음 반복 실행
        # 음료 이름을 입력받은 시점부터 프로세스를 생각해 코드 작성. 고려사항흔 절차지향 방식과 현재 참조해야하는 모듈들의 매겨변수 차이와 메서드 작동 원리
        # pop version 함수 작동 순서대로
        # is_resources_enough(order_ingredient) / is_resource_sufficient(drink)
        if coffee_maker.is_resource_sufficient(drink):
            # 조건문을 이용해 process_coins()와 make_payemnt를 활용해 
            # 모든것이 true면 작동중입니다 출력
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
