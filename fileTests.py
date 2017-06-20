import time
import os 

counter = 0

while True:
	counter = counter + 1	
	text = input('Enter Text: ')
	print('Lines completed:', counter)
	with open('test.txt', 'a') as file: 
		file.write(text + '\n')	

