#!/usr/bin/env python3
from lib import wait_key as getch;
from lib import go_up

tesbih = ("SubhanAllah", "Elhamdülillah", "Allahuekber");

def main():
	for soyle in tesbih:
		for i in range(0,33):
			print(str(i+1)+":\t"+soyle);
			go_up();
			getch();
			print(" " * (len(str(i+1)+":\t"+soyle)+4));
			go_up();

if __name__ == '__main__':
	main();
