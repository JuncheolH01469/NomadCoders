# Example 1
def say_hello(who):
    print("Hello", who)

say_hello("Gildong")

# Example 2
def plus(a, b):
    print(a + b)

def minus(a, b):
    print(a - b)

plus(56, 32)
minus(56, 32)

# Example 3
def plus(a, b):
    print(a + b)

# b=0 : b 인자 자리에 아무 숫자도 오지 않을 경우 대입할 b를 설정 (default value)
def minus(a, b=0):
    print(a - b)

plus(56, 32)
minus(56)