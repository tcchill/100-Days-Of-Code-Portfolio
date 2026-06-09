import random, time
from turtle import Screen
from classes import AlienFleet, GameManager, Player

#########################
screen = Screen()
screen.register_shape('aircraft-icon.gif')
screen.register_shape('ufo-icon.gif')
screen.register_shape('laser-icon.gif')

# ---setup screen---
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Space Invader Shooting Game")

# ---setup objects---
pl = Player(x=0, y=-200)
fleet = None
all_bullets = []
all_lasers = []
game_is_on = True
gm = GameManager()

##########################
def quit_game():
    global game_is_on
    game_is_on = False


##########################
def start_game():
    global game_is_on, all_bullets, all_lasers, fleet

    # Clean the screen
    gm.pen.clear()

    for bullet in all_bullets[:]:
        bullet.hideturtle()
    for laser in all_lasers:
        laser.hideturtle()

    if fleet is not None:
        for alien in fleet.aliens[:]:
            alien.hideturtle()

    # Set up new screen
    num_aliens = random.randint(6, 10)
    fleet_width = (num_aliens - 1) * 40
    max_start_x = 350 - fleet_width
    safe_start_x = random.randint(-350, max_start_x)
    fleet = AlienFleet(start_x=safe_start_x, start_y=250, num=num_aliens)

    all_bullets = []
    all_lasers = []
    pl.goto(0,-200)


    gm.game_rules()
    game_is_on = True

    next_attack_time = time.time() + 2

    # Game main loop
    while game_is_on:

        current_time = time.time()  # Lấy thời gian thực tại khung hình này
        if current_time >= next_attack_time:
            fleet.attack(all_lasers)  # Ra lệnh bắn và ném laser vào giỏ
            next_attack_time = current_time + 2  # Gia hạn thêm 5 giây cho lần bắn kế tiếp

        # alien moves & approach
        fleet.move()
        fleet.check_boundary()

        # aliens attack
        for laser in all_lasers[:]:
            laser.fly()
            # Nếu laser bay lọt xuống đáy màn hình thì xóa đi cho nhẹ máy
            if laser.ycor() < -280:
                laser.hideturtle()
                all_lasers.remove(laser)

        # bullets fly
        for bullet in all_bullets[:]:
            bullet.fly()
            if bullet.ycor() > 250:
                bullet.hideturtle()
                all_bullets.remove(bullet)

        # check if bullets hit aliens
        gm.bullet_hit_alien(all_bullets=all_bullets, fleet=fleet)

        # check result
        if gm.check_game(fleet=fleet, pl=pl, all_lasers=all_lasers):
            game_is_on = False

        screen.update()
        time.sleep(0.05)


def replay():
    start_game()


##########################
screen.listen()

screen.onkey(quit_game, 'q')
screen.onkey(pl.move_left, 'Left')
screen.onkey(pl.move_right, 'Right')
screen.onkey(lambda: pl.shoot(all_bullets), 'space')

screen.onkey(replay, 'r')


##########################
start_game()

screen.exitonclick()