import os
from bottle import Bottle, request
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  


sentry_sdk.init(
    dsn="", #  <--- введи здесь свой SENTRY_DSN
    integrations=[BottleIntegration()])  
  
app = Bottle()  

@app.route('/success') 
def success():
    return "Knock, knock, Neo. 🐇"

@app.route('/fail') 
def fail():    
    raise RuntimeError("There is an error! >:\ ")
    
if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080)