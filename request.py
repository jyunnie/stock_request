# -*- coding:utf-8 -*-
import urllib
import urllib2
import MySQLdb
import datetime
import time
#import mysql.connector
autoincrement_id = 0

def get_data(max_num):
    counter =0
    for x in range(max_num):
        stock_number = '601%03d' % counter
        req = urllib2.Request('http://hq.sinajs.cn/list=sh'+stock_number)
        response = urllib2.urlopen(req)
        data = response.read()
        words = data.split(',',31)
        for word in words:
            store(words)
        counter+= 1
        

def store(words):
    result = dict()
    result['ID'] = autoincrement_id
    result['stock_name'] = words[0]
    result['open_today'] = words[1]
    result['close_yesterday'] = words[2]
    result['price_now']= words[3]
    result['high_today']= words[4]
    result['low_today']= words[5]
    result['buy_one_price']= words[6]
    result['sell_one_price']= words[7]
    result['transaction_now']= words[8]
    result['transvalue_now']= words[9]
    result['buy_one_qty']= words[10]
    result['buy_one_price']= words[11]
    result['buy_two_qty']= words[12]
    result['buy_two_price']= words[13]
    result['buy_three_qty']= words[14]
    result['buy_three_price']= words[15]
    result['buy_four_qty']= words[16]
    result['buy_four_price']= words[17]
    result['buy_five_qty']= words[18]
    result['buy_five_price']= words[19]
    result['sell_one_qty']= words[20]
    result['sell_one_price']= words[21]
    result['sell_two_qty']= words[22]
    result['sell_two_price']= words[23]
    result['sell_three_qty']= words[24]
    result['sell_three_price']= words[25]
    result['sell_four_qty']= words[26]
    result['sell_four_price']= words[27]
    result['sell_five_qty']= words[28]
    result['sell_five_price']= words[29]
    result['quote_date']= words[30]
    result['quote_time']= words[31]
    autoincrement_id += 1
    yield result

def main():
   max_num = 101
   time_now=time.strftime("%H %M %S").split()
   print time_now
   if time_now[0] >= '09' and  time_now[0] <= '11':
	if time_now[1] >= '15': 
           print 'Morning Session'
	   #get_data(max_num)
   elif time[0] >= '13' and time_now[0] <= '15':
      print "Afternoon Session"
      #get_data(max_num)
   else:
      print "Not time to get data"
    #  get_data(max_num)
   
  
#seq = 'http://hq.sinajs.cn/list=sh601006'
#for x in range[1,10]:
#	seq += 1
#	print seq

main()
