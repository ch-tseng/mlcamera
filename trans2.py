# -*- coding: utf-8 -*-

import time
import urllib2
import goslate

#gs = goslate.Goslate()
proxy_handler = urllib2.ProxyHandler({"http" : "proxy.hinet.net :80"})
proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),
                                    urllib2.HTTPSHandler(proxy_handler))
gs_with_proxy = goslate.Goslate(opener=proxy_opener)

fo = open("synset.txt", "r")
fw = open('synset-trans.txt', 'w')

print "File name: ", fo.name

ii = 0
for line in fo.readlines():            
    line = line.strip()                  
    print (line)
    trans = gs_with_proxy.translate(line[10:], 'zh-TW')
    idNum = line[:10]
    txtTrans = ("{} {}".format(idNum.encode('utf-8').strip(), trans.encode('utf-8').strip()) )
    print ("{}   -->".format(ii, txtTrans) )
    fw.write(txtTrans + '\n')

    time.sleep(2)
    ii += 1

fo.close()
fw.close()

#print(google('This is a pen!', dst = 'zh-TW'))
