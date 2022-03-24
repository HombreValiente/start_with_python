# 5-1 클래스
# 과자 틀 --> 클래스(class)
# 과자 틀을 사용해 만든 과자 --> 객체(object)
# 클래스로 만든 객체는 객체마다 고유한 성격을 가지는 특징이 있다.

# class Cookie:
#     pass

# a = Cookie()
# b = Cookie()

# 사칙연산 클래스 만들기
# 객체 만들기
# class FourCal:
#     pass

# a = FourCal()
# print(type(a))

# 객체에 숫자 지정할 수 있게 만들기
class Fourcal:
    def setdata(self, first, second):    # 클래스 안에서 구현된 함수는 method라 부른다.
        self.first = first
        self.second = second
# setdata의 첫번째 매개변수 self에는 setdata 매서드를 호출한 객체 a가 자동으로 전달된다.
a = Fourcal()
print(a.setdata(4,2))
