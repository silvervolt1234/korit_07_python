# 자판기 물품 (이름, 가격)
items = [
    {"name": "콜라", "price": 1200},
    {"name": "사이다", "price": 1100},
    {"name": "커피", "price": 900},
    {"name": "생수", "price": 700},
    {"name": "주스", "price": 1500}
]

# 물품 목록 출력
print("=== 자판기 메뉴 ===")
for i in range(len(items)):
    print(f"{i+1}. {items[i]['name']} - {items[i]['price']}원")

# 돈 입력
money = int(input("돈을 넣어주세요: "))

# 물품 선택
choice = int(input("구매할 물품 번호를 입력하세요: ")) - 1

# 유효성 검사
if choice < 0 or choice >= len(items):
    print("잘못된 번호를 입력했습니다.")
else:
    qty = int(input("구매할 개수를 입력하세요: "))
    total_price = items[choice]["price"] * qty

    if money >= total_price:
        change = money - total_price
        print(f"{items[choice]['name']} {qty}개를 구매했습니다.")
        print(f"잔돈: {change}원")
    else:
        print("돈이 부족합니다. 구매할 수 없습니다.")