#!/usr/bin/python
# -*- coding: utf-8 -*
# Ma Friendo : JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614 )
##############################
   ## Check Daily Visitor Website  ##
### Thanks To :  StatsHow.com ###
##############################
import requests,re,os
from colorama import Fore


print("""

               __
              / _)
     _/\/\/\_/ /
   _|         /
 _|  (  | (  |
/__.-'|_|--|_|  
=============[ StatsHow | Check Daily Visitor Website ]

""")

Url = raw_input(Fore.WHITE+ "URL :~$ ")
Statswhat = requests.get("https://www.statshow.com/www/"+Url)
if "Website Worth" in Statswhat.content:
	Daily = re.findall('<span class="red_bold">(.*?)</span>', Statswhat.content)
	print('Daily Pageviews: '+Fore.GREEN + Daily[0] +Fore.WHITE)
	print('Daily Visitors: '+Fore.GREEN+ Daily[1] +Fore.WHITE)

reloadboom = raw_input("* Want To Repeat This Program Again ? Y/N : ")
if reloadboom == "Y" or reloadboom == "y":
	os.system("python2 Statshow.py")
else:
	print(" Bye ~(^_^~) ")

######COPY AND TYPED BY SHIN_#####
	
	
	