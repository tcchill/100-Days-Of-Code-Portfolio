from turtle import Turtle
import random, time


class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.shape("aircraft-icon.gif")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(x, y)
        self.setheading(90)
        self.next_shoot_time = 0
        self.cooldown_duration = 1

    def move_left(self):
        if self.xcor() > -350:
            self.goto(self.xcor() - 20, self.ycor())

    def move_right(self):
        if self.xcor() < 350:
            self.goto(self.xcor() + 20, self.ycor())

    def shoot(self, all_bullets):
        current_time = time.time()
        if current_time >= self.next_shoot_time:
            bullet = PlayerBullet(bullet_x=self.xcor(), bullet_y=self.ycor())
            all_bullets.append(bullet)
            self.next_shoot_time = current_time + self.cooldown_duration
        else:
            pass


class Alien(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("ufo-icon.gif")
        self.penup()
        self.goto(x, y)
        self.setheading(-90)
        self.x_step = 10  # mỗi frame đi 5px


class AlienFleet:
    def __init__(self, start_x, start_y, num):
        self.aliens = []
        for i in range(num):
            alien = Alien(start_x + i * 40, start_y)
            self.aliens.append(alien)

    def move(self):
        for alien in self.aliens:
            alien.goto(alien.xcor() + alien.x_step, alien.ycor())

    def check_boundary(self):
        for alien in self.aliens:
            if alien.xcor() > 350 or alien.xcor() < -350:
                for a in self.aliens:
                    a.x_step *= -1  # đổi chiều
                    a.goto(a.xcor(), a.ycor() - 40)  # đi xuống 1 hàng
                break

    def attack(self, laser_list):
        if self.aliens:
            attacker = random.choice(self.aliens)
            laser = Laser(laser_x=attacker.xcor(), laser_y=attacker.ycor() - 10)
            laser_list.append(laser)


class Laser(Turtle):
    def __init__(self, laser_x, laser_y):
        super().__init__()
        self.color("red")
        self.penup()
        self.shape("laser-icon.gif")
        self.setheading(270)
        self.goto(laser_x, laser_y)
        self.laser_speed = 15

    def fly(self):
        self.goto(self.xcor(), self.ycor() - self.laser_speed)


class PlayerBullet(Turtle):
    def __init__(self, bullet_x, bullet_y):
        super().__init__()
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y
        self.color("white")
        self.penup()
        self.shape("arrow")
        self.setheading(90)
        self.goto(bullet_x, bullet_y)
        self.bullet_speed = 15

    def fly(self):
        self.goto(self.xcor(), self.ycor() + self.bullet_speed)


class GameManager():
    def __init__(self):
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.color('white')

    def game_rules(self):
        self.pen.penup()
        self.pen.goto(160, 280)
        self.pen.pendown()
        self.pen.write('Press "Q" or Click mouse to quit.', font=("Arial", 10, "bold"))
        self.pen.penup()
        self.pen.goto(160, 260)
        self.pen.pendown()
        self.pen.write('Press "R" to replay.', font=("Arial", 10, "bold"))

    def bullet_hit_alien(self, all_bullets, fleet):
        for bullet in all_bullets:
            for alien in fleet.aliens:
                if bullet.distance(alien) < 20:
                    bullet.hideturtle()
                    all_bullets.remove(bullet)

                    alien.hideturtle()
                    fleet.aliens.remove(alien)

    def alien_hit_player(self, fleet, pl):
        for alien in fleet.aliens:
            if alien.distance(pl) < 50:
                return True
        return False

    def laser_hit_player(self, laser_list, pl):
        for laser in laser_list[:]:
            if laser.distance(pl) < 30:
                laser.hideturtle()
                laser_list.remove(laser)
                return True
        return False

    def check_game(self, fleet, pl, all_lasers):
        self.pen.penup()
        self.pen.goto(0, 200)

        if fleet is not None and not fleet.aliens:
            self.pen.pendown()
            self.pen.write('You win', align="center", font=("Courier", 24, "bold"))
            return True
        if self.alien_hit_player(fleet, pl):
            self.pen.pendown()
            self.pen.write('You lose', align="center", font=("Courier", 24, "bold"))
            return True
        if self.laser_hit_player(all_lasers, pl):  # ← thêm check này
            self.pen.pendown()
            self.pen.write('You lose', align="center", font=("Courier", 24, "bold"))
            return True
        return False