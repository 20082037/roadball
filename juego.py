import os
import time
import sys
from Tkinter import *
from PIL import ImageTk, Image
from time import sleep

class juego(object):

	def __init__(self):
		global estadoJuego
		estadoJuego='juego'
		self.roadBall=Toplevel()
		juego.nivel=1
		self.mapA=mapa(self.roadBall,self.nivel) #Crea el mapa para comenzar la partida
		self.movimiento="no"	
		self.ball=jugador(self.roadBall,self.mapA.canvas,self.mapA.mapaActual,self.movimiento,self.nivel)
		self.roadBall.after(0,self.update)		
	
	def creditos (self,canvas):
		canvas.create_text(750,550,text="Creditos:",anchor=CENTER,font=("none",40),fill='white')
		canvas.create_text(800,600,text="Juan De La Roca",anchor=CENTER,font=("none",25),fill='white')
		canvas.create_text(800,630,text="Alejandra Gonzales",anchor=CENTER,font=("none",25),fill='white')
		canvas.create_text(800,660,text="Wendy Taya",anchor=CENTER,font=("none",25),fill='white')	
		#for i in range(50):	
		#	canvas.move("Creditos:",0,-20)
		#	canvas.pack()
		self.roadBall.mainloop()

		
	def update(self):
		global estadoJuego
		print estadoJuego
		if estadoJuego=='gano':
			if self.nivel==5:
				self.mapA.canvas.delete('all')
				self.mapA.canvas.destroy()
				self.mapA.canvas=Canvas(self.roadBall,width=1024,height=768,background='white')			
				self.mapA.canvas.ganaste = ImageTk.PhotoImage(Image.open('ganastefinal.jpg'))
				self.mapA.canvas.create_image(0,0, anchor=NW,image=self.mapA.canvas.ganaste)
				self.mapA.canvas.pack()
				sleep(2)
				self.creditos(self.mapA.canvas)								
			
			else: 	
				self.nivel= self.nivel+1
				estadoJuego='juego'
				self.mapA.canvas.delete('all')
				self.mapA.canvas.destroy()
				self.mapA.__init__(self.roadBall,self.nivel)
				self.ball.__init__(self.roadBall,self.mapA.canvas,self.mapA.mapaActual,self.movimiento,self.nivel)
		elif estadoJuego=='perdio':
			estadoJuego='juego'
			self.mapA.canvas.delete('all')
			self.mapA.canvas.destroy()
			self.mapA.__init__(self.roadBall,self.nivel)
			self.ball.__init__(self.roadBall,self.mapA.canvas,self.mapA.mapaActual,self.movimiento,self.nivel)

		self.roadBall.after(10,self.update)


