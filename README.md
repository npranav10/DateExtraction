# DateExtraction

This repo contains the source code for system which extracts date from images in the required format.

To ease this functionality an API has been deployed in Heroku platform.


#### API Details:
1) URL : "http://npranav10-extractdate.herokuapp.com/extractDate"
2) The API accepts only base64 encoded bytes of an image
3) Request Header : "application/json" in the form {“base_64_image_content”: <base_64_image_content>}
4) Response Header : "application/json" in the form

If date is present:
{“date”: “YYYY-MM-DD”}
If date is not present:
{“date”: null}



#### Behind the Scenes:
1) Flask framework is used to a make a web app in Python to serve the API requests. 
2) Python driver code: "pytesseract" package is used to extract text from image and "js2py" package for advanced regex matching to match all possible data formats. 
3) Heroku platform is used to host the API.

#### Steps to run the program locally:
1) `git clone https://github.com/npranav10/DateExtraction`
2) `cd ./DateExtraction/localTest`
3) `python test.py ./pathtoimage/imagename.jpg`

A short info about files:


test.py : Driver code to run extract date from Images. Takes in location of an image as input.
e.g : `python test.py ./Receipts/1.jpg`

devtest.py : A script to automate execution of test.py for all images in the Receipts folder.
e.g : `python devtest.py`

imageTobase64.py : Encodes an image to base64 bytes and prints it in the console.


***********************************************************************************************************************************************
An article which will cover all aspects of designing and deploying this system will be publish soon and keep checking this page for the article's link.
***********************************************************************************************************************************************