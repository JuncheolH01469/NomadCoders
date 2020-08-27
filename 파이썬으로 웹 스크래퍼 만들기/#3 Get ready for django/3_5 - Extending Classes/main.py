# 클래스 만들기
class Car():

    # 기존 함수의 재정의 ( Override ) 가능
    def __init__(self, **kwargs):
        # Properties
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")   # get(key, default value)
        self.price = kwargs.get("price", "$20")     # get(key, default value)

    def __str__(self):
        return f"Car with {self.wheels} wheels"

# Inherit( 상속 ) / Extend ( 확장 )
# Car 클래스 안의 properties, override method 등 사용 가능
class Convertible(Car):

    def __init__(self, **kwargs):
        # super() - 부모 클래스 호출
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"

porche = Convertible(color="green", price="$40")
print(porche.color)
