def main():
    groceries = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Lemons']
    
    myList = []
    myList.append('Chips')
    
    print(groceries[0:])
    
    newG = groceries[1:3]
    print(newG)
    
    #adding
    groceries.append('Chips')
    groceries.insert(3,'cookies')
    print(groceries)
    
    x = groceries.pop()
    print(x)
    print(groceries)
    
    #mutable, can be changed
    groceries[2] = 'ZZZZZZZZZZZZZZZZ'
    print(groceries)
    
    finalGroc = tuple(groceries)
    print(finalGroc)
    finalGroc[1] = 'ZZZZZZZ'
    
     
main()