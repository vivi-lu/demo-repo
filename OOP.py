class Item:
    pay_rate = 0.8 # Pay rate after 20% discound
    all = []
    def __init__(self, name: str, price: float, quantity=0): #"self" is alwys calling instance so for example here "item1" once it is created
        # Run validation to received arguments
        assert price >= 0, f"Price {price} is not greater than or euqal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or euqal to zero!"

        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discound(self):
        self.price = self.price * self.pay_rate # hier geht "pay_rate" nicht, da ich immer mit "irgendwas.pay_rate" aufrufen muss 
        # auch "Item.pay_rate"ist nicht so ne gute Idee, da es dann immer bei 80% bleibt auch wenn ich unten was ändern würde, weil es zuerst auf class und ann instance level sucht

    '''
    item1 = Item("Phone", 100, 1)
    item1.apply_discound()
    print(item1.price)

    item2 = Item("Laptop", 1000, 3)
    item2.pay_rate = 0.7
    item2.apply_discound()
    print(item2.price)'''

    @classmethod
    def instantiate_from_csv(cls):


    def __repr__(self): #repr = representing your objects
        return f"Item ('{self.name}', {self.price}, {self.quantity})" # return them the same way as created for best practice - easier to identify now 
       
'''
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


for instance in Item.all:
    print(instance.name)
''' # to print all names mit for loop. Instance is Platzhalter und "all =[]" hab ma oben definiert auch unten weiter mit "appand", dass ma immer wieder anhängen mit self

print(Item.all)

