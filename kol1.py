#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

class Bank(object):

	def __init__(self):
		self.clients = [];
	def addClient(self, client):
		self.clients = [self.clients, client]
	def transfer(self, clientFrom, clientTo, value):
		if(value>=0 and clientFrom.cash >= value):
			clientFrom.withdraw(value)
			clientTo.input(value)

class Client(object):
	def __init__(self, name):
		self.cash = 0
		self.name = name
	def input(self, value):
		if value>0:
			self.cash = self.cash + value
	def withdraw(self, value):
		if value<self.cash:
			self.cash = self.cash - value
			return value

client1 = Client("jeden")
client2 = Client("dwa")
bank = Bank()
bank.addClient(client1)
bank.addClient(client2)
client1.input(2)
client1.withdraw(3)
bank.transfer(client1, client2, 1)
print("Client 1 cash: ")
print(client1.cash)
print("Client 2 cash: ")
print(client2.cash)
client3 = Client("trzy")
bank.addClient(client3)
bank.transfer(client1, client3, 1)
print("Client 3 cash: ")
print(client3.cash)
client3.withdraw(0.5)
print("Client 3 cash after withdraw: ")
print(client3.cash)
		
