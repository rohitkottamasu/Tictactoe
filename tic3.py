#tic-tac-toe
import sys
board=[]
board1=[]

for x in range(3):
    board.append([])



for y in range(3):
    for z in range(3):
        board[y].append('.')

def print1():
	for i in range(3):
		for j in range(3):
				sys.stdout.write("%s |"%board[i][j])
		print("\n........")


def positions():
	
    
	for x in range(3):
        	board1.append([])

	board1[0].append('00')
        board1[0].append('01')
	board1[0].append('02')
	board1[1].append('10')
	board1[1].append('11')
	board1[1].append('12')
        board1[2].append('20')
        board1[2].append('21')
        board1[2].append('22')
        for i in range(3):
        	for j in range(3):
            		sys.stdout.write(" %s |"%board1[i][j])
        
                print "\n-------------"
   
                           


def game(i,j,c):
	if board[i][j]=='.':
		board[i][j]=c		
	

def emptycheck():
    p=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='.':
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
	print("CURRENT BOARD:")
	print1()
	print("\n")
	positions()

	i=1
	while i!=0 and emptycheck():
		if(i%2!=0):
			print("player1 turn:")
			a=int(raw_input("Enter the position:"))
			b=a%10
			c=a/10
			game(c,b,'x')
		
		else:
	                print("player2 turn:")
			a=int(raw_input("Enter the position:"))
			b=a%10
			c=a/10
			game(c,b,'o')
	
		i=i+1
		win() 
	




