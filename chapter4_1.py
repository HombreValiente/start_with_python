# 4-1 함수
# def add(a, b):  # <--a, b는 매개변수
#     return a + b

# a = 3
# b = 4
# c = add(a, b)
# print(c)

# print(add(3, 4))  # <--- 3, 4는 인수

# 입력값과 결과값에 따른 함수의 형태
# 함수의 형태는 입력값과 결과값의 존재 유무에 따라 4가지 유형으로 나뉜다.

# 1. 일반적인 함수. (입력값과 결과값이 있는 함수)
# 결과값을 받을 변수 = 함수이름(입력인수1, 입력인수2, ...)
# def add(a, b):
#     result = a + b
#     return result  # <-- a+b의 결과값 반환

# a = add(3, 4)
# print(a)

# 2. 입력값이 없는 함수
# 결과값을 받을 변수 = 함수이름()
# def say():
#     return 'Hi'

# a = say()
# print(a)

# 3. 결과값이 없는 함수
# 함수이름(입력인수1, 입력인수2,...)

# def add(a, b):
#     print("%d, %d의 합은 %d입니다." % (a, b, a+b))

# a = add(3,4)
# print(a)

# 4. 입력값도 결과값도 없는 함수
# 함수이름()

# def say():
#     print("Hi")

# say()

# 매개변수 지정하여 호출하기
# def add(a, b):
#     return a+b

# result = add(a=3, b=7)
# print(result)
# result = add(b=5, a=3)   # <-- 매개변수를 지정하면 순서에 상관없이 사용할 수 있다.
# print(result)    

# 입력값이 몇개가 될지 모를 때 <-- 매개변수 앞에 *을 붙인다.
# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# result = add_many(1,2,3)
# print(result)
# result = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)

# def add_mul(choice, *args):
#     if choice == 'add':  # <-- 매개변수 choice에 'add'를 입력받았을 때
#         result = 0
#         for i in args:
#             result += i   # <-- args에 입력받은 모든 값을 더한다.
#     elif choice == 'mul':  # <-- 매개변수 choice에 'mul'을 입력받았을 때
#         result = 1
#         for i in args:
#             result *= i
#     return result

# result = add_mul('add', 1,2,3,4,5)
# print(result)
# result = add_mul('mul', 1,2,3,4,5)
# print(result)

# 키워드 파라미터 <-- 매개변수 이름 앞에 **을 붙이면 딕셔너리가 되어
# 모든 key = value 형태의 결과값이 그 딕셔너리에 저장된다.
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a= 1)
# print_kwargs(name = 'foo', age = 3)

# 함수의 결과값은 항상 하나
# def add_and_mul(a,b):
#     return a+b, a*b

# result = add_and_mul(3,4)
# print(result)
# result1, result2 = add_and_mul(3,4)
# print(result1, result2)
# def add_and_mul(a,b):
#     return a+b
#     return a*b
# 함수는 return문을 만나는 순간 결과값을 돌려준 다음 함수를 빠져나가므로 위 코드는 제대로 작동하지 않는다.

# 특별한 상황에서 함수를 빠져나가고 싶다면 return을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.
# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s입니다." % nick)

# say_nick("바보")

# 매개변수 초기값 미리 설정하기 - 초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓자!
# def say_myself(name, old, man=True):
#     print("나의 이름은 %s입니다." % name)
#     print("나의 이름은 %s입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("김동현", 25)
# say_myself("김동현", 25, True) # man변수에 입력값을 주지 않아도 초깃값을 설정했기 때문에 둘의 결과는 같다.
# say_myself("김동현", 20, False)

# 함수 안에서 선언한 함수의 효력 범위
# vartest.py
# a = 1  # <-- 함수 밖의 변수 a
# def vartest(a):
#     a = a + 1  # vartest 함수 선언

# vartest(a)   # vartest 함수의 입력값으로 a를 줌
# print(a)    # a값 출력
# 함수 안에서 선언한 매개변수는 함수 안에서만 사용될 뿐 함수 밖에서는 사용되지 않는다.


#함수 안에서 함수 밖의 변수를 변경하는 방법
# 1. return 사용하기
# vartest_return.py
# a = 1
# def vartest(a):
#     a = a + 1
#     return a

# a = vartest(a)   # vartest(a)의 결과값을 함수 밖의 변수 a에 대입
# print(a)
# 2. global 명령어 사용하기 -- 가급적이면 1번 방법 사용
# vartest_global.py
# a = 1
# def vartest():
#     global a   # 함수 안에서 함수 밖의 a변수를 직접 사용하겠다는 뜻
#     a = a + 1

# vartest()
# print(a)

# lambda
# def와 동일한 역할. 보통 함수를 한 줄로 간결하게 만들 때 사용한다.
# lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식
# add = lambda a, b: a+b
# result = add(3, 4)
# print(result)