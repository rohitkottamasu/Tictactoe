import sys
board1 = [['00','01','02'],['10','11','12'],['20','21','22']]
for i in range(3):
        	for j in range(0,3):
        		sys.stdout.write("%s | " % board1[i][j])
        	print "\n-------------"
