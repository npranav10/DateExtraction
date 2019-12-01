import os
path = '/home/hulk/npranav10/Fyle/local_test/Receipts'
files = os.listdir(path)
i = 1

for index, file in enumerate(files):
	os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
	i = i+1
