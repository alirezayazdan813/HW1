class Clothing:
    # material = ""
    type = ""

    def __init__(self, name, color : str, size, season, polymer_percent, cotton_percent'''pocket : pocket'''):
        self.name = name
        self.colors = color
        self.size = size
        self.fabric = fabric(color, polymer_percent, cotton_percent)
        self.season = season
        self.polymer_percent = polymer_percent
        self.cotton_percent = cotton_percent

    def check_p_cotton(self):
        return "This {} contains {} percent of cotton".format(self.name, self.cotton_percent)

    def check_p_polymer(self):
        return "This {} contains {} percent of polymer".format(self.name, self.polymer_percent)

    def season(self):
        return "{} is usually used in {}".format(self.name, self.season)

    def color(self):
        return "This {} is {}".format(self.name, self.color)

    def change_color(self, color):
        self.color = color

    def size(self):
        return "This {} is {}".format(self.name, self.size)

    def change_size(self, size):
        self.size = size


# /////////////////////////////////////////////////////////////////////////////////////////////
class Shirt(Clothing):
    # material = "Cotton"
    type = "shirt"

    def __init__(self, name, color, size, season, polymer_percent, cotton_percent, pocket, model):
        super().__init__(name, color, size, season, polymer_percent, cotton_percent)
        self.pocket = pocket
        self.model = model

    def sit_pocket(self):
        if self.pocket is None :
            return "The shirt, does not have pocket"
        else :
            return "The shirt, {}".format(self.pocket)  # The shirt, (has pocket) or (does not have pocket)

    def model(self):
        return "The shirt is {}".format(self.model)  # The shirt is (long sleeve) or (short sleeve)


polo = Shirt("Polo", "red", 'XL', "spring", 60, 40, 'has pocket', 'long sleeve')
print(polo.size)
polo.change_size('XXL')
print(polo.size)


# print(polo.size())  ???
# //////////////////////////////////////////////////////////////////////////////////////
class Tshirt(Clothing):
    # material = "Cotton"
    type = "t-shirt"

    def __init__(self, name, color, size, season, polymer_percent, cotton_percent, model, style):
        super().__init__(name, color, size, season, polymer_percent, cotton_percent)
        self.style = style
        self.model = model

    def model(self):
        return "This t-shirt is {}".format(self.model)  # This t-shirt is (v-neck) or (ringer)

    def style(self):
        return "This t-shirt's is {} t-shirt".format(self.style)  # This t-shirt is (singlet) or (normal) t-shirt
 
#////////////////////////////////////////////////////////////////////////////////////////
class Socks(Clothing):
    # material = "Cotton"
    type = "socks"

    def __init__(self, name, color, size, season, polymer_percent, cotton_percent, height, pattern):
        super().__init__(name, color, size, season, polymer_percent, cotton_percent)
        self.height = height
        self.pattern = pattern
    def get_height(self):
        return "The sock's height is {}".format(self.height)
    def get_pattern(self):
        return "Sock's pattern is {}".format(self.pattern)
       
#/////////////////////////////////////////////////////////////////////////////////////////
class Jacket(Clothing):
    # material = "Cotton"
    type = 'jacket'

    def __init__(self, name, color, size, season, polymer_percent, cotton_percent, brand, price):
        super().__init__(name, color, size, season, polymer_percent, cotton_percent)
        self.brand = brand
        self.price = price

    def get_brand(self):
        return "This jacket belongs to the {} brand".format(self.brand) #This jacket belongs to the boss brand

    def get_price(self):
        return "The price of this jacket is {} dollars".format(self.price) #The price of this jacket is 2 dollars

mmd_jacket = Jacket('Bomber', 'red', 'XL', 'Winter', 15, 85, 'boss', 2)
print(mmd_jacket.get_price())

#/////////////////////////////////////////////////////////////////////////////////////
class Jeans(Clothing):
    # material = "Cotton"
    type = 'jeans'

    def __init__(self, name, color, size, season, polymer_percent, cotton_percent, pocket_num, fly):
        super().__init__(name, color, size, season, polymer_percent, cotton_percent)
        self.pocket_num = pocket_num
        self.fly = fly

    def get_pocketnum(self):
        return "These jeans have {} pockets".format(self.pocket_num) #These jeans have 5 pockets

    def get_flytype(self):
        return "The fly of these jeans is {}".format(self.fly) #The fly of these jeans is zipper
#//////////////////////////////////////////////////////////////////////////////////
class Shorts(Clothing):
    # material = "Cotton"
    type = 'shorts'

    def __init__(self, name, color, size, season, polymer_percent, cotton_percent, s_type, pocket):
        super().__init__(name, color, size, season, polymer_percent, cotton_percent)
        self.s_type = s_type
        self.pocket = pocket

    def get_stype(self):
        return "These shorts are {}".format(self.s_type) #These shorts are boxer

    def get_flytype(self):
        return "These shorts have pocket : {}".format(self.pocket) #These shorts have pocket : True

#//////////////////////////////////////////////////////////////////////////////////
class fabric():
    # material = ""
    type = ""

    def __init__(self, color, season, polymer_percent, cotton_percent):
        self.colors = color
        self.polymer_percent = polymer_percent
        self.cotton_percent = cotton_percent

    def check_p_cotton(self):
        return "This {} contains {} percent of cotton".format(self.name, self.cotton_percent)

    def check_p_polymer(self):
        return "This {} contains {} percent of polymer".format(self.name, self.polymer_percent)

    def color(self):
        return "This {} is {}".format(self.name, self.color)

    def change_color(self, color):
        self.color = color

# ???? 5
#///////////////////////////////////////////////////////////////////////////////////

    
        
        






