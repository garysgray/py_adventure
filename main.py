from room import Controller

player_inventory = ['map','pocket mirror','compass']
control = Controller(player_inventory)
   
user_input = ""
while(True):

    print()
    print('The room is '+control.get_room_info())
    print('There are these items in the room: '+control.get_room_inventory())
    print('These are the exits from the room: '+control.get_room_exits())
    
    user_input = input("What is your next request ")
    
    if user_input != 'quit':
        
        
        if "help" in user_input:
            print('Try using key words: move north, get item, drop item, get inventory')
        
        elif "move" in user_input or "go" in user_input:            
            user_input = user_input.split(" ")
            if user_input[1] in (control.get_room_exits()).lower():
                control.current_room = control.update_player(user_input[1])
            else:
                print("sorry I cant move "+str(user_input[1])+" right now")
        elif "get" in user_input:
            user_input = user_input.split(" ")
            if user_input[1] == 'inventory':
                print(control.player.get_inventory())
            elif user_input[1] in control.get_room_inventory():
                item = control.current_room.sub_inventory(user_input[1])
                control.player.add_inventory(item)
            else:
                print("sorry I cant get "+str(user_input[1])+" right now")
        elif "drop" in user_input:
            user_input = user_input.split(" ")
            if user_input[1] in control.player.get_inventory():
                item = control.player.sub_inventory(user_input[1])
                control.current_room.add_inventory(item)
            else:
                print("sorry you dont have "+str(user_input[1])+" right now")
        else:
            print("sorry I cant help you "+str(user_input)+" right now")
    else:
        print("good bye and good ridance!!!")
        
        
        
        
        
        
        