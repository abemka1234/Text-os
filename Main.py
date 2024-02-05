import keyboard
import colorama
import time
import os
#-----------------------Подсказка---------------------------------
#[0,0]-- первое число y, второе x,y МИНУСОВОЙ
#----------------------ANSI-GRAPHIC-------------------------------
c = ""
symbols={}
opened_windows =[]
nower_window = ''
def Start_P(symbols):
	for i in range(31):
		for b in range(120):
			symbols[i,b] = " "
def P_S(c,symbols):
	for i in range(31):
		for b in range(120):
			c += symbols[i,b]
		print(c)
		c =""
def Window(symbols):
    for b in range(120):
        symbols[0,b] = colorama.Back.RED+' '+colorama.Style.RESET_ALL
    for d in range(120):
        symbols[30,d] = colorama.Back.RED+' '+colorama.Style.RESET_ALL
    for i in range(31):
        symbols[i,0] = colorama.Back.RED+' '+colorama.Style.RESET_ALL
    for e in range(31):
        symbols[e,119] = colorama.Back.RED+' '+colorama.Style.RESET_ALL
#-------------------------OS----------------------------------------------
def start_up(c,symbols):
	Start_P(symbols)
	Window(symbols)
	symbols[15,62] = "S"
	symbols[15,61] = "O"
	symbols[15,59] = "T"
	symbols[15,58] = "X"
	symbols[15,57] = "E"
	symbols[15,56] = "T"
	P_S(c,symbols)
	time.sleep(5)
	for i in range(4):
		symbols[i+18,57] = colorama.Back.WHITE+' '+colorama.Style.RESET_ALL
	for i in range(4):
		symbols[i+18,60] = colorama.Back.WHITE+' '+colorama.Style.RESET_ALL
	for i in range(2):
		symbols[21,i+58] = colorama.Back.WHITE+' '+colorama.Style.RESET_ALL
	for i in range(2):
		symbols[18,i+58] = colorama.Back.WHITE+' '+colorama.Style.RESET_ALL

	for i in range (20):
		symbols[19,59] = ' '
		symbols[20,58] = ' '
		symbols[19,58] = colorama.Back.RED+' '+colorama.Style.RESET_ALL
		symbols[20,59] = colorama.Back.RED+' '+colorama.Style.RESET_ALL
		os.system('cls')
		P_S(c,symbols)
		time.sleep(0.1)
		symbols[19,58] = ' '
		symbols[20,59] = ' '
		symbols[19,59] = colorama.Back.RED+' '+colorama.Style.RESET_ALL
		symbols[20,58] = colorama.Back.RED+' '+colorama.Style.RESET_ALL
		os.system('cls')
		P_S(c,symbols)
		time.sleep(0.1)
	Start_P(symbols)
	os.system('cls')
def open_desktop(symbols,nover_window):
	Window(symbols)
	symbols[0,112] = "D"
	symbols[0,113] = "E"
	symbols[0,114] = "S"
	symbols[0,115] = "K"
	symbols[0,116] = "T"
	symbols[0,117] = "O"
	symbols[0,118] = "P" 
def start_desktop(symbols):
	open_desktop(symbols,nower_window) 
	P_S(c,symbols)
	time.sleep(5)
start_up(c,symbols)
start_desktop(symbols)
m_coord = [16,59]
run = True
while run == True:
	open_desktop(symbols,nower_window) 
	if keyboard.is_pressed('W') == True:
		if m_coord != [0,[0-120]]:
			m_coord[0] -= 1
	if keyboard.is_pressed('S') == True:
		if m_coord != [31,[0-120]]:
			m_coord[0] += 1
	if keyboard.is_pressed('D') == True:
		if m_coord != [[0-31],120]:
			m_coord[1] += 1
	if keyboard.is_pressed('A') == True:
		if m_coord != [[0-31],0]:
			m_coord[1] -= 1
	m_y_coord = m_coord[0]
	m_x_coord = m_coord[1]
	symbols[m_y_coord,m_x_coord] = colorama.Back.WHITE+' '+colorama.Style.RESET_ALL
	symbols[15,5] = "B"
	if m_coord == [15,5] and keyboard.is_pressed('E') == True:
		os.system('cls')
		print("""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""")
		print("I RICKROLLED YOU >:)")
		time.sleep(10)
	P_S(c,symbols)
	time.sleep(0.1)
	os.system('cls')
	Start_P(symbols)