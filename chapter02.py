# 1.길동씨의 평균 점수
# 국어 = 80
# 영어 = 75
# 수학 = 55
# print(국어+영어+수학/3)

# 2. 13이 홀수인지 짝수인지 판별할 수 있는 방법
# 변수 값을 2로 나누어 나머지가 1인지 0인지를 통해 홀짝을 판별한다.

# 3.
# pin = '881120-1068234'
# yyyymmdd = pin[:6]
# num = pin[7:]
# print(yyyymmdd)
# print(num)

# 4. 
# pin = '881120-1068234'
# print(pin[7])

# 5.
# a = "a:b:c:d"
# b = a.replace(":", "#")
# print(b)

# 6.
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)

# 7.
# a = ['Life', 'is', 'too', 'short']
# result = ' '.join(a)
# print(result)

# 8. Hmm...
# a = (1, 2, 3)
# a = a + (4,)
# print(a)

# 9.
''' 
a = dict()
a[[1]] = 'python'의 경우 딕셔너리에서는 리스트 같이 변하는 값을 키로 사용할 수 없다.
'''

# 10. 어째서?? ---> 'B'키 값에 해당되는 값이 리턴되고 딕셔터리 a에서는 그 값이 제거되는 것을 확인할 수 있다.
# a = {'A':90, 'B':80, 'C':70}
# result = a.pop('B')
# print(a)
# print(result)

# 11.
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a)
# b = list(aSet)
# print(b)

# 12.
# a = b = [1, 2, 3]
# a[1] = 4
# print(b) # a와 b는 같은 주소에 값을 저장시키므로 한 쪽을 수정하면 다른 쪽도 수정된다.