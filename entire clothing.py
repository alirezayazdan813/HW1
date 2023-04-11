# Clothing class with aggregation and composition
class Clothing:
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell):
        self.size = size
        self.color = color
        self.brand = brand
        self.price = price

        self.zipper = Zip
        self.pocket = Pock
        self.buttons = Butt
        self.lining = Lin
        self.embellishments = Embell

        self.fabric = Fabric()
        self.thread = Thread()

    def get_zipper(self):
        return self.zipper.get_zip()
    
    def get_pocket(self):
        return self.pocket.get_pock()
    
    def get_button(self):
        return self.button.get_butt()
    
    def get_lining(self):
        return self.lining.get_lin()
    
    def get_embellishment(self):
        return self.embellishments.get_embell()
    
    def wash(self):
        print("Washing instructions: Machine wash cold, tumble dry low")
    
    def iron(self):
        print("Ironing instructions: Iron on low heat")

# Aggregation classes
class Zipper:
    def __init__(self, ziptype : bool):
        self.ziptype = ziptype
        self.length = 10
        self.color = 'silver'

    def zip_up(self):
        print("Zipper is now zipped up")
    
    def get_zip(self):
        if self.ziptype == True:
            print("The clothing have zipper")
        else :
            print("The clothing does not have zipper")

class Pocket:
    def __init__(self, pocktype : bool):
        self.pocktype = pocktype
        self.number_of_pockets = 2
        self.size = 'medium'

    def put_item(self):
        print("Item has been put in pocket")

    def get_pock(self):
        if self.pocktype == True:
            print("The clothing has pocket")
        else :
            print("The clothing does not have pocket")

class Buttons:
    def __init__(self, butttype : bool):
        self.butttype = butttype
        self.number_of_buttons = 5
        self.color = 'black'

    def add_button(self):
        print("A new button has been added")
    
    def get_butt(self):
        if self.butttype == True:
            print("The clothing has button")
        else :
            print("The clothing does not have button")

class Lining:
    def __init__(self, lintype : bool):
        self.lintype = lintype
        self.type = 'satin'
        self.color = 'white'

    def change_lining(self, new_type, new_color):
        self.type = new_type
        self.color = new_color
        print(f"Lining has been changed to {self.color} {self.type}")

    def get_lin(self):
        if self.lintype == True:
            print("The clothing has lining")
        else :
            print("The clothing does not have lining")


class Embellishments:
    def __init__(self, embelltype : bool):
        self.embelltype = embelltype
        self.type = 'beads'
        self.color = 'gold'

    def add_embellishment(self):
        print("An embellishment has been added")   

    def get_embell(self):
        if self.embelltype == True:
            print("The clothing has embellishment")
        else :
            print("The clothing does not have embellishment")

       
# Composition classes
class Fabric:
    def __init__(self):
        self.type = 'cotton'
        self.pattern = 'solid'

    def change_color(self, new_color):
        self.pattern = 'solid'
        print(f"Fabric pattern has been changed to {self.pattern} {new_color}")

class Thread:
    def __init__(self):
        self.color = 'white'
        self.type = 'polyester'

    def change_thread(self, new_color, new_type):
        self.color = new_color
        self.type = new_type
        print(f"Thread has been changed to {self.color} {self.type}")
        