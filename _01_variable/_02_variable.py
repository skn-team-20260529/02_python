# 변수(variable) : 값(literal)을 저장하는 메모리상의 공간. 각 변수마다 이름이 지정되어 있음.(이름을 불러서 사용)

# 변수 선언 방법
# 변수명 = 값
a = 10 #a라는 메모리상의 공간에 10이라는 literal을 대입
b = '홍길동' #b라는 메모리상 공간에 홍길동이라는 literal 대입

print("a =", a)
print("b =", b)

#대입연산자(=) : 우항의 값을 좌항의 변수에 대입. 무조건 오른쪽을 왼쪽에 대입함!!!
num = 100
print("num =", num) #100

#변수는 저장된 값이 변할 수 있다.
num = 999
print("num =", num)

num = 1
num = "abcded"
print("num =", num)

# 변수 명명규칙
# 1. 의미 있는 이름 사용하기
# 2. 변수명은 snake casing을 사용(소문자와 '_' 언더스코어만 사용)
# 단, 대문 사용 가능하고, 소문자와 구분된다. 라지A와 스몰a는 다른것으로 인식함.

team_name = "오지라퍼스"
print(team_name)    # 오지라퍼스

Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

밥조 = "4조"
print(밥조)


# 변수명은 숫자로 시작해서는 안된다. 왜냐하면 문법오류가 발생함 (문법오류 == 빨간줄)  cf.등호는 == 두번임.
name_1 = "콩쥐"
# 1_name = "팥쥐" #문법에러
_1_name = "신데렐라"

#특수문자는 언더스코어(_)를 외에는 쓰지 않음. (하이픈도 안됨)
# team-name = "오지라퍼스"  #에러
# team@name = "바보" #에러

# 예약어는 변수명으로 사용 불가 (파란색으로 변함)
#if
#else
#for

#파이썬 예약어 종류 확인
import keyword
print(keyword.kwlist)



