import random
'''
''.join(반복 가능 객체) method : '.' 앞에 있는 문자열을 기준으로
반복 가능 객체의 element들을 합쳐서 str로 합쳐주는 method
'''
# temp = ['배','고','프','다']
# feeling = ''.join(temp)
# print(temp)
# print(feeling)
# result=''
# for letter in temp:
#     result += letter
# print(result)
# feeling2 = '/'.join(temp)
# print(feeling2)
''' 
이상의 예시는 display를 재조합해 str로 바꿀 때 사용
'''
#todo -1 : 비어있는 list인 dispaly를 선언
display = []

#todo -2 : chosen_word의 문재개수만큼 '_'를 display에 추가
word_list = ['apple', 'banana', 'cherry']
chosen_word = random.choice(word_list)
print(chosen_word)
for i in chosen_word:
    display.append('_')
print(display)

#todo -3 : 사용자가 추측을 반복 가능하게 while 반복문을 작성. 사용자가 chosen_word의 모든 문자열을 맞추면, 즉 display에 '_'가 없을 때 반복문 정지. 반복문 종료 후 print('정답입니다') 출력
# while '_' in display:   # display에 element에 '_'가 있으면 반복 실행
while ''.join(display) != chosen_word:
    # '_'가 사라질때까지 반복해야하니
    guess = input('단어 입력 : ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)

#todo -4 : 정답을 보여줄 때 apple은 a p p l e로 출력되게 join 사용
print('정답입니다!')
print(' '.join(display))
print(' '.join(chosen_word))
