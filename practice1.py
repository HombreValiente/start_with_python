# multiline = '''
# Life is too short
# so you need python
# '''
# print(multiline)

# a = "python"
# print(a*2)

# a = "You need python"
# print(len(a))

# a = "Life is too short, you need python"
# print(a[0:4])
# print(a[:17])
# print(a[:])

# a = "20010331Rainy"
# year = a[:4]
# day = a[4:8]
# weather = a[8:]
# print(year, day, weather)

# a = "Pithon"
# print(a[:1] + 'y' + a[2:])

# a =  "I eat %d apples."
# print(a %3)

# number = 10
# day = "three"
# a = "I ate %d apples. so I was sick for %s days." % (number, day)
# print(a)

# 정렬과 공백
# a = "%10s" % "hi"
# print(a)

# a = "%-10sjane" % 'hi'
# print(a)

# 소수점 표현하기
# a = "%0.4f" % 3.42134234
# print(a)
# b = "%10.4f" % 3.42134234
# print(b)

# format 함수를 이용한 포맷팅
# a = "I eat {0} apples".format(3)
# print(a)
# a = "I eat {0} apples".format("five")
# print(a)
# number = 10
# a = "I eat {0} apples".format(number)
# print(a)
# a = "I eat {number} apples. so I was sick for {days} days".format(number=10, days=3)
# print(a)
# a = "I eat {0} apples. so I was sick for {day} days".format(10, day=3)
# a = "{0:<10}".format("hi")   # 왼쪽으로 정렬
# print(a)
# b = "{0:>10}".format("hi")   # 오른쪽으로 정렬
# print(b)
# a = "{0:^10}".format("hi")     # 가운데로 정렬
# print(a)
# 공백 채우기
# a = "{0:=^10}".format("hi")
# print(a)
# b = "{0:!<10}".format("hi")
# print(b)
# 소수점 표현
# y = 3.4231234
# a = "{0:0.4f}".format(y)
# print(a)
# {또는} 문자 표현하기
# a = "{{and}}".format()
# print(a)

# f 문자열 포맷팅
# name = " 홍길동 "
# age = 30
# a = f'나의 이름은 {name}이고, 나이는 {age + 1}입니다.'
# print(a)
# d = {'name':'홍길동', 'age':'30'}
# a = f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
# print(a)
# a = f'{"hi":<10}'
# b = f'{"hi":>10}'
# c = f'{"hi":^10}'
# d = f'{"hi":=^10}'
# e = f'{"hi":!>10}'
# print(a, b, c, d, e)
# a = f'{"python":!^12}'
# print(a)

# 문자열 관련 함수
# 문자 개수 세기(count)
# a = "hobby"
# c = a.count('b')
# print(c)

# 위치 알려주기(find) # 찾는 문자나 문자열이 없으면 -1을 반환
# a = "python is the best choice"
# c = a.find('b') 
# d = a.find('k')
# print(c, d)

# 위치 알려주기(index)  # 찾는 문자나 문자열이 없으면 오류
a = "Life is too short"
# in1 = a.index('t')
# # in2 = a.index('k')
# print(in1)

# 문자열 삽입(join)
a = ",".join('abcd')
print(a)
# b = ",".join(['a', 'b', 'c', 'd'])
# print(b)

# 소문자를 대문자로 바꾸기(upper)
# a = 'hi'
# b = a.upper()
# print(b)

# 대문자를 소문자로 바꾸기(lower)
# a = "HI"
# b = a.lower()
# print(b)

# 왼쪽 공백 지우기(lstrip)"
# a = " hi "
# b = a.lstrip()
# print(b)

# 오른쪽 공백 지우기(rstrip)
# c = " hi "
# d = c.rstrip()
# print(d)
# 양쪽 공백 지우기(strip)
# a = " hi "
# b = a.strip()
# print(b)

# 문자열 바꾸기(replace)
# a = "Life is too short"
# b = a.replace('Life', 'Your leg')
# print(b)

# 문자열 나누기(split)
# a = "Life is too short"
# b = a.split()   # 공백을 기준으로 문자열을 나눈다
# print(b)
# c = "a:b:c:d"
# d = c.split(":")  # : 기호를 기준으로 문자열을 나눈다
# print(d)