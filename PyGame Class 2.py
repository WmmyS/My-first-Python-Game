import pygame
import random
pygame.init()
pygame.mixer.init()

"""Este é o meu primeiro joguinho em python, a lógica contida neste código não foi criada por mim, porém todas
as alterações e desenhos foram. O projeto inicial foi criado a partir do tutorial do Youtube no canal: Eletrônica e Programação,
o link da primeira aula é : https://www.youtube.com/watch?v=ddgppBdhVn8.
	Todo o conteúdo desse código é para fins didáticos e será colocado em meu portifólio para apresentação e futuras atualizações,
caso queiram testar e sugerir alterações fiquem a vontade. :) """

"""This is my first litle game in python language, the logic in this code was not created by me,but the all
changes and drawings were. The initial project was created starting of the tutorial on Youtube chanel: Eletrônica e Programação,
the link of the first class is: https://www.youtube.com/watch?v=ddgppBdhVn8.
	All content of this code is for didactic purposes and will be placed in my portifolio to apresentation and updates in the future,
if you want test and sugest changes fells free :)"""

clock = pygame.time.Clock()

tireSound = pygame.mixer.Sound('tiresound2.wav')
crash = pygame.mixer.Sound('batida.wav')
pygame.mixer.music.load('paranoid.mp3')
pygame.mixer.music.load('paranoid.mp3')
pygame.mixer.music.play(-3)

"""Tentativa de implementação na fica e no som das batidas (ainda em desenvolvimento)"""

def crashc(y1,x1,y,x,crash):
	if ((y1 in range(y1 + 80) and (x1 in range(x1 + 80)))) == ((y in range(y+80)) and (x in range(x+80))):
		crash.play()

"""Nesta parte inserimos o timer e suas fontes e modelos (futuras alterações)"""

font = pygame.font.SysFont('Cooper Black', 25)
text = font.render("Time: 0",True,(255,150,0),(0,0,0))
pos_text = text.get_rect()
pos_text.center = (50,50)

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("CarGame")

x = 360
y = 330
POS_others_Y1 = -20
POS_others_Y2 = -20
POS_others_Y3 = -20
local = 0
screenmove = 0
timer = 0
time_second = 0

roads = [230,380,520]
random.seed()
POS_others_X1 = random.choice(roads)
POS_others_X2 = random.choice(roads)
POS_others_X3 = random.choice(roads)
speeds = [15, 20, 18, 23]
random.seed()
SpeedCar1 = random.choice(speeds)
SpeedCar2 = random.choice(speeds)
SpeedCar3 = random.choice(speeds)
turn = 10
options = ['Carro Azul.png','Carro Vermelho.png','Carro Amarelo.png','Carro Laranja.png', 'Carro Preto.png']
random.seed()
vehicle = random.choice(options)
screen = pygame.image.load('Estrada Longa.png')
car = pygame.image.load('Carro.png')
others1 = pygame.image.load(vehicle)
others2 = pygame.image.load(vehicle)
others3 = pygame.image.load(vehicle)

"""A partir de agora está é a jenela de execução do código, nesta janela irão ser repetidas as transições de
quadros e feitas as alterações respectivamente de acordo com as condições e alterações das variáveis"""

window_open = True
while window_open:
	pygame.time.delay(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			window_open = False

	comands = pygame.key.get_pressed()

	car = pygame.image.load('Carro.png')
	
	#crashc(POS_others_Y1,POS_others_X1,y,x,crash)

	if comands [pygame.K_UP] and y >= 20:
		y -= turn
	if comands [pygame.K_DOWN] and y <= 440:
		y += turn
	if comands [pygame.K_RIGHT] and x <= 550:
		x += turn
		tireSound.play()
		tireSound.fadeout(100)
		car = pygame.image.load('Carro R2.png')
	if comands [pygame.K_LEFT] and x >= 200:
		x -= turn

		tireSound.play()
		tireSound.fadeout(100)
		car = pygame.image.load('Carro L1.png')


	if POS_others_Y1 > 620:
		roads = [220, 210, 240, 230, 250]
		POS_others_Y1 = (-250)
		random.seed()
		POS_others_X1 = 230
		random.seed()
		vehicle = random.choice(options)
		speeds = [15, 20, 18, 23]
		random.seed()
		SpeedCar1 = random.choice(speeds)
		others1 = pygame.image.load(vehicle)
		pygame.display.update()

	if POS_others_Y2 > 620:
		roads = [360, 370, 380, 390, 400]
		POS_others_Y2 = (-250)
		random.seed()
		POS_others_X2 = random.choice(roads)
		random.seed()
		vehicle = random.choice(options)
		speeds = [15, 20, 18, 23]
		random.seed()
		SpeedCar2 = random.choice(speeds)
		others2 = pygame.image.load(vehicle)
		pygame.display.update()

	if POS_others_Y3 > 620:
		roads = [510, 530, 520, 540, 550]
		POS_others_Y3 = (-250)
		random.seed()
		POS_others_X3 = random.choice(roads)
		random.seed()
		vehicle = random.choice(options)
		speeds = [15, 20, 18, 23]
		random.seed()
		SpeedCar3 = random.choice(speeds)
		others3 = pygame.image.load(vehicle)
		pygame.display.update()

	if (POS_others_X1 == POS_others_X2) and ((POS_others_Y1 in range(POS_others_Y2 + 100)) or (POS_others_Y1 in range(POS_others_Y2 + 80))):
		random.seed()
		POS_others_Y2 = (POS_others_Y1 - 200)

	if (POS_others_X2 == POS_others_X3) and ((POS_others_Y2 in range(POS_others_Y3 + 100)) or (POS_others_Y2 in range(POS_others_Y3 + 80))):
		random.seed()
		POS_others_Y3 = (POS_others_Y1 - 200)

	if (POS_others_X1 == POS_others_X3) and ((POS_others_Y1 in range(POS_others_Y3 + 100)) or (POS_others_Y1 in range(POS_others_Y3 + 80))):
		random.seed()
		POS_others_Y3 = (POS_others_Y2 - 200)

	if (timer<20):
		timer += 1
	else:
		time_second += 1
		text = font.render("Time: "+str(time_second),True,(255,150,0),(0,0,0))
		timer = 0

	POS_others_Y1 += SpeedCar1
	pygame.display.update()
	POS_others_Y2 += SpeedCar2
	pygame.display.update()
	POS_others_Y3 += SpeedCar3
	pygame.display.update()
	#number = (0, -500, -400, -300, -200)
	

	screenmove -= 50

	if screenmove == -600:
		screenmove = 0

	window.blit(screen, (0,screenmove))
	window.blit(car, (x, y))
	window.blit(others1, (POS_others_X1, POS_others_Y1))
	window.blit(others2, (POS_others_X2, POS_others_Y2))
	window.blit(others3, (POS_others_X3, POS_others_Y3))
	window.blit(text, pos_text)

	pygame.display.update()