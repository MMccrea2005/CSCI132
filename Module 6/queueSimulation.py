import random
from pythonds3.basic import Queue

class Register:
    def __init__(self, ipm):
        self.item_rate = ipm
        self.current_customer = None
        self.time_left = 0
        
    def tick(self):
        if self.current_customer is not None:
            self.time_left = self.time_left - 1
            if self.time_left <= 0:
                self.current_customer = None
    def busy(self):
        return self.current_customer is not None
    
    def start_next_customer(self, newCustomer):
        self.current_customer = newCustomer
        self.time_left= newCustomer.get_items() * 60 / self.item_rate
        
class Customer:
    def __init__(self, time):
        self.timestamp = time
        self.items = random.randrange(1, 21) #Customer can have up to twenty items
    
    def get_timestamp(self):
        return self.timestamp
    
    def get_items(self):
        return self.items
    
    def wait_time(self, current_time):
        return current_time - self.timestamp

def simulation(seconds, items_per_minute):
    simRegister = Register(items_per_minute)
    cusQueue = Queue()
    waitingTimes = []
    
    for current_second in range(seconds):
        if new_Customer():
            customer = Customer(current_second)
            cusQueue.enqueue(customer)
            
        if (not simRegister.busy()) and (not cusQueue.is_empty()):
            nextCustomer = cusQueue.dequeue()
            waitingTimes.append(nextCustomer.wait_time(current_second))
            simRegister.start_next_customer(nextCustomer)
            
        simRegister.tick()
    average_wait = sum(waitingTimes) / len(waitingTimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, cusQueue.size()))


    
    
def new_Customer():
    num = random.randrange(1,121) # One customer showing up every two minutes on average
    return num == 120 

for i in range(10):
    simulation(3600, 12) #Using just one hour, with employee scanning an item every five seconds. seems slow but is also to account for big and heavy itmes