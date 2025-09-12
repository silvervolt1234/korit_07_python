from turtle import Turtle, Screen
# turtle 모듈에서 Turtle, Screen 클래스를 import

t = Turtle()        # 터틀 객체를 생성하고 객체명 t
screen = Screen()   # 스크린 객체 생성
# 이상의 경우만 작성했을 때 모니터가 점멸하는걸 확인하는데
# 코드가 다 돌아가면 프로그램이 종료하는데 이로 인해 켜졌다 꺼진다

t.shape('turtle')
t.color('white')
screen.bgcolor('black')
screen.exitonclick()

