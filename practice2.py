# 2-3 리스트 자료형
'''비어있는 리스트는 a = list()로 생성할 수 있다.
리스트명 = [요소1, 요소2, 요소3, ...]
e = [1, 2, ['Life', 'is']] 처럼 리스트 자체를 요솟값으로 가질 수 있다.
리스트 안에는 어떠한 자료형도 포함시킬 수 있다.'''

# 리스트는 문자열처럼 인덱싱과 슬라이싱이 가능하다.
# a = [1,2,3]
# print(a)
# print(a[0])
# print(a[0] + a[2])  # <--- 1 + 3

'''a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0])   # <--- ['a', 'b', 'c'] 안에 첫번째 요소를 가져온다.'''

# A = [1, 2, 3, 4, 5]
# print(A[1:3])
# a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(a[3][:2])

# 리스트 더하기
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# 리스트 반복하기
# a = [1, 2, 3]
# print(a * 3)
# 리스트 길이 구하기
# a = [1, 2, 3]
# print(len(a))

# 문자형과 정수를 더할 때
# a = [1, 2, 3]
# print(str(a[2]) + "hi")

# 리스트에서 값 수정하기
# a = [1, 2, 3]
# a[2] = 4
# print(a)
# a = [1, 2, 3]
# del a[1]
# print(a)
# a = [1, 2, 3, 4, 5]
# del a[:2]
# print(a)

# 리스트 요소 추가(append)
# a = [1, 2, 3]
# a.append(4)  # <--- 리스트 마지막에 4를 추가
# print(a)
# a.append([5,6])
# print(a)
# 리스트 정렬(sort)
# a = [1, 4, 3, 2]
# a.sort()
# print(a)
# a = ['a', 'c', 'b']
# a.sort()
# print(a)
# 리스트 뒤집기(reverse)
# a = ['a', 'c', 'b', 'd']
# a.reverse()
# print(a)
# 위치 반환(index)
# a = [1, 2, 3]
# b = a.index(3)  # <--- a의 세번째(a[2]) 요소
# print(b)
# 리스트에 요소 삽입(insert)
# a = [1, 2, 3]
# a.insert(0, 4)  # <--- a[0] 위치에 4 삽입
# print(a)
# a.insert(3, 5)  # <--- a[3] 위치에 5 삽입
# print(a)
# 리스트 요소 제거(remove) remove(x)는 리스트에서 첫번째로 나오는 x를 삭제하는 함수
# a = [1, 2, 3, 1, 2, 3]
# a.remove(3)
# print(a)
# a.remove(3)
# print(a)
# 리스트 요소 끄집어내기(pop)  pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
# a = [1, 2, 3]
# a.pop()
# print(a)
# a.pop(1)    # <--- a[1]의 요소를 제거
# print(a)
# 리스트에 포함된 요소 x의 개수 세기(count)
# a = [1, 2, 3, 1]
# b = a.count(1)
# print(b)
# 리스트 확장(extend)  extend(x)에서 x에는 리스트만 올 수 있으며, 원래의 a 리스트에 x리스트를 더하게 된다.
a = [1, 2, 3]
a.extend([4, 5])    # extend([4,5])는 a += [4, 5]와 동일하다.
print(a)
b = [6, 7]
a.extend(b)
print(a)