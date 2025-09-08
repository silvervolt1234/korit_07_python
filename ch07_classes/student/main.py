class Student:
    # 생성자 정의
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id
        # 성적 저장을 위한 빈 딕셔너리 -> 과목명 key, 점수 value
        self._grades = {}
    
    # python 버전의 getter에 해당
    @property
    def name(self):
        return self._name

    # python 버전의 setter 예시
    @name.setter
    def name(self, value):
        self._name = value
student1 = Student('김일', 2025001)
# getter의 호출 예시 객체명.속성명 -> 객체명. 메서드명()이 아닌것에 주목
print(f'학생 이름 : {student1.name}')

# setter의 호출 예시
student1.name = '김영'
print(f'변경된 학생 이름 : {student1.name}')

'''
Java를 기준으로만 python 코드를 생각하면 의문점이 발생하는데
1. _name이라는 속성이 있는데 객체명.name을 통해 김영 / 김일이라는 속성갑 출력
2. 객체명._name = '김영'이 아닌 객체명.name = '김영'으로 객체의 속성값을 직접 바꾼걸로 보인다는 점

이 발생

python에서는 _name / name이 서로 다른 개념이니 '_'는 파이썬 언어에서 내부적으로 동일한 속성

객체명.속성명에 ()가 없지만 메서드처럼 처리하기에 객체명.속성명은 getter로 처리하고 객체명.속성명=데이터 는 setter로 처리

이런 코드라인의 성립에 중요점이 `@property`와 `@속성명.setter`라는 데코레이터(decorator)

기본적으로 자동생성되니 일일히 애너테이션 달고 _속성명 / 일반 속성명을 따질 필요 없음
'''