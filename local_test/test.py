import js2py
import json
import pytesseract
from PIL import Image
import base64
import sys
import csv
if __name__ == "__main__":
	with open(str(sys.argv[1]), "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
   	
	#print(encoded_string)
	imgstring = encoded_string
	imgdata = base64.b64decode(imgstring)
    filename = './image.png'
    with open(filename, 'wb') as f:
		f.write(imgdata)
		f.close()

    text = pytesseract.image_to_string(Image.open(r'./image.png'))
    print(text)

	f = js2py.eval_js( """


	function $(temp) {   

	function getMonth(m){
	m = ("janfebmaraprmayjunjulaugsepoctnovdec".indexOf(m.toLowerCase()) / 3 + 1).toString() ;
	if(m.length == 1)
	{
	return "0"+m;
	}
	else
	{
	return m;
	}

	}
	var states = /([\s](?:[A][L]|[A][K]|[A][Z]|[A][R]|[C][A]|[C][O]|[C][T]|[D][E]|[F][L]|[G][A]|[H][I]|[I][D]|[I][L]|[I][N]|[I][A]|[K][S]|[K][Y]|[L][A]|[M][E]|[M][D]|[M][A]|[M][I]|[M][N]|[M][S]|[M][O]|[M][T]|[N][E]|[N][V]|[N][H]|[N][J]|[N][M]|[N][Y]|[N][C]|[N][D]|[O][H]|[O][K]|[O][R]|[P][A]|[R][I]|[S][C]|[S][D]|[T][N]|[T][X]|[U][T]|[V][T]|[V][A]|[W][A]|[W][V]|[W][I]|[W][Y])[\s])/i;
	
	var ddmmyyyy = /(?:[0-9]|[0-3][0-9])(?:[./-]|[\s])(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])[1-2][0-9][0-9][0-9]/i;
	
	var mmddyyyy = /(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])[0-3][0-9](?:[./-]|[\s])[1-2][0-9][0-9][0-9]/i;
		
	var ddmonthyy = /[0-3][0-9](?:[./-]|[\s])(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC|January|Febrary|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)(?:[./-]|[\s])[0-9][0-9][\s]/i;
	
	var ddmonthapoyy = /[0-3][0-9](?:[./-]|[\s]|)(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC|January|Febrary|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)(?:[.'/-]|[\s])[0-9][0-9][\s]/i;
	
	var monthddapoyy = /(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC|January|Febrary|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)(?:[./-]|[\s]|)(?:[0-3][0-9]|[0-9])[',][0-9][0-9][\s]/i;

	var monthddyyyy = /(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC|January|Febrary|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)(?:[\s]|[./-]|)(?:[1-3][0-9]|[0-9])(?:[,'][\s]|[,'])[1-2][0-9][0-9][0-9]/i;

	var monthddyy = /(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC|January|Febrary|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)(?:[\s]|[./-]|)(?:[1-3][0-9]|[0-9])[',][0-9][0-9]/i;

	var ddmmyy = /(?:[0-3][0-9]|[0-9])(?:[./-]|[\s])(?:[0-9]|[0-1][0-9])(?:[./-]|[\s])([0-9][0-9][\s])/i;
	
	var ddmonthyyyy = /[0-3][0-9](?:[./-]|[\s])(:?Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC|January|Febrary|March|April|May|June|July|August|September|October|November|December|JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)(?:([\s][./-])|[./-]|[\s])(?:[0-9][0-9][0-9][0-9]|[0-9][0-9])/i;
	
	var mmddyy = /(?:[0-1][0-9]|[0-9])(?:[./-]|[\s])[0-3][0-9](?:[./-]|[\s])([0-9][0-9])/i;
	
	var t;
	
	if(temp.match(monthddyyyy))
	{
		t= temp.match(monthddyyyy)[0].toString();
		t = t.split(/([\s])+/);
		return [t[4],getMonth(t[0]).toString(),t[2][0]].join('-');
	}
	else if(temp.match(monthddyy))
	{
		t= temp.match(monthddyyyy)[0].toString();return t;
		//t = t.split(/([\s])+/);
		//return [t[4],getMonth(t[0]).toString(),t[2][0]].join('-');
	}
	else if(temp.match(mmddyyyy)&& temp.match(states))
	{
		t = temp.match(mmddyyyy)[0].toString();
		t = t.split(/[\s./-]+/);
		return [t[2],t[0],t[1]].join('-');
	}else if(temp.match(mmddyyyy))
	{
		t = temp.match(mmddyyyy)[0].toString();
		t = t.split(/[\s./-]+/);
		return [t[2],t[0],t[1]].join('-');
	}
	else if(temp.match(ddmmyyyy))
	{
		t = temp.match(ddmmyyyy)[0].toString();
		t = t.split(/[\s./-]+/);
		return [t[2],t[1],t[0]].join('-');
	}
	else if(temp.match(mmddyy)&& temp.match(states))
	{
		t = temp.match(mmddyy)[0].toString();
		t = t.split(/[\s,/-]+/);
		return ["20"+t[2],t[0],t[1]].join('-');
	}
	else if(temp.match(mmddyy))
	{
		t = temp.match(mmddyy)[0].toString();
		t = t.split(/[\s,/-]+/);
		return ["20"+t[2],t[0],t[1]].join('-');
	}
	else if(temp.match(ddmmyy))
	{
		t = temp.match(ddmmyy)[0].toString();
		t = t.split(/[\s,/-]+/);
		return ["20"+t[2],t[1],t[0]].join('-');
	}

	else if(temp.match(ddmonthyyyy))
	{
		t= temp.match(ddmonthyyyy)[0].toString();
		t = t.split(/[\s'/-]+/);
		return [t[2],getMonth(t[1]).toString(),t[0]].join('-');
	}
	else if(temp.match(ddmonthyy))
	{
		t= temp.match(ddmonthyy)[0].toString();
		t = t.split(/[\s'-/-]+/);
		return ["20"+t[2],getMonth(t[1]).toString(),t[0]].join('-');
	}
	else if(temp.match(ddmonthapoyy))
	{
		t= temp.match(ddmonthapoyy)[0].toString();
		t = t.split(/[\s'/-]+/);
		return ["20"+t[2],getMonth(t[1]).toString(),t[0]].join('-');
	}
	else if(temp.match(monthddapoyy))
	{
		t= temp.match(monthddapoyy)[0].toString();//return t;
		//t = t.split(/(?:|[\s'/-])+/);
		return ["20"+t[6]+t[7],getMonth(t[0]+t[1]+t[2]).toString(),t[3]+t[4]].join('-');
	}
	else
	{
		return "null";
	}
	
	
	}


	""")

	result = f(text)

	print(len(text))
	if(len(text)<20):
		with open('test.csv', 'a') as f:
			if(result != None):
				wtr = csv.writer(f, delimiter= ' ')
				print(str(sys.argv[1])+str('\t null text \t')+str(result))
		    		wtr.writerow(str(sys.argv[1])+str('\t null text \t')+str(result))
			else:
				wtr = csv.writer(f, delimiter= ' ')
				print(str('\t null text \t')+"null")
		    		wtr.writerow(str('\t null text \t')+"null")
	else:
		with open('test.csv', 'a') as f:
			if(result != None):
				wtr = csv.writer(f, delimiter= ' ')
				print(str(sys.argv[1])+"\t"+str(result))
		    		wtr.writerow(str(sys.argv[1])+"\t"+str(result))
			else:
				wtr = csv.writer(f, delimiter= ' ')
				print("null")
		    		wtr.writerow("null")


