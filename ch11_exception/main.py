'''
1. 예외 처리의 필요성
    1) 예외(exception) : 개발자가 직접 처리가능한 문제
    2) 오류(error) : 개발자가 처리할 수 없는 문제
    3) 예외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결하는게 아니라 발생된 문제로 인해 프로그램이
        비정상적 종료를 막고 사용자에게 발생한 문제에 대해 정보 전달을 목적

2. 예외 처리
    1) 고전적 예외 처리
'''
a = int(input('나누는 수(제수)를 입력하세요 >>> '))
b = int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
if a == 0:
    print('0으로 나눌 수 없습니다')
else:
    result = b / a
    print(result)
'''
어떤 갑싱든 0으로는 나눌수 없기에 if a == 0으로 0을 나누기 자체를 시도할 수 없게 예외처리

여기서 생각 가능한건 
    1) 어떤 문제가 발생할 지 예상해야 대비 가능
    2) 어떤 문제가 발생할 지 예상해도 대비할 수 없는 경우 발생

3.예외 처리의 종류
+------+---------------------+--------------------------------------------+
| 순번  |     예외 클래스       |                    의미                    |
+------+---------------------+--------------------------------------------+
|  1   |    BaseException    |             최상위 예외 클래스                |
|  2   |      Exception      |        대부분 예외 클래스의 슈퍼 클래스         |
|  3   |   ArithmeticError   |           산술 연산에 문제가 있을 때           |
|  4   |    AttributeError   |            잘못된 속성을 참조할 때             |
|  5   |       EOFError      |     파일에서 더 이상 읽어들일 데이터가 없을 때    |
|  6   | ModuleNotFoundError |           import할 모듈이 없을 때             |
|  7   |  FileNotFoundError  |            존재하지 않는 파일일 때             |
|  8   |      IndexError     |          잘못된 인덱스를 사용할 때             |
|  9   |      NameError      |         잘못된 이름(변수)을 사용할 때           |
|  10  |     SyntaxError     |              문법이 틀렸을 때                 |
|  11  |      TypeError      |     계산하려는 데이터의 유형이 잘못되었을 때      |
|  12  |      ValueError     |      계산하려는 데이터의 값이 잘못되었을때        |
+------+---------------------+--------------------------------------------+
'''
from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ['순번', '예외 클래스', '의미']
table.add_row([1, 'BaseException', '최상위 예외 클래스'])
table.add_row([2, 'Exception', '대부분 예외 클래스의 슈퍼 클래스'])
table.add_row([3, 'ArithmeticError', '산술 연산에 문제가 있을 때'])
table.add_row([4, 'AttributeError', '잘못된 속성을 참조할 때'])
table.add_row([5, 'EOFError', '파일에서 더 이상 읽어들일 데이터가 없을 때'])
table.add_row([6, 'ModuleNotFoundError', 'import할 모듈이 없을 때'])
table.add_row([7, 'FileNotFoundError', '존재하지 않는 파일일 때'])
table.add_row([8, 'IndexError', '잘못된 인덱스를 사용할 때'])
table.add_row([9, 'NameError', '잘못된 이름(변수)을 사용할 때'])
table.add_row([10, 'SyntaxError', '문법이 틀렸을 때'])
table.add_row([11, 'TypeError', '계산하려는 데이터의 유형이 잘못되었을 때'])
table.add_row([12, 'ValueError', '계산하려는 데이터의 값이 잘못되었을때 '])

print(table)
'''
4. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except / finally
    형식 :
try : 
    코드 작성 영역
except :
    예외 발생 시 처리 영역
finally :
    언제나 실행되는 영역
'''
try :
    a = int(input('나누는 수(제수)를 입력하세요 >>> '))
    b = int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
    print(f'b / a = {b/a}')
except:
    print('예외가 발생했습니다')
