from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from nrl_todo import todo_function
from screenshot import Takescreenshot


app = Flask(__name__)

@app.route("/")
def hello1():
    return "Hello, World! Welcome to Bot"

@app.route("/sms", methods=["GET","POST"])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    return_val =todo_function(msg)   
   
    _returnmsg=format(return_val)
       

    if(_returnmsg.find("#") == 1):
         response=resp.message(_returnmsg)  
          #response.media("http://18c145e05696.ngrok.io/"+ _returnmsg +".jpg")
    else:
          response=resp.message(_returnmsg)
          response.media("http://18c145e05696.ngrok.io/"+ _returnmsg +".jpg")

   #response.media("http://18c145e05696.ngrok.io/"+ _returnmsg +".jpg")
   
	#  response.media("http://18c145e05696.ngrok.io/"+ format(return_val) +".jpg")
  
  
    #response.media("file:///C:/Users/bisharbn/Pictures/1.jpg")
    #response.media("https://img.lovepik.com/photo/40104/2699.jpg_wh300.jpg")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
