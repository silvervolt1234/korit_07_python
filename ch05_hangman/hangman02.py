import random

word_list = ['apple', 'banana', 'cherry']
chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 1 : 비어있는 list인 display 생성
display = []
# display 예제
# display.append('김')
# print(display)
# display.append(1)
# print(display)

#todo - 2 : 이상의 코드라인을 참조해 chosen_word의 각 문자 개수마다 '_'를 추가 chosen_word == 'apple'이라면 display = ['_', '_', '_', '_', '_']
for i in chosen_word:
    display.append('_')      # 반복실행문에서 변수 i가 쓰이지 않아서 반복횟수가 chosen_word만큼. 그렇기에 i 같은 변수보다는 반복횟수만 통제
print(display)

#todo - 3 : chosen_word의 각 문자들을 반복. 그 위치의 문자가 guess와 일치하면 해당 위치에서 문자 공개. 사용자가 p를 입력하고 chosen_word == 'apple'면 display = ['_', 'p', 'p', '_', '_']
guess = input('단어 입력 : ').lower()
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess      # guess라는 데이터를 display인 인덱스 넘버 i 위치에 재대입
print(display)