'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램으로
try / except 문을 사용해 '예외가 발생했습니다'를 출력
'''
try :
    height = input('키를 입력하세요 >>> ')
    height = round(height)
    print(f'입력하신 키는 {height}cm로 처리됩니다')
except :
    print('에외가 발생했습니다')
'''
    1) 특정 예외만 처리하는 방식
        try / except 문을 사용하면 기본적으로 예외의 종류와 상관없이 모든 예와가 처리
        하지만 서로 다른 메세지를 출력할 수 있으면 개발자에게 예외를 처리할만한 추가 정보 제공 가능
        1)-1. 0으로 나누는 경우 -> 0으로 나눌 수 없습니다
        1)-2. 정수가 아닌 값을 입력히는 경우 -> 정수만 입력할 수 있습니다 
        등으로 특정 예외에 서로 다른 안내문을 제시한다고 하면 except문 뒤에 처리하고자 하는 예외를 모두 명시
'''
try :
    a = int(input('나누는 수(제수)를 입력하세요 >>> '))
    b = int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
    print(f'b / a = {b/a}')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
except TypeError:
    print('나눌때 자료형이 일치하지 않습니다')
except ValueError:
    print('정수만 입력할 수 있습니다')
try :
    a = int(input('나누는 수(정수)를 입력하세요 >>> '))
    b = int(input('나누어지는 수(정수)를 입력하세요 >>> '))
    print(f'b / a = {b/a}')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다')
'''
        거의 모든 예외는 Exception 클래스의 서브 클래스에 해당해 따라서 모든 예외는 Exception의 인스턴스가 된다
        except 마지막에 Exception을 명시하면 예상치 못한 예외들도 처리 가능
        
형식 :
try :
    코드 작성 영역
except 예외클래스1 :
    예외메세지1
except 예외클래스2 :
    예외메세지2
...
except Exception:
    예외메세지n
finally : 
    항시 실행되는 코드 영역

Java에서와 동일하게 Exception이 가장 상위에 있으면 모든 예외가 전부 Exception으로 잡히기에 순서도 중요

3. 예외 메세지 처리하기
    이상까지는 특정 예외갑 라생시 메세지를 커스텀했지만 기본적으로 이미 예외메세지를 보유한 경우 존재
    default exception message를 출력하는 방식 학습

형식 :
try :
    코드 작성 영역
except 예외클래스 as 예외메세지:
    예외 발생 시 처리 영역
'''
z = [10, 20, 30, 40, 50]

try :
    print(z[10])
except IndexError as e :
    print(e)
'''
4. else / finally 
    try / excepted 문에 else / finally를 달 수 있는데
    else : 예외가 발생하지 않으면 처리되는 구문
    finally : 예외 발생 여부와 관계없이 맨 마지막에 처리되는 구문
'''
try :
    a = int(input('나누는 수를 정수로 입력하세요 >>> '))
    b = int(input('나누어지는 수를 정수로 입력하세요 >>> '))
    result = b / a      # 예외 발생 가능한 구간이 try문 내에 있어야 함
    print(result)
except ZeroDivisionError as e :
    print(e)
except TypeError as e :
    print(e)
except ValueError as e :
    print(e)
except Exception as e :
    print(e)
else :
    print(f'b / a = {b / a}')
finally :
    print('프로그램 종료')
'''
5. 강제로 예외를 발생시키기
    어떤 사람이 나이를 정수로 입력받는 프로그램을 사용한가고 가정했을 때
    컴퓨터 상으로는(=파이썬 상으로는) -1000이 정수이기에 예외가 발생하지 않으나
    -1000살이 도니느건 불가능해서 조건문이 아닌 직접 예외를 발생시켜 처리 -> raise문

형식 :
raise 예외클래스()

또는
raise 예외클래스(예외메세지)

