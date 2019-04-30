import base64
inputRead = open('/Users/heliwei/Downloads/data.txt','rb')

outputWrite = open('/Users/heliwei/Downloads/data.jpg','wb') 
base64Test = base64.decode(inputRead,outputWrite)
