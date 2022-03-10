# 2-4 튜플 자료형
# 리스트는 []로 둘러싸지만 튜플은 ()으로 둘러싼다.
# 리스트는 그 값의 생성,삭제,수정이 가능하지만 튜플은 그 겂을 바꿀 수 없다.
'''
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
튜플에서는 t2와 같이 1개의 요소만을 가질 때는 요소 뒤에 콤마를 반드시 붙여야 하고,
t4처럼 괄호를 생략해도 무방하다.
프로그램이 실행되는 동안 그 값이 항상 변하지 않기를 바라거나 혹시 값이 바뀔까 걱정된다면
튜플 사용!
'''
# 튜플은 값을 변화시킬 수 없다는 점만 제외하면 리스트와 완전히 동일
# t1 = (1, 2, 'a', 'b')
# print(t1[0])
# print(t1[1:])
# t2 = (3, 4)
# print(t1 + t2)
# a = (1, 2, 3)
# b = (4,)
# print(a + b)
# print(a + (4,))


# 2-5 딕셔터리 자료형
# 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고, key를 통해 value를 얻는다.
# Key에는 변하지 않는 값을 사용하고, value에는 변하는 값과 변하지 않는 값 모두 사용 가능.

# 딕셔터리 쌍 추가, 삭제
# a = {1: 'a'}
# a[2] = 'b' # <--- {2:'b'}쌍 추가
# print(a)
# a['name'] = 'pey'  # <--- {'name':'pey'}
# print(a)
# a[3] = [1,2,3]  # <--- {3: [1,2,3]} 쌍 추가
# print(a)

# del a[1]
# print(a)

# 딕셔너리에서 key 사용해 value 얻기
# grade = {'pey': 10, 'julliet': 99}
# print(grade['pey'])
# print(grade['julliet'])
# a = {1: 'a', 2: 'b'}
# print(a[1])
# print(a[2])

# 주의사항!
'''
Key는 고유한 값이므로 동일한 Key가 존재하면 안된다.
Key에는 리스트는 쓸 수 없지만 튜플은 가능
'''

# 딕셔너리 관련 함수
# key 리스트 만들기(keys)  <--- 딕셔너리 안의 key만을 모아서 dict_keys 객체를 돌려준다.
# a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
# b = a.keys()
# print(b)
# for k in a.keys():
#     print(k)
# c = list(a.keys())  # dict_keys 객체를 리스트로 변환시킨다.
# print(c)

# value 리스트 만들기(values)  <--- 딕셔너리 안의 value만 모아 dict_values 객체를 돌려준다.
# b = a.values()
# print(b)
# key,value 쌍 얻기(items)
#  c = a.items()
# print(c)
# key:value 쌍 모두 지우기(clear)
# print(a.clear())
# key로 value 얻기(get)
# d = a.get('name')
# print(d)
# print(a.get('phone'))
'''a['nokey]처럼 존재하지 않는 키는 key 오류를 발생시키고
a.get['nokey']는 None을 돌려준다는 차이가 있다'''
# print(a.get('nokey'))
# print(a['nokey'])

# 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고
# 싶을 때는 get(x, '디폴트 값')을 사용하면 편리하다.
# print(a.get('foo', 'bar'))  # <-- a딕셔너리에는 'foo'에 해당하는 값이 없으므로 디폴트 값인 'bar'를 돌려준다.

# 해당 key가 딕셔너리 안에 있는지 조사하기(in)
# print('name' in a)
# print('email' in a)
# 나혼자코딩
# a = {'name':'홍길동', 'birth':'1128', 'age' : '30'}

# 2-6 집합 자료형
'''
set 자료형의 특징
- 중복을 허용하지 않는다.
- 순서가 없다. (따라서 인덱싱 불가)
'''
# s1 = set([1, 2, 3])
# l1 = list(s1)  # <-- 리스트로 변환
# print(l1)
# print(l1[0])
# s2 = set('Hello')
# t1 = tuple(s2)  # <-- 튜플로 변환
# print(t1)

# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# 교집합
# print(s1 & s2)
# print(s1.intersection(s2))
# print(s2.intersection(s1))
# 합집합
# print(s1 | s2)
# print(s1.union(s2))
# 차집합
# print(s1 - s2)
# print(s2 - s1)
# print(s1.difference(s2))

# 값 1개 추가하기(add)
# s1 = set([1, 2, 3])
# s1.add(4)
# print(s1)
# 값 여러 개 추가하기(update)
# s1 = set([1, 2, 3])
# s1.update([4, 5, 6])
# print(s1)
# 특정값 제거해기(remove)
# s1 = set([1, 2, 3])
# s1.remove(2)
# print(s1)


# 2-7 불 자료형
'''
불(bool) 자료형이란 참과 거짓을 나타내는 자료형으로 True, False 두가지의 값만을 가질 수 있다.
'''
# a = True
# b = False
# print(type(a))
# print(type(b))
# print(1==1)
# print(1>2)
# print([])

# if []:
#     print("cham")
# else:
#     print("gueji")

# print(bool('python'))
# print(bool(''))
# print(bool(0))

# 2-8 자료형의 값을 저장하는 공간, 변수
'''
변수란, 파이썬에서 사용하는 객체를 가르키는 것. 객체란 자료형과 같은 것을 의미
a = [1,2,3]이라고 하면 [1,2,3] 값을 가지는 리스트 자료형(객체)이 자동으로 메모리에
생성되고 변수 a는 [1,2,3]리스트가 저장된 메모리의 주소를 가르키게 된다.
'''
# a = [1,2,3]
# print(id(a))  # id함수는 변수가 가리키고 있는 객체의 주소 값을 돌려주는 파이썬 내장 함수

# 리스트를 복사할 때
# a = [1,2,3]
# b = a   # <-- b는 a와 완전히 동일. 
# print(a is b)
# a[1] = 4
# print(a)
# print(b)

# b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가르키도록 만들기
# 1. [:]사용
# a = [1,2,3]
# b = a[:] # <--- 리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
# a[1] = 4
# print(a)
# print(b)
# 2.copy모듈 사용
# from copy import copy
# a = [1,2,3]
# b = copy(a)  # <--- b = a[:]와 동일
# print(a)
# print(b)
# print(b is a)

# 변수 만들기
# a, b = ('python', 'life')
# (a, b) = 'python', 'life'  # 위 예문과 동일
# [a, b] = ['python', 'life']
# a = b = 'python'
a = 3
b = 5
a, b = b, a # <-- a와 b의 값을 바꿈
print(a)
print(b)