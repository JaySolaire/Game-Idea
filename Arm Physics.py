import sys, pygame, math
pygame.init()

def setMagnitude(listA, mag):
	if mag == 0:
		return [0,0]
	size = math.sqrt(listA[0]**2 + listA[1]**2)
	if size == 0:
		return [0,0]
	size = size / mag
	listA[0] = listA[0] / size
	listA[1] = listA[1] / size
	return listA
	
def getMagnitude(listA):
	if listA[0] == 0 and listA[1] == 0:
		return 0
	size = math.sqrt(listA[0]**2 + listA[1]**2)
	return size
	

#Create Screen
screenSize = width, height = 600,600
screenColor = (150, 150, 255)
screen = pygame.display.set_mode(screenSize)
ballImage = pygame.image.load("ball.bmp")
ball = ballImage.get_rect()
strength = 10
weight = 10
"""
strength = strength * 5
weight = weight * 5
power = (strength - weight) +10
"""

power = (strength / float(weight))**2 *10


if power < 10:
	power = 10
topSpeed = strength
ballPos = [-25,-20]		#to account for mouse position
speed = (0, 0) 
while (1): #50% accel to mouse, 50% current direction
	msPos = list(pygame.mouse.get_pos())
	accelToMouse = [msPos[0] - ballPos[0], msPos[1] - ballPos[1]]
	topAcc = getMagnitude(accelToMouse) * (power/10)
	topSpeed = getMagnitude(accelToMouse) #cant be increased because it would lead to spinning
	if topSpeed > power:
		topSpeed = power
	accelToMouse = setMagnitude(accelToMouse, topAcc)
	speed = [speed[0] + accelToMouse[0], speed[1] + accelToMouse[1]]
	speed = setMagnitude(speed, topSpeed)
	ball= ball.move(speed)
	ballPos = [ballPos[0] + speed[0], ballPos[1] + speed[1]]
	
	#UPDATE SCREEN
	screen.fill(screenColor)
	screen.blit(ballImage, ball)
	pygame.display.flip()
	events=pygame.event.get()
	#CHECK FOR EXIT
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
	pygame.time.delay(30) 
print("Done!")

#ball.move(xspeed, yspeed)
pygame.time.delay(100)             #stop the program for 1/10 second
