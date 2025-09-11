'''
외부 패키지의 설치 # 1. setting을 통한 방법
setting-python interpreter를 통해 검색 후 설치

외부 패키지의 설치 # 2. 터미널을 이용한 방법
pip install 패키지명
'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

# PrettyTable의 객체 생성
table = PrettyTable()

table.field_names = ['도감번호', '포켓몬명', '타입']

# for i in range(len(pokemon_data)):
#     table.add_row(pokemon_data[i])

table.add_rows(pokemon_data)

print(table)