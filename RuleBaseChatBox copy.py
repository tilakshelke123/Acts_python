def ChatBot():
    name=input("Enter your name:-")
    
    print("Welcome! To the Wold of Home Automation chatpot ",name)
    print("Control: 1> Lights, 2> Fan, 3>AC, 4>Door Lock " )
    
    while True:
        user_input = input("Enter command (1/2/3/4): ")
        
        
        if user_input == '1':
               print(" Current Lights status ")
               btn=input("want to tun on/off light type O for on and F for off:")
               if btn=='O':
                print("Light is on")
                
                
               elif btn=='F':
                print("Light is Off")
               else:
                print("Invalid option")
            
        elif user_input == '2':
                print("Fan speed status")
           
                btn=input("want to tun on/off Fan type O for on and F for off:")
                if btn=='O':
                 print("Fan is on")
                elif btn=='F':
                 print("Fan is Off")
                else:
                 print("Invalid option")   
        elif user_input == '3':
                print("Air Conditioner  status.")
            
                btn=input("want to tun on/off Air Conditioner type O for on and F for off:")
                if btn=='O':
                 print("Air Conditioner is on")
                elif btn=='F':
                 print("Air Conditioner is Off")
                else:
                 print("Invalid option")   
        elif user_input == '4':
               print("Door Lock status ")
          
               btn=input("want to tun open/close Door Lock type O for open and F for close:")
               if btn=='O':
                print("Door is open")
               elif btn=='F':
                print("Door  is close")
               else:
                print("Invalid option")  
       
       
        else:
            print("Invalid command.")

if __name__ == "__main__":
    ChatBot()
    
    
 