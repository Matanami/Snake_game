from turtle import Turtle
ALIGN = "center"
FONT = ('calibri', 18, 'normal')
LOCATION = 0,280

class Scorebored(Turtle):
    

    def __init__(self):
        super().__init__()
        self.goto(LOCATION)
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        with open("highes.txt", 'r') as high:
            self.high_score = int(high.read())

        self.updatescore()


    def updatescore(self):
        self.clear()
        self.color('pink')
        self.write(f"Score: {self.score}   High Score: {self.high_score}",False, align=ALIGN,font=FONT)

    def reset_borde(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highes.txt",'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.updatescore()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.updatescore()