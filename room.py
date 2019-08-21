class Room:
    
    def __init__(self, color, inventory, exits):
        self.color = color
        self.inventory = inventory         
        self.exits = exits
        self.special_items = list()
               
    def get_color(self):
        return self.color    
    
    def get_inventory(self):
        return ', '.join(self.inventory)
        
    def get_special_items(self):
        return self.special_items
    
    def get_exits(self):
        return ', '.join(self.exits)
        
    def sub_inventory(self,item):
        if item in self.inventory:
            index = self.inventory.index(item)
            return self.inventory.pop(index)
        else:
            print('sorry no {} here'.format(item))
            return 0
    
    def add_inventory(self,item):
        self.inventory.append(item)
        
    def add_special_item(self,special_item):
        self.special_items.append(special_item)

    def sub_special_item(self,item_name):
        
        for i in range(len(self.special_items)):

            if self.special_items[i].name == item_name:

                del self.special_items[i]
                return True
        return False
       
class Player:
    def __init__(self,inventory):
        self.inventory = inventory
        self.x =0
        self.y =0   
    
    def get_inventory(self):
        return ', '.join(self.inventory)
            
    def add_inventory(self,item):
        self.inventory.append(item)
        
    def sub_inventory(self,item):
        if item in self.inventory:
            index = self.inventory.index(item)
            return self.inventory.pop(index)
        else:
            print('sorry no {} here'.format(item))
            return 0
        
    def get_position(self):
        return (self.x,self.y)
    
    def move(self,direction):   
        if direction == "north":
            self.y -= 1
        elif direction == "south":
            self.y+= 1
        elif direction == "east":
            self.x += 1
        elif direction == "west":
            self.x -= 1
            
class Item:
    def __init__(self,name,use_item,dialog,event):
        self.name = name
        self.use_item = use_item
        self.dialog = dialog
        self.event = event
        
            
class House:
    def __init__(self,controller):
        rm_1_color = 'red'
        rm_1_inventory = ['book','hammer']
        rm_1_exits = ['South','East']

        rm_2_color = 'blue'
        rm_2_inventory = ['key','fork']
        rm_2_exits = ['South','West']

        rm_3_color = 'green'
        rm_3_inventory = ['dice','seeds']
        rm_3_exits = ['North','East']

        rm_4_color = 'yellow'
        rm_4_inventory = ['soap','cup']
        rm_4_exits = ['North','West']
        
        door = Item("door",'key',"There is a large door, it is locked",controller.unlock_door)
        rock = Item("rock",'hammer',"There is a giant rock, it is shiny",controller.break_rock)
        car = Item("car",'soap',"There is a old car, it is dirty",controller.clean_car)
        bird = Item("bird",'seeds',"There is a small bird, it looks hungry",controller.feed_bird)
        
        room_1 = Room(rm_1_color,rm_1_inventory,rm_1_exits)
        room_1.add_special_item(door)
        
        room_2 = Room(rm_2_color,rm_2_inventory,rm_2_exits)
        room_2.add_special_item(rock)
        
        room_3 = Room(rm_3_color,rm_3_inventory,rm_3_exits)
        room_3.add_special_item(car)
        
        room_4 = Room(rm_4_color,rm_4_inventory,rm_4_exits)
        room_4.add_special_item(bird)
        
        self.rooms = [[room_1,room_2],[room_3,room_4]]
    
    
