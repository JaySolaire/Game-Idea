#speed1 = speed1 -1
#speed2 = speed2 - counter
#speed3 = speed3 - counter**2
#speed4 = speed4 - counter2
#counter +=1
#counter2 += Scqrrt (counter2)

import sys, pygame, math
pygame.init()


#Create Screen
screenSize = width, height = 1000,600
screenColor = (150, 150, 255)
screen = pygame.display.set_mode(screenSize)

#Create Projectiles
ballImage1 = pygame.image.load("ball.bmp")
ball1 = ballImage1.get_rect()
ballImage2 = pygame.image.load("ball.bmp")
ball2 = ballImage2.get_rect()
ballImage3 = pygame.image.load("ball.bmp")
ball3 = ballImage3.get_rect()
ballImage4 = pygame.image.load("ball.bmp")
ball4 = ballImage4.get_rect()

#Separate Projectiles
ball1 = ball2.move(10,100)
ball2 = ball2.move(10,200)
ball3 = ball3.move(10,300)
ball4 = ball4.move(10,400)

#Set Initial Speeds
speed1 = 100.0
speed2 = 100.0
speed3 = 100.0
speed4 = 100.0

counter = 1.0
counter2 = 1.0

while (1):
	
	#Update Speeds
	speed1 = speed1 -5
	speed2 = speed2 - counter
	speed3 = speed3 - counter**2
	speed4 = speed4 - counter2
	counter +=1
	counter2 += math.sqrt(counter2)
	if speed1 < 0:
		speed1 = 0
	if speed2 < 0:
		speed2 = 0
	if speed3 < 0:
		speed3 = 0
	if speed4 < 0:
		speed4 = 0
	#Move balls
	ball1 = ball1.move(speed1, 0)
	ball2 = ball2.move(speed2, 0)
	ball3 = ball3.move(speed3, 0)
	ball4 = ball4.move(speed4, 0)
	
	#Update Screen
	screen.fill(screenColor)
	screen.blit(ballImage1, ball1)
	screen.blit(ballImage2, ball2)
	screen.blit(ballImage3, ball3)
	screen.blit(ballImage4, ball4)
	pygame.display.flip()
	
	#CHECK FOR EXIT
	events=pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
	pygame.time.delay(100) 

