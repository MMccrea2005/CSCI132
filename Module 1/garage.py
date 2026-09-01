class Garage:
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.occupied = 0
        
    def getoccupied(self):
        return self.occupied
    
    def enter(self):
        if self.occupied == self.cap:
            print('ERROR - we are full')
        else:
            self.occupied +=1
        
    def exit(self):
        self.occupied -=1
        
    def isFull(self):
        return self.occupied == self.cap
        
def main():
    g = Garage('Main St Garage', 3)
    
    g.enter()
    g.enter()
    g.enter()
    g.exit()
    print(g.isFull())


main()