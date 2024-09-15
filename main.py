import pgzrun
import random

WIDTH = 512
HEIGHT = 544

background = Actor("map")
background.topleft = 0,0

ship = Actor("ship")
ship.pos = WIDTH/2, HEIGHT/2
health = 5
enemykillCharge = ""
explosionFrames = ["explosion1", "explosion2", "explosion3", "explosion4", "explosion5", "explosion6"]
attack = False

enemyImages = ["blueenemy", "greenenemy", "greyenemy", "redenemy"]
enemies = []
timer = 0
explosions = []
game = True
def draw():
    global timer, health, enemykillCharge, game
    screen.clear()
    background.draw()
    ship.draw()
    screen.draw.text(f"Health: {health}", center = (WIDTH/2, 30))
    screen.draw.text(f"Charge: {enemykillCharge}", center = (WIDTH/2, 50))
    charge = len(str(enemykillCharge))
    if game == True:
        for explosion in explosions:
                explosion.draw()
        timer += 1

        if timer % 88 == 0:
                makeEnemies()
                timer = 0
        if health < 1:
                screen.draw.text(f"Health: {health}, You Lose", center = (WIDTH/2, HEIGHT/2))  
                game = False
        
        if len(str(enemykillCharge)) >= 10 and game == True:
                text = f"charge:{charge}  You Won!!"
                screen.draw.text(text, center = (WIDTH/2, HEIGHT/2))
                game = False
        for enemy in enemies:
                enemy.draw()
                animate(enemy,pos = ship.pos, angle = enemy.angle_to(ship.pos) - 90, duration = 0.75, tween = "accel_decel")
                if enemy.colliderect(ship):
                        if attack == False:
                                health -= 1
                        explosions.append(Actor("explosion1"))
                        explosions[-1].pos = enemy.pos
                        enemykillCharge += "-"
                        enemies.remove(enemy)
    if game == False:
                screen.clear()
                background.draw()
                ship.draw()
                if health < 1:
                    screen.draw.text(f"Health: {health}, You Lose", center = (WIDTH/2, HEIGHT/2))  
                if len(str(enemykillCharge)) >= 10:
                        text = f"charge:{charge}  You Won!!"
                        screen.draw.text(text, center = (WIDTH/2, HEIGHT/2))
def on_mouse_down(pos):
        global attack, game, ship
        if attack == False:
                attack = True
        if game == True:
                animate(ship,pos = pos, angle = ship.angle_to(pos) - 90, duration = 1, tween = "bounce_end", on_finished = attackEnd)

def attackEnd():
    global attack
    attack = False

def makeEnemies():
    enemy = Actor("greenenemy")
    enemies.append(enemy)
    enemy.image = enemyImages[random.randint(0,3)]

    if enemy.image == "greenenemy":
        enemy.pos = 0,0

    elif enemy.image == "blueenemy":
        enemy.pos = WIDTH,0

    elif enemy.image == "redenemy":
        enemy.pos = 0, HEIGHT

    elif enemy.image == "greyenemy":
        enemy.pos = WIDTH, HEIGHT

def updateexplosion():
        for explosion in explosions:
                if explosion.image == "explosion1":
                        explosion.image = "explosion2"
                elif explosion.image == "explosion2":
                        explosion.image = "explosion3"
                elif explosion.image == "explosion3":
                        explosion.image = "explosion4"
                elif explosion.image == "explosion4":
                        explosion.image = "explosion5"
                elif explosion.image == "explosion5":
                        explosion.image = "explosion6"
                elif explosion.image == "explosion6":
                        explosions.remove(explosion)

        clock.schedule(updateexplosion, 0.1)
clock.schedule(updateexplosion, 0.1)
pgzrun.go()