raise의 경우 강제로 예외를 발생시키는 점에서 주로 사용되는 예외클래스는 Exception
'''
age = int(input('나이를 입력하세요 >>> '))      # -1000을 입력해도 예외 발생 없음
print(f'당신의 나이는 {age}살입니다')

try :
    age = int(input('나이를 입력하세요 >>> '))
    if age < 0 or age > 200 :
        raise Exception('강제로 발생시킨 예외')
except Exception as e :
    print('발생한 예외 메세지')
    print(e)
'''
이상은 특정 예외가 아닌 raise로 넘어가려면 바로 예외 발생
즉 age에 가능한 정수값을 넣어도 예외가 발생해서 단독으로 처리가 불가능
그렇기에 이 부분은 조건문을 이용해 특정 조건일때만 예외로 넘기는 추가 코드가 필요

6. 사용자 정의 예외 클래스
    
    음수를 입력 받을때 강제로 예외를 발생시키는 예외 클래스 정의
'''
class NegativeAgeError(Exception):      # Exception 클래스를 상속받았다는 의미
    pass
    """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
# 예외를 발생시키기만 하면 되기에 굳이 코드를 쓸 필요는 없고
# Exception 클래스를 상속받았으면 슈퍼 클래스의 속성/method를 사용 가능
class TooManyAgeError(Exception):
    pass

try :
    age = int(input('나이를 입력하세요 >>> '))
    if age < 0:
        raise NegativeAgeError('나이는 음수일 수 없습니다')
    elif age > 200:
        raise TooManyAgeError('200살 초과된 나이는 입력할 수 없습니다')

except NegativeAgeError as e :
    print('발생한 예외 메세지')
    print(e)

except TooManyAgeError as e :
    print('발생한 예외 메세지')
    print(e)

else :
    print(f'당신의 나이는 {age}살 입니다.')
finally:
    print('프로그램 종료')
'''
과제 :
    나이가 200살 초과일 때 TooManyAgeError 예외를 발생시켜
    200살 초과된 나이는 입력할 수 없습니다 라는 메세지 출력
'''

''' 
과제 

사용자의 점수를 0 이상 100 이하로 입력받아서 점수가 80점 이상이면 합격, 아니면 불합격을 출력하는 프로그램을 작성하는데
0 이상 100 이하의 유효한 값이 아니면 예외를 발생시키고 점수는 0 이상 100 이하입니다 라는 메세지 출력 -> 사용자 정의 예외 클래스 정의
ScoreOutOfRangeError 클래스 정의

입력받는데 예를 들어 백점이라고 입력하면 점수는 숫자로 입력해야합니다 라는 메세지 출력
실수로 입력하면 정수로 입력해야합니다 메세지 출력

예상 할 수 없는 예외가 발생 시 Exception을 적용해 디폴트 에러 메세지 출력

프로그램 종료를 마지막에 출력
'''
class ScoreOutOfRangeError(Exception):
    pass

try :
    score = input('점수를 입력하세요 >>> ')
    if '.' in score :
        raise TypeError
    score = int(score)

    if score < 0 or score > 100 :
        raise ScoreOutOfRangeError('점수는 0 이상 100 이하입니다')

except ScoreOutOfRangeError as e :
    print('발생한 예외 메세지')
    print(e)

except ValueError :
    print('점수는 숫자로 입력해야합니다')

except TypeError :
    print('정수로 입력해야합니다')

except Exception :
    print('에러 발생')

else :
    if score >= 80 :
        print('합격')
    else:
        print('불합격')
finally:
    print('프로그램 종료')
'''
사용자로부터 숫자를 입력받아 해당 숫자로 100을 나누는 값을 출력하는 프로그램을 작성하시오.
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 예외 메세지를 출력

