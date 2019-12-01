from flask import Flask, request
import js2py
import json
import pytesseract
from PIL import Image
import base64


app = Flask(__name__)
 
@app.route("/extractDate", methods=['POST'])
def hello():	

        imgstring =  request.json['base_64_image_content']

	imgdata = base64.b64decode(imgstring)
	filename = './image.png'  
	with open(filename, 'wb') as f:
	    f.write(imgdata)
	    f.close()

	    f = js2py.eval_js( """function $(temp) {   
		
		var ddmmyyyy = /(?:[0-9]|[0-3][0-9])(?:[./-]|[\s])(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])[1-2][0-9][0-9][0-9]/i;
		
		var mmddyyyy = /(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])[0-3][0-9](?:[./-]|[\s])[1-2][0-9][0-9][0-9]/i;
		    
		var ddmonthyy = /[0-3][0-9](?:[./-]|[\s])(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:[./-]|[\s])[0-9][0-9][\s]/i;
		
		var ddmonthapoyy = /[0-3][0-9](?:[./-]|[\s]|)(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:[.'/-]|[\s])[0-9][0-9][\s]/i;
		
		var ddmmyy = /(?:[0-3][0-9]|[0-9])(?:[./-]|[\s])(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])([0-9][0-9][\s])/i;
		
		var ddmonthyyyy = /[0-3][0-9](?:[./-]|[\s])(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:[./-]|[\s])(?:[0-9][0-9][0-9][0-9]|[0-9][0-9])/i;
		
		var mmddyy = /(?:[0-1][0-9]|[0-9])(?:[./-]|[\s])[0-3][0-9](?:[./-]|[\s])([0-9][0-9])/i;
		
		var t;
		if(temp.match(ddmmyyyy))
		{
		    t = temp.match(ddmmyyyy);
		}
		else if(temp.match(mmddyyyy))
		{
		    t= temp.match(mmddyyyy);
		}
		else if(temp.match(ddmmyy))
		{
		    t= temp.match(ddmmyy);
		}
		else if(temp.match(mmddyy))
		{
		    t= temp.match(mmddyy);
		}
		else if(temp.match(ddmonthyyyy))
		{
		    t= temp.match(ddmonthyyyy);
		}
		else if(temp.match(ddmonthyy))
		{
		    t= temp.match(ddmonthyy);
		}
		else if(temp.match(ddmonthapoyy))
		{
		    t= temp.match(ddmonthapoyy);
		}
		else
		{
		    t = "null"
		}
		
		document.write(t[0]);
		
	    }
		""".replace("document.write", "return "))

	result = f(text)

	if(result != None):
	    return(str("{ 'date': '")+str(result)+str("' }")         
	else:
	    return( str("{ 'date': 'null' }"))

@app.route("/extractDate", methods=['GET'])
def helloget():
	return("GET is working fine")

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")
