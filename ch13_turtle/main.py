from turtle import Turtle, Screen
from random import Random
# turtle 모듈에서 Turtle, Screen 클래스를 import.

t = Turtle()        # 터틀 객체를 생성했고 객체명 t
screen = Screen()   # 스크린 객체 생성
# 이상의 경우만 작성했을 때 모니터가 점멸 것을 확인할 수 있는데
# 코드가 다 돌아가면 프로그램이 종료되기 때문에, 창이 켜졌다가 꺼지는 것

t.shape('turtle')           # Turtle의 메서드를 호출했는데 argument가 str
t.color('white')
screen.bgcolor('black')
t.speed(0)

# 랜덤 객체 생성
random = Random()
colors = [
    'dark red',
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
    'light yellow'
]

# t.forward(100.3)
# t.penup()
# t.forward(100.3)
# t.forward(100.3)
# t.pendown()
# t.forward(30)

# 점선 그리는 반복문
# for _ in range(10):
#     t.forward(15)
#     t.penup()
#     t.forward(15)
#     t.pendown()

# .left(각도)
# t.left(90)

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# for _ in range(3):
#     t.forward(100)
#     t.left(120)
#
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
#
# for _ in range(5):
#     t.forward(100)
#     t.left(72)
#
# for _ in range(6):
#     t.forward(100)
#     t.left(60)

# 그럼 오각형 / 육각형도 그리기.


# 이상을 일반화 시키기 위해서 알 수 있는 것은
'''
삼각형일 때 120
사각형일 때 90
오각형일 때 72
육각형일 때 60

십각형일 때 36
'''
# n = int(input('몇각형을 만드시겠습니까? >>> '))
# for _ in range(n):
#     t.forward(100)
#     t.left(360/n)

# for i in range(3, 13):
#     for _ in range(i):
#         t.forward(100)
#         t.left(360 / i)
#     t.color(random.choice(colors))
#

# 도형을 그릴때마다 반복문을 쓰기는 무리가 있으니 함수를 정의
# def draw_shape(n):
#     for i in range(n):
#         t.forward(100)
#         t.left(360 / n)
#     t.color(random.choice(colors))
#
# def draw_dotted_line(n):
#     t.color(random.choice(colors))
#     for i in range(n):
#         t.left(360 / n)
#         for _ in range(15):
#             t.forward(5)
#             t.penup()
#             t.forward(5)
#             t.pendown()

# for i in range(3, 11):
#     draw_shape(i)

# for i in range(3, 11):
#     draw_dotted_line(i)
#
# t.forward(100)
# print(t.heading())
# t.left(90)
# t.forward(100)
# print(t.heading())
# t.left(30)
# t.forward(100)
# print(t.heading())
# t.right(30)
# t.forward(100)
# print(t.heading())
# t.setheading(30)
# t.forward(100)
# print(t.heading())

# t.heading()의 return 값은 flaot
# .setheading()의 parameter가 float / return None

# t.setheading(t.heading() + 100)

# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)
# t.color(random.choice(colors))
# t.circle(100)
# t.left(60)


# for i in range(36):
#     t.color(random.choice(colors))
#     t.circle(100)   # 원 그리기
#     # 거북의 머리를 미리 다른쪽으로 돌려서 다음 원이 겹치지 않는 함수
#     t.setheading(t.heading() + 10)

# for i in range(10):
#     t.color(random.choice(colors))
#     t.circle(100)   # 원 그리기
#     # 거북의 머리를 미리 다른쪽으로 돌려서 다음 원이 겹치지 않는 함수
#     t.setheading(t.heading() + 36)

# 함수화를 위한 일반식
# n = 6
# for i in range(n):
#     t.color(random.choice(colors))
#     t.circle(100)   # 원 그리기
#     # 거북의 머리를 미리 다른쪽으로 돌려서 다음 원이 겹치지 않는 함수
#     t.setheading(t.heading() + (360 / n))

# 함수화
def draw_spirograph(size_of_gap):
    for i in range(360 // size_of_gap):
        t.color(random.choice(colors))
        t.circle(100)  # 원 그리기
        t.setheading(t.heading() + (360 / size_of_gap))

draw_spirograph(30)
# 이상의 코드의 문제점은 
# 1. 매개변수인 size_of_gap은 n 번째 원과 n+1번째 원의 각도 차이를 나타내는건데 실제로는 반복 횟수를 통제
# 2. 360을 입력했을 때 제자리에서 원이 생성되는것이 아닌 360번을 그대로 반복

screen.exitonclick()