class mapa(object):
	
	def __init__(self,roadBall,nivel):
		
		#Ingresa todos los mapas que usaremos en el juego
		self.map1= ["+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+",
      			    "+2 2           2 2 2             2 2   2+",
       			    "+2 2             S                 2   2+",
		            "+2                           2     2   2+",     
			    "+2         2                       2   2+",     
       			    "+2   2 2 2 2             2         2   2+",     
		            "+2     2     2 2       2   2       2   2+",     
       			    "+2   2 I 1   2 2         2   2 2 2 2   2+",     
       			    "+2     2     2 2   2 2  22           I 2+",
 		            "+2   2          2        2         2 2 2+",     
      			    "+2           2 222   2   2     2   2 2 2+",
      			    "+2       2      2        2 2       2 2 2+",
       		 	    "+2     2 2             222         2 2 2+",
       			    "+2 2   2           2     2         2   2+",
       			    "+2     2   2      2      2     2       2+",
       			    "+2 2        2     2      2         2   2+",
       			    "+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+"]

		self.map2=["+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+",
		           "+2 2                                 2             2 2 2 2+", 
       			   "+2 2   2                             2       2       2 2 2+",
       			   "+2   2   2            2              2     2 2     2     2+",
       			   "+2         2           2 2           2 2 2       2   2   2+",
       			   "+2     2 2       2           2       2   2     2     2   2+",
       			   "+2   2                       2       2   2   2       2   2+",
      			   "+2 2                             2   2   I          S2 2 2+",
		           "+2 2              22     2 2                             2+",
       			   "+2 2             2     I           2                     2+",
       			   "+2               2   2         2                     2   2+",
       			   "+2   2   2     2       2   2                             2+",
       			   "+2     2                             2                   2+",
       			   "+2       2 2        2    2   2     2 2 2           2     2+",
       			   "+2       2 2                         2     2       2     2+",
       			   "+2 2             2       2       2                       2+",
       			   "+2       2     2       2   2 2     2     2   2 2         2+",
       			   "+2     2           2  12   2 2   2   2       2 2 2       2+",
       			   "+2 2 2      2          2 2         2   2             2 2 2+",
       			   "+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+"]

		self.map3=["+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+",
		           "+2 2 2 2 2 2 2 2 2 2 2                                          +",
       			   "+2       2  2  2       2 2                                S2    +",
       			   "+2               2     2 2 2           2                   I    +",
       			   "+2 2       2               2 2                                  +",
       			   "+2    2    2 2   I           2 2         2   2                  +",
       			   "+2                   2222      2 2 2 2   2     2         2      +",
       		      	   "+2         2                 2           2   2                  +",
       			   "+2       2                 2   2                                +",
       			   "+2         2   2         2       2   2                          +",
       			   "+2             2         2                                      +",
       			   "+2 2                22 2                                   2    +",
       			   "+2                22         2 2                                +",
       			   "+2  22   2   2  22                     2 2                 2 2  +",
       			   "+2 2   2   2   2       2 2                   2 2           2 2  +",
       			   "+2                                         2   2                +",
       			   "+2               2     2               222   2 2                +",
       			   "+2             2               2                                +",
       			   "+2                       2         2 2                          +",
       			   "+21  2       2           2       2 2                           2+",
       			   "+2 2 2           2                                         2    +",
       			   "+2 2 2 2                                  2                2    +",
       			   "+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+",]

		self.map4=["+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
		           "+2   1       2 22  22 2                                  22222   +",
			   "+   2                                                        2   +",
 			   "+   2           22                                           2   +",
 			   "+  22 22222222222222         22             2222             2   +",
 			   "+  22          2           2 2                              I2  2+",
 			   "+  22                                        2                   +",
			   "+  22222222222222222                         2222                +",
 			   "+      2222222222222                                             +",
 			   "+    222222222222222   2   S                                     +",
			   "+           22 22      22  22                                    +",
			   "+                     2    22                                    +",
			   "+ 2                  2222222                                     +",
			   "+  22222            22                                      S    +",
			   "+  222        22  22          2                            222   +",
			   "+2222222222222222222222222222222222222222222222222222222222222222+",
			   "+  I  22       2           2 2                             222   +",
			   "+2            2                    22 2 2 2 2       2      222   +",
			   "+              2        2                           2       2    +",
			   "+   2                  22 2                         2    S       +",
			   "+2  22                  2           2             2              +",
			   "+2  2222                   2                 2    2          222 +",
			   "+2  2222222                2                2222  22             +",
			   "+2  2222                  22                222   2222           +",  
			   "+2  222       2         S                   22222     2222222    +",
			   "+22  2        22    2                        222  22222222222    +",
			   "+22    22                                    2222222222222222    +",
			   "+22     22 22222       2  22222                 22               +",
			   "+          2    2 22 22    2222                   2              +",
			   "+22 S2222222222222222    2 2222                    2      2222222+",
			   "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"]

		self.map5= ["+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
		            "+                               S                     S         +",
			    "+        2                                       2              +",
			    "+  2                    2                            2          +",
			    "+                                             2                 +",
			    "+                                                 2        2    +",
			    "+  2                         S            2         2           +",
			    "+         2                                    2            2   +",
			    "+                                     2                      2  +",
			    "+                                          2                  I +",
			    "+        2                             2                       S+",
			    "+ 2            2       2                                        +",
			    "+                                                               +",
			    "+                                                  2            +",
			    "+   2               22S2222222222222S22222222             2     +",
			    "+         2         2                       2                   +",
			    "+                   2   222222S2222222222   2                  2+",
			    "+                   2   2               2   2       2           +",
			    "+                   2   2   2222222222  2   S                   +",
			    "+                   2   S   2        2  2   2                   +",
			    "+        2          2   2   2        I  2   2                   +",
			    "+  2                2   2   22222222 2  2   2    s              +",
			    "+                   2   2            2  S   2        2          +",
			    "+                   2   22222222222222  2   S               222 +",  
			    "+         2         2                   2   2               22  +",
			    "+    2              222222222222222222222   2        2          +",
			    "+         2                                 2        2        S +",
			    "+ 2                                         2        2        2 +",
			    "+     2       222S222222222S2222S2222S2222222        2222222  2 +",
			    "+1 2                                                            +",
			    "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"] 
		
		#Elige el mapa que proyectara dependiendo del nivel en el que se encuentre el jugador
		if (nivel==1):
			self.mapaActual=self.map1
		elif (nivel==2):
			self.mapaActual=self.map2
		elif (nivel==3):
			self.mapaActual=self.map3
		elif (nivel==4):
			self.mapaActual=self.map4
		elif (nivel==5):
			self.mapaActual=self.map5

		self.canvas=Canvas(roadBall,width=20*len(self.mapaActual[0]),height=20*len(self.mapaActual),background='white') #Definir ancho y largo en funcion al mapa
		roadBall.title('Road Ball')
		#self.canvas.pack()	

		# Carga todas las imagenes para poder proyectarlas

		self.canvas.ball = ImageTk.PhotoImage(Image.open('ball.png').resize((20,20),Image.ANTIALIAS))
		self.canvas.ladrillo = ImageTk.PhotoImage(Image.open('bricks.jpg').resize((20,20),Image.ANTIALIAS))
		self.canvas.portal = ImageTk.PhotoImage(Image.open('portal.jpg').resize((20,20),Image.ANTIALIAS))
		self.canvas.puerta = ImageTk.PhotoImage(Image.open('puerta.png').resize((20,20),Image.ANTIALIAS))

		#Proyecta el mapa
		for fila in range(len(self.mapaActual)):
			for columna in range(len(self.mapaActual[fila])):
				if (self.mapaActual[fila][columna]==' '): # si el valor de la posicion es 0 sera un lugar vacio		
					self.canvas.create_rectangle(20 * columna , 20 * fila , 20 * columna + 20, 20 * fila + 20,
                    outline='white', fill='white')						
				if (self.mapaActual[fila][columna]=='1'): # si el valor de la posicion es 0 sera un lugar vacio		
					self.canvas.create_rectangle(20 * columna , 20 * fila , 20 * columna + 20, 20 * fila + 20,
                    outline='white', fill='black')						
				elif (self.mapaActual[fila][columna]=='2'):# si el valor de la posicion es 0 sera una pared normal
					self.canvas.create_image(20 * columna , 20 * fila , anchor=NW,image=self.canvas.ladrillo)
				elif (self.mapaActual[fila][columna]=='I'):# si el valor de la posicion es 0 sera una pared normal
					self.canvas.create_image(20 * columna , 20 * fila , anchor=NW,image=self.canvas.portal)
				elif (self.mapaActual[fila][columna]=='S'):# si el valor de la posicion es 0 sera una pared normal
					self.canvas.create_image(20 * columna , 20 * fila , anchor=NW,image=self.canvas.puerta)



		self.canvas.pack()

