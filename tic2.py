#tic-tac-toe
import sys
board=[]
board1 = [['00','01','02'],['10','11','12'],['20','21','22']]
p=0

def print1():
	for i in range(3):
        	for j in range(3):
        		sys.stdout.write("%s | " % board[i][j])
        	print "\n-------------"

def positions():    
	board1 = [['00','01','02'],['10','11','12'],['20','21','22']]
	for i in range(3):
        	for j in range(3):
        		sys.stdout.write("%s | " % board1[i][j])
        	print "\n-------------"
                           
def game(st,c):
	for i in range(3):
		for j in range(3):
			if(board[i][j]==st):
				board[i][j] = c	
	
def emptycheck():
	for i in range(3):
		for j in range(3):
			if (board[i][j] == str(i)+str(j)):
				p=1
	return p      

def win():
	if board[0]=='x' or board[1]=='x' or board[2]=='x':
		print("Player1 wins")
	elif board[0]=='o' or board[1]=='o' or board[2]=='o': 
		print("Player2 wins")		
  
        elif board[0][0]=='x' and board[1][1]=='x' and board[2][2]=='x':
		print("Player1 wins")
	elif board[0][0]=='o'and board[1][1]=='o' and board[2][2]=='o':
		print("Player2 wins")
	elif board[0][2]=='x' and board[1][1]=='x' and board[2][0]=='x':	
		print("Player1 wins")
	elif board[0][2]=='o'and board[1][1]=='o' and board[2][0]=='o':
		print("Player2 wins")
  
def input():
	print('player1-x')
	print('player2-o')




print("CURRENT BOARD:-")
positions()

i=1
while i!=0 and emptycheck():
	if(i%2!=0):
		print("player1 turn:")
		a=raw_input("Enter the position")
		game(a,'x')
		
	else:
		print("player2 turn:")
		a=raw_input("Enter the position")
		game(a,'o')

i=i+1
win() 
	




