import threading

class BankAccount(object):
    balance = int()
    isopen = False
    lock = threading.Lock()
    
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        if self.isopen == False:
            raise ValueError("Can't access closed account.")
        else:
            return self.balance

    def open(self):
        if self.isopen == True:
            raise ValueError("Account already opened.")
        else:
             self.isopen = True
            

    def deposit(self, amount):
        
        if self.isopen == False:
            raise ValueError("Can't access closed account.")
        elif amount < 0:
            raise ValueError ("Invalid amount.")
        else:
            self.lock.acquire()
            self.balance += amount
            self.lock.release()

    def withdraw(self, amount):
        if self.isopen == False:
            raise ValueError("Can't access closed account")
        elif amount < 0:
            raise ValueError("Invalid amount.")
        elif amount > self.balance:
            raise ValueError ("Not possible to withdraw more money than you have in your account.")
        else:
            self.lock.acquire()
            self.balance -= amount
            self.lock.release()

    def close(self):
        if self.isopen == False:
            raise ValueError ("No open account.")
        else:
            self.isopen = False
            self.balance = 0
