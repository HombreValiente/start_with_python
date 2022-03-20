# 4-2 사용자 입력과 출력

# 사용자 입력 - 사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때
# a = input()
# print(a)
# number = input("숫자를 입력하세요")
# print(number)

# print문 알아보기
# "로 둘러싸인 문자열은 +연산과 동일
# print("life" "is" "too" "short")
# print("life" "is" "too short")
# 문자열 띄어쓰기는 ,로 한다.
# print("life", "is", "too short")
# 한줄에 결과값 출력할려면 매개변수 end 사용해 끝문자 지정
# for i in range(10):
#     print(i, end=' ')


# 4-3 파일 읽고 쓰기

# 파일 생성하기
'''
파일열기 모드: 
1. r -> 읽기 모드 - 파일을 읽기만 할 때 사용
2, w -> 쓰기 모드 - 파일에 내용을 쓸 때 사용
3. a -> 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
'''

# f = open(r"c:\Users\KIM DONGHYUN\Desktop\doit\새파일.txt", 'w')  # 파일객체 = open(파일이름, 파일열기 모드)
# f.close()

# 파일을 쓰기 모드로 열어 출력값 적기
# f = open(r"c:\Users\KIM DONGHYUN\Desktop\doit\새파일.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)   # data를 파일 객체 f에 써라
# f.close

# 프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
# readline 함수 사용하기
# f = open(r"c:\Users\KIM DONGHYUN\Desktop\doit\새파일.txt", 'r')
# line = f.readline()  # 파일의 첫번째 줄만을 출력
# print(line)
# f.close()

# 모든 줄을 읽는 법
# f = open(r"c:\Users\KIM DONGHYUN\Desktop\doit\새파일.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break  # readline()은 더이상 읽을 줄이 없는 경우 None을 출력한다.
#     print(line)
# f.close

# 입력 받은 내용을 그대로 출력
# while 1:
#     data = input()
#     if not data: break
#     print(data)

# readlines 함수 사용
# f = open(r"c:\Users\KIM DONGHYUN\Desktop\doit\새파일.txt", 'r')
# lines = f.readlines()   # lines는 리스트 ["1번째 줄입니다.", .... "10번쨰 줄입니다."]가 저장된다.
# for line in lines:
#     print(line)
# f.close()

# read 함수 사용하기
# data = f.read()  # f.read()는 파일의 내용 전체를 문자열로 돌려준다.
# print(data)
# f.close()

# 파일에 새로운 내용 추가하기
# 쓰기모드'w'로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다.
# 원래 있던 값을 유지하면서 새로운 값만 추가해야되는 경우 파일을 추가모드'a'로 열면 된다.
f = open(r"c:\Users\KIM DONGHYUN\Desktop\doit\새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함께 사용하기
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
# with문을 사용하면 with블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close된다.