class jugador(object):
	
	def __init__(self,roadBall,canvas,mapa,movimiento,nivel):

		self.movimiento=movimiento

		#Insertar reconocedor de eventos del teclado		
		roadBall.bind("<Key>",lambda event,arg=canvas,arg1=mapa,arg2=nivel:self.key(event,arg,arg1,arg2))
		roadBall.focus_set()

		canvas.ball = ImageTk.PhotoImage(Image.open('ball.png').resize((20,20),Image.ANTIALIAS))
		
		#Buscar jugador y dibujarlo
		for fila in range(len(mapa)):
			for columna in range(len(mapa[fila])):		
				if (mapa[fila][columna]=='1'): # si el valor de la posicion es 1 es el jugador
					print mapa[fila][columna] 		
					self.ball=canvas.create_image(20 * columna , 20 * fila , anchor=NW,image=canvas.ball)
					canvas.pack()
					break

	def movUp(self,canvas,mapa,nivel):
		global estadoJuego				
		while self.movimiento=="up":
			if (mapa[int(canvas.coords(self.ball)[1]/20)-1][int(canvas.coords(self.ball)[0]/20)]==' ' or mapa[int(canvas.coords(self.ball)[1]/20)-1][int(canvas.coords(self.ball)[0]/20)]=='1'):
				print self.movimiento				
				canvas.move(self.ball, 0, -20)
				canvas.update()
				sleep(0.025)
			elif (mapa[int(canvas.coords(self.ball)[1]/20)-1][int(canvas.coords(self.ball)[0]/20)]=='I'): 
				canvas.move(self.ball, 0, -20)
				canvas.update()				
				portalx=0
				portaly=0
				count=0
				for i in range(len(mapa)):
					for j in range(len(mapa[i])):
						if (mapa[i][j]=='I' and (int(canvas.coords(self.ball)[1]/20)!=i and int(canvas.coords(self.ball)[0]/20)!=j)and count==0):
							portalx=j
							portaly=i
							count+=1				
				print portalx , portaly			
				canvas.move(self.ball,portalx*20-canvas.coords(self.ball)[0],portaly*20-canvas.coords(self.ball)[1])
				canvas.update()
				sleep(0.1)

			elif (mapa[int(canvas.coords(self.ball)[1]/20)-1][int(canvas.coords(self.ball)[0]/20)]=='S'): 			
				canvas.move(self.ball, 0, -20)
				canvas.update()								
				estadoJuego='gano'
				sleep(2)
				self.movimiento="no"
			elif (mapa[int(canvas.coords(self.ball)[1]/20)-1][int(canvas.coords(self.ball)[0]/20)]=='+'): 			
				canvas.move(self.ball, 0, -20)
				canvas.update()								
				estadoJuego='perdio'
				sleep(2)
				self.movimiento="no"

			else:self.movimiento="no"

	def movRight(self,canvas,mapa,nivel):
		global estadoJuego				
		while self.movimiento=="right":
			if (mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)+1]==' ' or mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)+1]=='1'):
				print self.movimiento				
				canvas.move(self.ball, 20, 0)
				canvas.update()
				sleep(0.025)			
			elif (mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)+1]=='I'): 
				canvas.move(self.ball, 20, 0)
				canvas.update()				
				portalx=0
				portaly=0
				count=0
				for i in range(len(mapa)):
					for j in range(len(mapa[i])):
						if (mapa[i][j]=='I' and (int(canvas.coords(self.ball)[1]/20)!=i or int(canvas.coords(self.ball)[0]/20)!=j)and count==0):
							portalx=j
							portaly=i
							count+=1				
				print portalx , portaly			
				canvas.move(self.ball,portalx*20-canvas.coords(self.ball)[0],portaly*20-canvas.coords(self.ball)[1])
				canvas.update()
				sleep(0.1)

			elif (mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)+1]=='S'): 			
				canvas.move(self.ball, 20, 0)
				canvas.update()								
				estadoJuego='gano'
				sleep(2)
				self.movimiento="no"
			elif (mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)+1]=='+'): 			
				canvas.move(self.ball, 20, 0)
				canvas.update()								
				estadoJuego='perdio'
				sleep(2)
				self.movimiento="no"

			else:self.movimiento="no"

	def movLeft(self,canvas,mapa,nivel):
		global estadoJuego				
		while self.movimiento=="left":
			if (mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)-1]==' ' or mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)-1]=='1'):
				print self.movimiento				
				canvas.move(self.ball, -20, 0)
				canvas.update()
				sleep(0.025)
			elif (mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)-1]=='I'): 
				canvas.move(self.ball, -20, 0)
				canvas.update()				
				portalx=0
				portaly=0
				count=0
				for i in range(len(mapa)):
					for j in range(len(mapa[i])):
						if (mapa[i][j]=='I' and (int(canvas.coords(self.ball)[1]/20)!=i or int(canvas.coords(self.ball)[0]/20)!=j)and count==0):
							portalx=j
							portaly=i
							count+=1				
				print portalx , portaly			
				canvas.move(self.ball,portalx*20-canvas.coords(self.ball)[0],portaly*20-canvas.coords(self.ball)[1])
				canvas.update()
				sleep(0.1)
	
			elif (mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)-1]=='S'): 			
				canvas.move(self.ball, -20, 0)
				canvas.update()								
				estadoJuego='gano'
				sleep(2)
				self.movimiento="no"
			elif (mapa[int(canvas.coords(self.ball)[1]/20)][int(canvas.coords(self.ball)[0]/20)-1]=='+'): 			
				canvas.move(self.ball, -20, 0)
				canvas.update()								
				estadoJuego='perdio'
				sleep(2)
				self.movimiento="no"


			else:self.movimiento="no"
	
	def movDown(self,canvas,mapa,nivel):
		global estadoJuego		
		while self.movimiento=="down":
			if (mapa[int(canvas.coords(self.ball)[1]/20)+1][int(canvas.coords(self.ball)[0]/20)]==' ' or mapa[int(canvas.coords(self.ball)[1]/20)+1][int(canvas.coords(self.ball)[0]/20)]=='1'):
				print self.movimiento				
				canvas.move(self.ball, 0, 20)
				canvas.update()
				sleep(0.025)
			elif (mapa[int(canvas.coords(self.ball)[1]/20)+1][int(canvas.coords(self.ball)[0]/20)]=='I'): 
				canvas.move(self.ball, 0, 20)
				canvas.update()				
				portalx=0
				portaly=0
				count=0
				for i in range(len(mapa)):
					for j in range(len(mapa[i])):
						if (mapa[i][j]=='I' and int(canvas.coords(self.ball)[1]/20)!=i and int(canvas.coords(self.ball)[0]/20)!=j and count==0): 
							portalx=j
							portaly=i
							count+=1
							print i, j				
				print portalx , portaly			
				canvas.move(self.ball,portalx*20-canvas.coords(self.ball)[0],portaly*20-canvas.coords(self.ball)[1])
				canvas.update()
				sleep(0.1)

			elif (mapa[int(canvas.coords(self.ball)[1]/20)+1][int(canvas.coords(self.ball)[0]/20)]=='S'): 			
				canvas.move(self.ball, 0, 20)
				canvas.update()								
				estadoJuego='gano'
				sleep(2)
				self.movimiento="no"

			elif (mapa[int(canvas.coords(self.ball)[1]/20)+1][int(canvas.coords(self.ball)[0]/20)]=='+'): 			
				canvas.move(self.ball, 0, 20)
				canvas.update()								
				estadoJuego='perdio'
				sleep(2)
				self.movimiento="no"

			else:self.movimiento="no"

	def key(self,event,canvas,mapa,nivel):
		if self.movimiento=="no":		
			if event.char == "w":
				self.movimiento="up"
				self.movUp(canvas,mapa,nivel)
			elif event.char == "a":
				self.movimiento="left"
				self.movLeft(canvas,mapa,nivel)
			elif event.char == "d":
				self.movimiento="right"
				self.movRight(canvas,mapa,nivel)
			elif event.char == "s":
				self.movimiento="down"
				self.movDown(canvas,mapa,nivel)
		print self.movimiento


def inicioJuego():
	global canvasInicio
	canvasInicio.destroy()
	canvasInicio=None
	a=juego()
		
	
inicio=Tk()

global estadoJuego
global canvasInicio
estadoJuego='juego'


canvasInicio=Canvas(inicio,width=600,height=300,background='white')
inicio.title('Road Ball')
canvasInicio.inicio= ImageTk.PhotoImage(Image.open('inicia3.jpg').resize((600,300),Image.ANTIALIAS))
#canvasInicio.nivel1= ImageTk.PhotoImage(Image.open('inicio.jpg').resize((600,300),Image.ANTIALIAS))
canvasInicio.create_image(0,0, anchor=NW,image=canvasInicio.inicio)
canvasInicio.create_text(300,150,text="ROAD BALL",anchor=CENTER,font=("none",50),fill='white')

button1= Button(inicio, text = "Iniciar juego", command = inicioJuego, anchor = NW)
button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
button1_window = canvasInicio.create_window(240, 180, anchor=NW, window=button1)

canvasInicio.pack()

inicio.mainloop()

