# 3-1 if문
# money = 2000
# if money >= 3000:
#     print("택시타고 가라")
# else:
#     print("걸어가라")

# 나혼자코딩
# pocket = ['cash', 'cellphone', 'card']
# if 'card' in pocket:
#     print("버스를 타고 가라")
# else:
#     print("걸어가라")

# 조건문에서 아무것도 하지않게 설정하는 법
# pocket = ['cash', 'cellphone', 'card']
# if 'card' in pocket:
#     pass
# else:
#     print("걸어가라")

# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고,
# 돈도 없고 카드도 없으면 걸어 가라.
# pocket = ['paper', 'cellphone']
# card = True
# if 'money' in pocket:
#     print("택시를 타라")
# elif card:
#     print("택시를 타고 가라")
# else:
#     pritn("걸어가라")

# 조건부 표현식
# score = 78
# if score >= 60:
#     message = "success"
# else:
#     message = "failure"
# 위 문장은 다음과 똑같다.
# message = "success" if score >= 60 else "failure"
# print(message)


# 3-2 while문
# 열번 찍어 안 넘어가는 나무 없당
# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니당")

# 여러가지 선택지 중 하나를 선택해서 입력받는 예제
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number : """

# number = 0  # <-- 번호를 입력받을 변수
# while number != 4:    # <--- 입력 받은 번호가 4가 아닌 동안 반복
#     print(prompt)
#     number = int(input())

# coffee.py
# coffee = 10
# while True:
#     money = int(input("돈을 넣어주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# while문의 맨 처음으로 돌아가기
# a = 0
# while a < 10:
#     a = a + 1
#     if a % 2 == 0: continue  # <-- a를 2로 나누었을 때 나머지가 0이면 처음으로 돌아간다.
#     print(a)
# 나혼자코딩
# a = 0
# while a < 10:
#     a = a + 1
#     if a % 3 == 0: continue
#     print(a)

# 3-3 for문
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2...
'''
리스트나 튜플, 문자열의 첫번째 요소부터 마지막
요소까지 차례로 변수에 대입되어 '수행할 문장1', '수행할 문장2'등이 수행된다.
'''
# 1. 전형적인 for문
# test_list = ['one','two', 'three']
# for i in test_list:
#     print(i)
# 2. 다양한 for문의 사용
# a = [(1,2), (3,4), (5,6)]
# for (first, last) in a:
#     print(first + last)

# 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고, 그렇지 않으면 불합격
# marks1.py
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print("%d번 님 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# 합격한 사람은 축하메세지, 불합격은 아무것도 안보냄
# marks2.py
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60: continue
#     print("%d번 학생 합격입니다. 축하합니당" % number)

# range 함수~~
# a = range(10)  # <-- range(10)은 0부터 10미안의 숫자를 포함하는 range객체를 만들어준다.
# print(a)  # range(0, 10)   <--- 0,1,2,3,4,5,6,7,8,9  range(1,11)  <-- 1~10
# add = 0
# for i in range(1, 11):
#     add += i
# print(add)

# marks3.py
# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] < 60: continue
#     print("%d번 학생 축하드립니다. 합격입니당" % (number+1))

# 나혼자코딩
# a = 0
# for i in range(1,101):
#     a += i
# print(a)

# 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i*j, end=" ")  # end 매개변수는 해당 결과값을 출력할 때 다음 줄로 넘기지 않고, 그 줄에 계속해서 출력하기 위해서이다.
#     print('')

# 리스트 내포 사용
# a = [1, 2, 3, 4]
# result = []
# for num in a:
#     result.append(num*3)
# print(result)
# a리스트의 각 항목에 3을 곱한 결과를 result리스트에 담는 예제
# a = [1, 2, 3, 4]
# result = [num*3 for num in a]
# print(result)

# 짝수에만 3을 곱하여 담고 싶다면?
# a = [1, 2, 3, 4]
# result = [num*3 for num in a if num % 2 == 0]
# print(result)

# 구구단 다시
result = [x*y for x in range(2, 10)
    for y in range(1,10)]
print(result)