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

def say():
    print("Hi")

say()