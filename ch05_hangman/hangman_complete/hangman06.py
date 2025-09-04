import random
import hangman_arts
import hangman_wordlist
# logo / stages와 같은 변수는 x
# 외부의 hangman_word_list에 있는 world_list를 참조해서 chosen_word 생성
print(hangman_arts.logo)
chosen_word = random.choice(hangman_wordlist.word_list)
print(chosen_word)

lives = 6
display = []
end_of_game = False

for i in chosen_word:
    display.append('_')
print(display)

while not end_of_game:
    print(hangman_arts.stages[lives])
    guess = input('단어 입력 : ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            print(display)
    if '_' not in display:
        print(hangman_arts.stages[lives])
        print(' '.join(display))
        print('게임 클리어')
        end_of_game = True
    if guess not in chosen_word:
        lives -= 1
        print(f'{lives} 번 남았습니다')
        print(display)
        if lives == 0:
            end_of_game = True
            print(hangman_arts.stages[lives])
            print('게임 오버')
            print(f'정답은 {chosen_word}입니다.')
