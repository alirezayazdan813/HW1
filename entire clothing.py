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

# Child classes with polymorphism (iron, wash)
class Shirt(Clothing):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, sleeve_length):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell)
        self.sleeve_length = sleeve_length

    def get_neck(self):
        if  33.5 <= self.sleeve_length < 34 :
            print("This shirt has 17-17.5 neck")
        elif  34 <= self.sleeve_length < 34.5 :
            print("This shirt has 17.5-18 neck")
        elif  34.5 <= self.sleeve_length < 35 :
            print("This shirt has 18-18.5 neck")
        elif  35 <= self.sleeve_length < 35.5 :
            print("This shirt has 18.5-19 neck")
        elif  35.5 <= self.sleeve_length < 36 :
            print("This shirt has 19-19.5 neck")

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

# testing inharitance and aggregation 
obj0 = Jacket("XL", "red", "sinsin", 18, Zipper, True, Pocket, Buttons, Lining, Embellishments, False)
obj0.iron()
obj0.hoodhood()
obj0.get_zipper()
print("End of obj0 (jacket)")
print("")

# testing composition
obj1 = Socks("medium", "white", "jj", 5, Zipper, Pocket, Buttons, Lining, Embellishments, 'cotton')
obj1.wash()
obj1.get_button()
obj1.fabric.change_color("blue")
print("End of obj1 (socks)")
print("")

# Grandchild classes for Shirt
class TShirt(Shirt):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, sleeve_length, graphic):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, sleeve_length)
        self.graphic = graphic

    def get_graphic(self):
        print("This attractive t-shirt has {} design on it".format(self.graphic))


class DressShirt(Shirt):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, sleeve_length, collar_type):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, sleeve_length)
        self.collar_type = collar_type

class PoloShirt(Shirt):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, sleeve_length, material_type):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, sleeve_length)
        self.material_type = material_type

# Grandchild classes for Jeans
class SkinnyJeans(Jeans):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, style, ripped):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, style)
        self.ripped = ripped

class BootcutJeans(Jeans):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, style, inseam):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, style)
        self.inseam = inseam

class StraightJeans(Jeans):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, style, stretch):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, style)
        self.stretch = stretch
        
# Grandchild classes for Shorts
class CargoShorts(Shorts):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, length, number_of_pockets):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, length)
        self.number_of_pockets = number_of_pockets

class BoardShorts(Shorts):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, length, pattern):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, length)
        self.pattern = pattern

class DenimShorts(Shorts):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, length, cuffs):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, length)
        self.cuffs = cuffs
        
# Grandchild classes for Socks
class AnkleSocks(Socks):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, material, number_of_pairs):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, material)
        self.number_of_pairs = number_of_pairs

class AthleticSocks(Socks):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, material, arch_support):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, material)
        self.arch_support = arch_support

class DressSocks(Socks):
    def __init__(self, size, color, brand, price, Zip, Pock, Butt, Lin, Embell, material, pattern):
        super().__init__(size, color, brand, price, Zip, Pock, Butt, Lin, Embell, material)
        self.pattern = pattern
        
# Grandchild classes for Jacket
class Windbreaker(Jacket):
    def __init__(self, size, color, brand, price, Zip, ziptype, Pock, Butt, Lin, Embell, hooded, waterproof):
        super().__init__(size, color, brand, price, Zip, ziptype, Pock, Butt, Lin, Embell, hooded)
        self.waterproof = waterproof

class BomberJacket(Jacket):
    def __init__(self, size, color, brand, price, Zip, ziptype, Pock, Butt, Lin, Embell, hooded, material_type):
        super().__init__(size, color, brand, price, Zip, ziptype, Pock, Butt, Lin, Embell, hooded)
        self.material_type = material_type

class FleeceJacket(Jacket):
    def __init__(self, size, color, brand, price, Zip, ziptype, Pock, Butt, Lin, Embell, hooded, zip_num):
        super().__init__(size, color, brand, price, Zip, ziptype, Pock, Butt, Lin, Embell, hooded)
        self.zip_num = zip_num

    def get_zip_num(self):
        print("This jacket has {} zippers".format(self.zip_num))

# testing grand child class
obj2 = TShirt("XL", "yellow", "zak", 12, Zipper, Pocket, Buttons, Lining, Embellishments, 34, 'tupac')
obj2.get_graphic()
obj2.iron()
obj2.get_embellishment()
obj2.thread.change_type("BSPP")
obj2.get_neck()
print("End of obj 2 (tshirt)")
print("")

obj3 = FleeceJacket("XL", "Blue", "TU", 33, Zipper, True, Pocket, Buttons, Lining, Embellishments, True, 3)
obj3.iron()
obj3.hoodhood()
obj3.get_zipper()
print(obj3.zip_num)
obj3.get_zip_num()
print("End of obj 3 (fleece jacket)")
