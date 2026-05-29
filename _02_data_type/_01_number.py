# number(숫자형) : 정수, 실수, 복소수

# type(변수명 | 값)  함수: 변수 또는 값의 타입을 확인하는 내장(파이썬에 내장된) 함수.  cf. |(버티컬바) : "또는"의 의미임.

# 정수(int :integer)
n = 123
print(n, type(n))

price = 1_000_000_000; #정수 자릿수 구분
print(price, type(price))

# 정수 최댓값
import sys
print(sys.maxsize, type(sys.maxsize))

# 2진법, 8진법, 16진법
a = 0b100 #==4
b=12
print(a, type(a))
print(b, type(b))

c = 0o23  #==19

d= 0xff  #==255
print(c, type(c))
print(d, type(d))


#------------------
# 실수 (float)

m=123.456
print(m, type(m))

f2= -99999.99999
print(f2, type(f2))

f3= 1.01234567890123456789   #소수점 아래에는 16자리까지 표현이 가능하다. 프린트값이 1.0123456789012346까지 나옴
print(f3, type(f3))

#-----------------
#복소수(complex)
c = 2j
print(c, type(c))
d= 3+4j  #(3+4j)
print(d, type(d))





#==================
#산술연산 [ + , - , * , /, //(몫만 구하기) , %(modulo:나머지) , **(거듭제곱) ]

print("--산술연산--")
print(1+2)
print(1-2)
print(1*2)
print(1/2)  #나누어 떨어질 때까지의 몫을 구함.
print(1//2) #정수 영역에서의 몫만 구함
print(1%2)  #정수 영역에서의 나머지.

#거듭제곱
print(3**2)
print(3**3)
print(2**63)
print(2**64)
print(2**123)






