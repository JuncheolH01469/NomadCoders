# Example 1
def minus(a, b):
    return a - b

# 위치에 영향을 받지 않고 인자의 이름에 맞게 해당 값이 대입되어 값을 리턴한다
result = minus(b = 25, a = 8)

print(result)

# string 안에 변수를 포함시키고 싶다면 string 앞에 f ( format )를 써줌
# Example 2
def say_hello(name, age):
    return f"Hello {name} you are {age} years old"

hello = say_hello("Gildong", "25")

print(hello)