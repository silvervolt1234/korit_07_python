import random
# word_list 내부의 element를 하나 선택하기 위한 random 모듈 도입
'''
사용 예시
'''
# numbers = [1,2,3,4,5]
# chosen_number = random.choice(numbers)  # choice 라는 메서드의 argument로 list 도입
# print(chosen_number)

word_list = ['apple', 'banana', 'cherry']
#todo - 1 : word_list에서 단어 하나를 임의적으로 선택하도록 random 모듈을 사용하고 해당 단어를 chosen_word에 저장
chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 2 : 사용자에게 알파벳을 하나 추측해서 입력하라고 요청하고 이를 guess 변수에 저장. 그리고 대문자 방지를 위해 input() 뒤에 .lower 적용
guess = input('단어 입력 : ').lower()

#todo - 3 : guess에서 입력한 문자 하나가 chosen_word의 string 문자열 중 하나의 문자열과 일치하는지 반복문을 통해 확인하게 프로그램 작성. 맞으면 정답, 틀리면 오답으로 출력
'''
예를 들어 chosen_word가 apple이고
guess에 a를 입력하며 정답이라고 출력
b라고 입력하면 오답이라고 출력
'''
# 1. enhanced-for
for i in chosen_word:
    if i == guess:
        print('정답', end=' ')
    else:
        print('오답', end=' ')
print()

# 2. 일반 for
# len() 함수 : 반복 가능 객체의 길이을 int로 return
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        print('정답', end=' ')
    else:
        print('오답', end=' ')
print()