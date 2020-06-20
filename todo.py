from screenshot import Takescreenshot

def todo_function(res):
    """This function greets to the person passed in asa parameter"""    
    _returnval=''

    _Screenvalue=""" Welcome to NRL Whatsapp BOT \n Press one of the following  
1. Take Screenshot and Send Email 
2. Send Compendium
"""


    #Takescreenshot()
    return (do_action_useresponse(int(res)))

   # if (res==1) :
    #    Takescreenshot()
    #    _returnval='Take Screenshot and send email' 
    #else: 
     #    Takescreenshot()
      #   _returnval=_Screenvalue
    
# Switcher is dictionary data type here 
def do_action_useresponse(argument): 
    _Screenvalue=""" Welcome to NRL Whatsapp BOT \n Press one of the following  
Please choose your Choice 
1. Bishar Photo
2. Sajina Photo
3. Ayaan Bishar Photo
4. Aydin Bishar Photo
5. Family Photo
0 .Main Menu
"""
    switcher = {        
        1: "1", 
        2: "2", 
        3: "3",
        4: "4",
        5: "5",
        0:_Screenvalue
    } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "nothing") 
  


    #return (_returnval)

