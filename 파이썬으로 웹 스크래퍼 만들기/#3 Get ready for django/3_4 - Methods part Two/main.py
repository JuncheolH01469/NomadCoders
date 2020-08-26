# 클래스 만들기
class Car():

    # 기존 함수의 재정의 ( Override ) 가능
    def __str__(self):
        return f"Car with {self.wheels} wheels"

    def __init__(self, **kwargs):
        # Properties
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")   # get(key, default value)
        self.price = kwargs.get("price", "$20")     # get(key, default value)

porche = Car(color="green", price="$40")
print(porche.color, porche.price)

mini = Car()
print(mini.color, mini.price)

# 출력시 실제로 파이썬이 하고 있는 일
# print(porche.__str__())