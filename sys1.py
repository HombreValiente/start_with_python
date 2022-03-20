import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
# 입력받은 인수를 for문을 사용해 차례대로 하나식 출력하는 예.
# sys모듈의 argv는 명령 창에서 입력한 인수를 의미.