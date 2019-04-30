# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import base64
http_url='https://api-cn.faceplusplus.com/imagepp/v1/mergeface'
key = "JYbBNFD0oYwTCU0IVqpDRN-EWaB2UsiC"
secret = "E37UC6ZUWFmmQGSXmp_Mt36XENv6q4gI"
filepath = r"/Users/heliwei/WorkSpace/TbTy/hlw.jpg"
mergefile = r"/Users/heliwei/WorkSpace/TbTy/xyjy.jpg"
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'template_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s' % boundary)
fr=open(mergefile,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'merge_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'template_rectangle')
data.append('116,70,152,152')
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'merge_rate')
data.append('50')
#data.append('--%s' % boundary)
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
	#req.add_header('Referer','http://remotserver.com/')
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()

        spliQrcont = qrcont.split('\"')
        rawFile = open(r'/Users/heliwei/WorkSpace/TbTy/rawData.txt','w')

        #rawFile.write(qrcont)
        rawFile.write(spliQrcont[5])
        rawFile.close()
        rawFile = open(r'/Users/heliwei/WorkSpace/TbTy/rawData.txt','rb')
        imageFile = open(r'/Users/heliwei/WorkSpace/TbTy/merge.jpg','wb')
        baseTest = base64.decode(rawFile,imageFile)
        rawFile.close()
        imageFile.close()

except urllib2.HTTPError as e:
    print e.read()
