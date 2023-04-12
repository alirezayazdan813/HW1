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
        return self.zipper.get_zip(self)

    def get_pocket(self):
        return self.pocket.put_item(self)

    def get_button(self):
        return self.buttons.add_button(self)

    def get_lining(self):
        return self.lining.change_lining(self)

    def get_embellishment(self):
        return self.embellishments.add_embellishment(self)

    def wash(self):
        print("Washing instructions: Machine wash cold, tumble dry low")

    def iron(self):
        print("Ironing instructions: Iron on low heat")


# Aggregation classes
class Zipper:
    def __init__(self, ziptype: bool):
        self.ziptype = ziptype
        self.length = 10
        self.color = 'silver'

    def zip_up(self):
        print("Zipper is now zipped up")

    def get_zip(self):
        if self.ziptype == True:
            print("The clothing has a zipper")
        else:
            print("The clothing does not have a zipper")


class Pocket:
    def __init__(self, pocktype: bool):
        self.pocktype = pocktype
        self.number_of_pockets = 2
        self.size = 'medium'

    def put_item(self):
        print("Item has been put in pocket")


class Buttons:
    def __init__(self, butttype: bool):
        self.butttype = butttype
        self.number_of_buttons = 5
        self.color = 'black'

    def add_button(self):
        print("A new button has been added")



class Lining:
    def __init__(self, lintype: bool):
        self.lintype = lintype
        self.type = 'satin'
        self.color = 'white'

    def change_lining(self, new_type, new_color):
        self.type = new_type
        self.color = new_color
        print(f"Lining has been changed to {self.color} {self.type}")



class Embellishments:
    def __init__(self, embelltype: bool):
        self.embelltype = embelltype
        self.type = 'beads'
        self.color = 'gold'

    def add_embellishment(self):
        print("An embellishment has been added")

       
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

    def change_color(self, new_color):
        self.color = new_color
        print(f"Thread has been changed to {self.color} {self.type}")

    def change_type(self, new_type):
        self.type = new_type
        print(f"Thread has been changed to {self.color} {self.type}")

# Child classes with polymorphism
class Shirt(Clothing):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, sleeve_length):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell)
        self.sleeve_length = sleeve_length

    def iron(self):
        print("Ironing instructions: Iron on medium heat")

class Jeans(Clothing):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, style):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell)
        self.style = style

    def wash(self):
        print("Washing instructions: Machine wash in warm water, tumble dry low")

class Shorts(Clothing):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, length):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell)
        self.length = length

    def wash(self):
        print("Washing instructions: Machine wash in cold water, hang to dry")

class Socks(Clothing):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, material):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell)
        self.material = material

    def wash(self):
        print("Washing instructions: Machine wash in warm water, tumble dry low")

class Jacket(Clothing):
    def __init__(self, size, color, brand, price, Zip, ziptype, Pock, Butt, Lin, Embell, hooded):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell)
        self.hooded = hooded
        self.ziptype = ziptype

    def iron(self):
        print("Ironing instructions: Iron on low heat")
    
    def hoodhood(self):
        print("This jacket is hooded : {}".format(self.hooded))

    def get_zip(self):
        return self
    #?????????????????????????????????????????????????????????????????????

# testing inharitance and aggregation 
mmd = Jacket("XL", "red", "sinsin", 18, Zipper, True, Pocket, Buttons, Lining, Embellishments, False)
mmd.iron()
mmd.hoodhood()
mmd.get_zipper()

# testing composition
ali = Socks("medium", "white", "jj", 5, Zipper, Pocket, Buttons, Lining, Embellishments, 'cotton')
ali.wash()
ali.get_button()
ali.fabric.change_color("blue")


