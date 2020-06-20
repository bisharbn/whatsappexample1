# Switcher is dictionary data type here 
def todo_function(argument): 
    _Screenvalue=""" #Welcome to NRL Whatsapp BOT \n Press one of the following  
1. Compendium
2. FSI Error
"""
    switcher = {        
        "1": Compendium(), 
        2: "2", 
        3: "3",
        4: "4",
        "comp": downloadcompendium,
        "0":_Screenvalue
    } 
    return switcher.get(argument, "nothing") 
  
#To Download the compendium
def Compendium():
    """This function greets to the person passed in asa parameter"""    
    _compendium_text=""" #Please enter the Order Code ~comp~ 
"""
    return (_compendium_text)


def downloadcompendium(testcode):
    """This function greets to the person passed in asa parameter"""    
    _Comp=testcode +" #TestName : Glucose"
    _compendium_text=""" # Test Code """
    return (_Comp)