# 클래스 만들기
class Car():
    # Properties
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    # 메소드 만들기
    def start(self):
        print("I started")

porche = Car()
porche.start()