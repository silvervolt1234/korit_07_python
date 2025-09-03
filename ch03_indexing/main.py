str_example = 'hello, python!'
print(str_example[0])
print(str_example[1])
print(str_example[2])
print(str_example[3])
print(str_example[4])
print(str_example[5])
print(str_example[6])
print(str_example[7])

for alphabet in str_example:        # enhanced-for 형태
    print(alphabet, end = '')

print(str_example[-1])
print(str_example[-2])
print(str_example[-3])
print(str_example[-4])
print(str_example[-5])
print(str_example[-6])
print(str_example[-7])

'''
마이너스 인덱스 : 문자열의 뒤에서 부여하는 번호. 맨 마지막 데이터의 인덱스 넘버는 -1

문자열 슬라이싱(slicing): 문자열의 인덱스를 활용해 한 문자 이상으로 구성된 문자을 추출할 때 사용하는 방법. 추출하고자 하는 단어나 문자으이 시작 인덱스와 종료 인덱스로 그 사이 문자 추출 가능

형식:
a[시작인덱스 : 종료인덱스 : 증감값]
시작인덱스 : 생략시 처음부터 추출
종료인덱스 : 생략시 끝까지 추출
증감값 : 생략시 1씩 증가(인덱스 넘버 0부터)
'''
print(str_example[:-3:])     # 0번부터 순서대로 3번 미만 인덱스까지 출력

'''
기본 예제
네 자리 숫자를 입력받아 그 숫자의 마지막 숫자를 출력

네 자리 숫자를 입력하세요 >>> 0205
맨 마지막 숫자는 5입니다.
맨 마지막 숫자는 5이며, 홀수입니다. -> 조건문 사용
'''

num = input('네 자리 숫자를 입력하세요 >>> ')
print(num[-1])

nums = int(num)
if nums % 2 == 0:
    print(f'맨 마지막 숫자는 {num}이며, 짝수입니다.')
else:
    print(f'맨 마지막 숫자는 {num}이며, 홀수입니다.')