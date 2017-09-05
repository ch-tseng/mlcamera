# -*- coding: utf-8 -*-

import time
from translation import baidu, google, youdao, iciba

fo = open("synset.txt", "r")
fw = open('synset-trans.txt', 'w')

print "File name: ", fo.name

ii = 0
for line in fo.readlines():            
    line = line.strip()                  
    txtWords = (line[10:]).strip().encode('utf-8')
    idNum = line[:10].strip().encode('utf-8')
    trans = google(txtWords, dst = 'zh-TW') 
    #trans = youdao(line[10:], dst = 'zh-CN')
    txtTrans = ("{} {}".format(idNum, trans.encode('utf-8')) )
    print ("{} {} --> {}".format(ii, line, txtTrans) )
    fw.write(txtTrans + '\n')

    time.sleep(0.3)
    ii += 1

fo.close()
fw.close()

#print(google('This is a pen!', dst = 'zh-TW'))