지시 사항
1. 사용자로부터 숫자 입력
2. 입력받은 숫자로 100을 나눠 결과 출력
3. 입력값이 0이면 0으로 나눌 수 없습니다 메세지 출력
4. 입력 값이 숫자가 아니면 적절한 예외를 처리해 숫자만 입력할 수 있습니다 메세지 출력
5. 예외가 발생하지 않은 경우 정상적으로 처리되었습니다 라는 메세지를 출력하고 결과 출력
6. 프로그램 종료 메세지 출력
'''
class ZeroNumberError(Exception):
    pass
try :
    num = float(input('숫자를 입력하세요 >>> '))
    if num == 0 :
        raise ZeroNumberError
except ZeroNumberError :
    print('0으로 나눌 수 없습니다')
except ValueError :
    print('숫자만 입력할 수 있습니다')
except Exception as e :
    print(e)
else :
    print('정상적으로 처리되었습니다')
    print(f'100 / {num} = {100 / num}')
finally:
    print('프로그램 종료')
'''
사용자로부터 리스트의 인덱스를 입력받아 인덱스의 값을 출력하는 프로그램 작성
만약 잘못된 인덱스 입력시 적절한 예외 메세지 출력

지시사항
1. 미리 정의된 리스트 존재
2. 사용자로부터 리스트의 인덱스 입력
3. 입력받은 인덱스를 사용해 리스트의 값을 출력
4. 인덱스가 리스트의 범위를 벗어나면 적절한 메세지를 출력
5. 사람을 의심하고 예상되는 예외 적용
6. 예외가 발생하지 않으면 정상적으로 처리되었습니다라는 메세지와 함께 해당 인덱스 값 출력
7. 프로그램 종료 메세지를 출력
8. 마이너스 인덱스 미적용 -> 사용자 정의 예외 클래스를 통해서 적용
    -> NegativeNumIndexError 
'''
my_list = [10, 20, 30, 40, 50]
class NegativeNumIndexError(Exception):
    pass
try:
    num = int(input('리스트의 인덱스 번호를 입력하세요 >>> '))
    if num > len(my_list)-1 or num < -len(my_list):
        raise NegativeNumIndexError
except NegativeNumIndexError as e:
    print('리스트의 범위가 아닙니다')
except ValueError as e:
    print('정수를 입력하세요')
except TypeError as e:
    print('해당값을 적용할 수 없습니다')
except Exception as e:
    print('에러발생')
else:
    print('정상적으로 처리되었습니다')
    print(my_list[num])
finally:
    print('프로그램 종료')
'''
사용자로부터 속성을 입력받아 객체의 속성값 출력
사용자가 잘못된 속성을 입력하면 적절한 예외 처리 메세지를 출력

지시 사항
1. 미리 정의된 클래스와 객체
2. 사용자로부터 속성명을 입력
3. 입력받은 속성명으로 객체의 속성값 출력
4. 잘못된 속성명을 입력하면 존재하지 않는 속성입니다 메세지 출력
5. 예외가 발생하지 않은 경우 정상적으로 처리되었습니다 메세지와 속성값 출력
6. 프로그램 종료 메세지 출력
'''
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 객체 생성
person1 = Person(name='김일', age=21)
print(vars(person1))            # 결과값 : {'name': '김일', 'age': 21}
print(getattr(person1, 'age'))  # 결과값 : 21
# getattr()의 두 번째 argument는 인스턴스 변수 명을 받는다 -> 그 데이터를 str로 받는다
print(getattr(person1, 'name')) # 결과값 : 김일

try :
    info = input("정보를 입력하시오 >>> ")
    value = getattr(person1, info)
    print(value)
except AttributeError as e:
    print('속성이 없습니다')
finally:
    print('프로그램 종료')
person1_dict = vars(person1)
'''
getattr(객체명, 속성명_str) - 특정 객체의 두 번째 argument와 일치하는 속성명의 값을 return
var(객체명) - 특정 객체의 속성명-속성값 쌍을 dictionary 형태의 key-value 쌍으로 변환해 return
'''
print(person1_dict)
attr_key = input('출력할 속성명을 입력하세요 >>> ')
print(person1_dict[attr_key])