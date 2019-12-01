import os


if __name__ == '__main__': 
	i = 1
	for filename in os.listdir("./Receipts/"):
		arg = "python test.py ./Receipts/"+str(filename)
		#print(arg)
		print("###############################################################")		
		print("Image number : "+str(i))
		print("###############################################################")
		os.system(arg)
		i = i + 1