class Controller:
    def __init__(self): 
        player_inventory = ['map','compass']
        self.house = House(self)
        self.current_room = self.house.rooms[0][0]
        self.player = Player(player_inventory)
         
    def update_player(self,direction):    
        self.player.move(direction)
        x,y = self.player.get_position()
        temp = self.house.rooms[y][x]   
        return temp
    
    def get_room_exits(self):
        return self.current_room.get_exits()
        
    def get_room_inventory(self):
        return self.current_room.get_inventory()
    
    def get_room_info(self):
        return self.current_room.get_color()
        
    def get_special_items(self):
        return self.current_room.get_special_items()
        
        
    def is_one_of_in_list(self,list_a,list_b):
        for word in list_a:
            for possible_match in list_b:
                if possible_match == word:
                    return True                   
        return False
        
    def are_all_in_list(self,list_a,list_b):
        count = 0
        max = len(list_a)
        for word in list_a:
            for possible_match in list_b:
                if possible_match == word:
                    count += 1
                
        if count == max:
            return True
        else:
            return False
        
    def get_match(self,list_a,list_b): 
        for item in list_a:
            if item in list_b:
                return item
        return None
        
    def get_special_match(self,list_a,list_b): 
        for item in list_a:
            for special_item in list_b:
                if item == special_item.name:
                    return special_item
        return None
    
    def show_room_dialog(self):
        print()
        print('The room is '+self.get_room_info())
        print('There are these items in the room: '+self.get_room_inventory())        
        for item in self.get_special_items():
            print(item.dialog)
        print('These are the exits from the room: '+self.get_room_exits())
        
    def unlock_door(self,special_item):
        print()
        print("the door unlocks and slowly opens.")
        print("A large egg rolls out onto the floor.")
        print("The door disapears in a puff of smoke!")       
        self.current_room.add_inventory('egg')
        self.player.sub_inventory(special_item.use_item)
        self.current_room.sub_special_item(special_item.name)
                
    def break_rock(self,special_item):
        print()
        print("The hammer smashes the rock into dust")
        print("A large gold nugget is all that is left.")
        print("The hammer was turned to dust as well!")
        self.current_room.add_inventory('nugget')
        self.player.sub_inventory(special_item.use_item)
        self.current_room.sub_special_item(special_item.name)
        
    def clean_car(self,special_item):
        print()
        print("the car is clean")
        print("A man runs in, jumps in the car and drives away.")
        print("The man dropped his wallet!")
        self.current_room.add_inventory('wallet')
        self.player.sub_inventory(special_item.use_item)
        self.current_room.sub_special_item(special_item.name)
        
    def feed_bird(self,special_item):
        print("the bird is feed")
        print("The bird flys away, but quickly comes back.")
        print("the bird drops a shiny ring on the ground an leaves!")
        self.current_room.add_inventory('ring')
        self.player.sub_inventory(special_item.use_item)
        self.current_room.sub_special_item(special_item.name)
             
    def check_user_input(self,user_input):
    
        user_input = user_input.split(" ")

        if self.is_one_of_in_list(['help','ugh'],user_input):
            print('Try using key words: move north, get item, drop item, get inventory, use this with that')
        
        elif self.is_one_of_in_list(['move','go'],user_input):
        
            word = self.get_match(user_input,self.get_room_exits().lower())
            
            if word != None:
                self.current_room = self.update_player(word)
                print('you move to the',word)
            else:
                print("sorry I cant move that way right now")
            
        elif self.is_one_of_in_list(['get','take'],user_input):

            word = self.get_match(user_input,self.get_room_inventory())
            
            if self.is_one_of_in_list(['inventory','stuff'],user_input):
                print(self.player.get_inventory())            
            elif word != None:    
                item = self.current_room.sub_inventory(word)
                self.player.add_inventory(item)
                print('the',item,'has been picked up')
                
            else:
                print("sorry, cant get that right now")
            
        elif self.are_all_in_list(['use','with'],user_input):
        
            special_item = self.get_special_match(user_input,self.get_special_items())
            
            if special_item != None:
                word = self.get_match(user_input,self.player.get_inventory())
                if word != None:
                    if special_item.use_item == word:
                        special_item.event(special_item)
                        
                    else:
                        print("sorry I cant use it that way")
                else:
                    print("sorry I cant use it that way")        
            else:
                print("sorry I cant use it that way") 
                
        elif self.is_one_of_in_list(['drop','leave'],user_input):
        
            word = self.get_match(user_input,self.player.get_inventory())
            
            if word != None:
                self.player.sub_inventory(word)
                self.current_room.add_inventory(word)
                print('the',word,'has been dropped')
            else:
                print("sorry you dont have that")
                
            
        else:
            print("sorry I cant help you do that")
        
    
 
    
    
    
    
    
    
    