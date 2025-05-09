import time
import random
from turtle import Turtle
from score_boardCM import Scoreboard
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1.8
CREATE_CAR_INTERVAL = 1.5

class CarManager(Scoreboard):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.last_car_creation_time = time.time()
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.choice(range(-250, 251, 20))
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.cars_speed)

    def check_create_car(self):
        current_time = time.time()
        if current_time - self.last_car_creation_time >= CREATE_CAR_INTERVAL:
            self.create_car()
            self.last_car_creation_time = current_time
    def increaseSpeedCM(self):
            self.cars_speed *= MOVE_INCREMENT

