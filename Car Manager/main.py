from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from score_boardCM import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Car Manager')
screen.bgcolor('white')
screen.tracer(0)

score = Scoreboard()
Gamer= Player()
car_manager = CarManager()
screen.listen()
screen.onkey(Gamer.go_up, "w")
screen.onkey(Gamer.go_down, "s")
gameISOn =True
while gameISOn:
    screen.update()
    car_manager.check_create_car()
    car_manager.move_cars()
    time.sleep(0.1)

    for car in car_manager.all_cars:
        if car.distance(Gamer) < 20:
            gameISOn =False
            score.game_overCM()
    if Gamer.ycor() > 280:
        Gamer.goto(0,-280)
        print("Level up!")
        score.increase_scoreCM()
        car_manager.increaseSpeedCM()



screen.exitonclick()