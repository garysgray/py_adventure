from room import Controller

control = Controller()   
user_input = ""

while(True):
    
    control.show_room_dialog()
    
    user_input = input("What is your next request ")
    
    
    if user_input != 'quit':
        control.check_user_input(user_input)
                                  
    else:
        print("good day!!!")
        break
        
        

        

        