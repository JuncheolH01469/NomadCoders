# 클래스 만들기
class Car():
    # Properties
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

# Instance 만들기
porche = Car()
porche.color = "Red"

ferrari = Car()
ferrari.color = "Yellow"

mini = Car()
mini.color = "White"

print(porche.color)
print(ferrari.color)
print(mini.color)