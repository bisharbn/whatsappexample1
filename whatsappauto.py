from twilio.rest import Client 
 
account_sid = 'AC1f9bea9242d22f9333cfb6eebcc14a05' 
auth_token = 'b3b3827e62feac844cc750fb1f581961' 
client = Client(account_sid, auth_token) 

def send_message(message1):
    """Send Message function"""
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=message1,      
                              to='whatsapp:+971556951445' 
                          )                        

    print(message.sid)

_Screenvalue=""" Welcome to NRL Whatsapp BOT \n Press one of the following  
Please choose your Choice 
1. Bishar Photo
2. Sajina Photo
3. Ayaan Bishar Photo
4. Aydin Bishar Photo
5. Family Photo
0 .Main Menu
"""
send_message(_Screenvalue)
    