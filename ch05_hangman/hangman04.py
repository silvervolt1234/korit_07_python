import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
'''
이상의 코드라인을 보면 내부의 element가 복수의 라인으로 이루어진 str인 list라고 할 수 있다
'''
#todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화
lives = 6

#todo - 2 : hangman03을 참조해 while 반복문 바깥쪽 완성
display = []

word_list = ['apple', 'banana', 'cherry']
chosen_word = random.choice(word_list)
print(chosen_word)
for i in chosen_word:
    display.append('_')
print(display)

#todo -3 : while문 조건을 수정해 6번의 기회가 소진되면 반복문 종료
end_of_game = False
while not end_of_game:
    print(stages[lives])
    guess = input('단어 입력 : ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:     # 선택된 단어의 알파벳이 일치
            display[i] = guess
            print(display)
        # else:
        #     lives -= 1
        #     if lives == 0:
        #         print(stages[lives])
        #         print(display)
        #         print('모든 기회를 잃었습니다')
        #         end_of_game = True
        # 는 오류 발생. 반복문 내부에서 guess가 일치하는지 여부를 따져야 하기에
        # chosen_world가 apple이고 guess가 a라면 첫 반복은 display의 0번지가 a로 변환
        # 반복문 내부에 위치해서 1, 2, 3, 4번지에 대해서 a가 display 인덱스와 일치하는
        # element인지 확인하게 되고 p p l e가 a와 달라서 lives -= 1이 4번 적용되 행맨이 완성
    
    # 이러한 이유로 for 바깥에서 guess가 chosen_word에 속하지 않는지 확인하는 조건문을 별개로 작성
    if '_' not in display:
        print(stages[lives])
        print(' '.join(display))
        print('게임 클리어')
        end_of_game = True
    if guess not in chosen_word:
        lives -= 1
        print(f'{lives} 번 남았습니다')
        print(display)
        if lives == 0:
            end_of_game = True
            print(stages[lives])
            print('게임 오버')
            print(f'정답은 {chosen_word}입니다.')

#todo - 4 : lives의 변수와 stages 리스트의 관계를 파악해 guess를 입력할 때마다 올바른 stages의 element가 출력될 수 있도록 작성