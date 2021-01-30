from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_cars()
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for _ in range(10):
            new_y = randint(-230, 270)
            new_x = randint(-280, 280)
            car = Turtle()
            car.color(choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(new_x, new_y)
            car.setheading(180)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.goto(300, car.ycor())
            car.forward(self.move_distance)

    def hit(self, player):
        for car in self.cars:
            if abs(car.ycor() - player.ycor()) < 15 and car.distance(player) < 25:
                print(car.ycor(), player.ycor())
                return True

    def change_position(self):
        for car in self.cars:
            new_y = randint(-230, 270)
            new_x = randint(-280, 280)
            car.goto(new_x, new_y)




