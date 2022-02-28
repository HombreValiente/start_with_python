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
y = 3.4231234
a = "{0:0.4f}".format(y)
print(a)