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

# 구매할 물품 여러 개 선택
cart = []  # 선택한 물품과 개수를 저장할 리스트

while True:
    choice = input("구매할 물품 번호를 입력하세요 (종료: 0): ")
    if choice == "0":
        break

    choice = int(choice) - 1
    if choice < 0 or choice >= len(items):
        print("잘못된 번호입니다.")
        continue

    qty = int(input(f"{items[choice]['name']} 몇 개 구매하시겠습니까? "))
    cart.append({"item": items[choice], "qty": qty})

# 총액 계산
total_price = sum([entry["item"]["price"] * entry["qty"] for entry in cart])

if money >= total_price:
    change = money - total_price
    print("\n=== 구매 내역 ===")
    for entry in cart:
        print(f"{entry['item']['name']} {entry['qty']}개 - {entry['item']['price'] * entry['qty']}원")
    print(f"총액: {total_price}원")
    print(f"잔돈: {change}원")
else:
    print("돈이 부족합니다. 구매할 수 없습니다.")