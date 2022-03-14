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
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타라")
elif card:
    print("택시를 타고 가라")
else:
    pritn("걸어가라")

# 조건부 표현식
score = 78
# if score >= 60:
#     message = "success"
# else:
#     message = "failure"
# 위 문장은 다음과 똑같다.
message = "success" if score >= 60 else "failure"
print(message)