# DateExtraction

This repo contains the source code for system which extracts date from images in the required format.

To ease this functionality an API has been deployed in Heroku platform.
API Details:
1)URL : "http://npranav10-extractdate.herokuapp.com/extractDate"
2) The API accepts only base64 encoded bytes of an image
3) Request Header : "application/json" in the form
{“base_64_image_content”: <base_64_image_content>}
4) Response Header : "application/json" in the form

If date is present:
{“date”: “YYYY-MM-DD”}
If date is not present:
{“date”: null}



Behind the Scenes:
1) Flask framework to a make app in Python to serve the API requests. 
2) Python driver code: "pytesseract" package to extract text from image and using advanced regex matching using "js2py" package to match all possible data formats. 
3) Heroku platform is used to host the API.

