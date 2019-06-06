
class Room:
    
    def __init__(self, color, inventory, exits):
        self.color = color
        self.inventory = inventory 
        self.exits = exits
        
    def get_color(self):
        return self.color    
    
    def get_inventory(self):
        return ', '.join(self.inventory)
                
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
            
            
class House:
    def __init__(self):
        rm_1_color = 'red'
        rm_1_inventory = ['fork','rock','sneakers']
        rm_1_exits = ['South','East']

        rm_2_color = 'blue'
        rm_2_inventory = ['spoon','scissors','slippers']
        rm_2_exits = ['South','West']

        rm_3_color = 'green'
        rm_3_inventory = ['knife','paper','boots']
        rm_3_exits = ['North','East']

        rm_4_color = 'yellow'
        rm_4_inventory = ['plate','cup','knapkin']
        rm_4_exits = ['North','West']
        
        
        room_1 = Room(rm_1_color,rm_1_inventory,rm_1_exits)
        room_2 = Room(rm_2_color,rm_2_inventory,rm_2_exits)
        room_3 = Room(rm_3_color,rm_3_inventory,rm_3_exits)
        room_4 = Room(rm_4_color,rm_4_inventory,rm_4_exits)
        
        self.rooms = [[room_1,room_2],[room_3,room_4]]
    
    
class Controller:

    

    def __init__(self,player_inventory):
    
        self.house = House()
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
        
    
    
    
    
    
    
    
    
    
    
    
    
    