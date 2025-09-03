'''
for 반복문 :
원래 python의 default for문의 경우 enhanced for가 기본이지만 Java / JS때 일반 반복문을 기준으로 학습해서 동일 방식 학습 실시

중요점은 rang() 함수
1
2
3
...
10
출력하는 for문 작성
'''
for i in range(10):
    print(i+1)
'''
이상에서 중요한것은 마찬가지로 i가 0부터 시작한다는 점
이름 Java / JS로 풀면 
for (int i = 0; i < 10; i++) {
    System.out.print(i+1);
}
형태

range() : 몇 번 반복되는지 지정하는 함수 -> for문과 연계되서 사용

range() 함수의 응용 :
    range((시작값),(종료값),(증감값))
    
시작값 : 생략 가능, 생략시 0부터 시작
종료값 : 명시하지 않으면 끝까지 진행
증감값 : 생략 가능, 생략시 1씩 증가

for 반복문
형식 
for i(아무거나) in range(시작값, 종료값, 증감값):
    반복실행문
'''
for i in range(1, 11, 1):   # 종료값은 미만으로 적용
    print(i)
'''
전체 합쳐 생각하면 range() 내에 있는 부분이
Java 상에서 for()의 () 내에 있는 부분을 지정
for (int i = 0; i < 10; i++) {
    System.out.print(i+1);
'''
str_example = '안녕하세요'
for i in str_example:
    print(i)
'''
range()가 필수는 아니고 default 형태는

형식
for 변수명 in iterable(반복 가능 객체):
반복 실행문

range() 함수를 쓸 필요 없이 반복 가능 객체(list / tuple / string / set)의 처음부터 끝까지 돌아간다. enhanced - for문과 유사
'''
num_list =[1,2,3,4,5]
for i in num_list:
    print(i, end=' ')     # println이 아니라 한줄에 작성
print()
print(6)
# print는 자동 개행이기에 마무리를 사용자화 하려면 end = 키워드를 사용