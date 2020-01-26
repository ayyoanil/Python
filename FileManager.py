fileHandle = open('test.txt', 'w')
fileHandle.write('This is the first line \n')
fileHandle.write('This is the second line \n')
fileHandle.close()

fileHandle = open('test.txt', 'r')
text = fileHandle.read()
print(text)
fileHandle.close()
