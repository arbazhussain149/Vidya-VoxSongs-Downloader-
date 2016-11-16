from lxml import html
import requests
import wget
import time

print """ Just Run : python vidya.py 
			Requires : wget Module 
			pip install wget """
print "\n" * 2
raw_input("> Are you Ready ? Hit Enter \n")


start_page = requests.get('http://www.vidyavox.com/music')
tree = html.fromstring(start_page.text)

name = tree.xpath('//a[@class="link"]/text()')
artist = tree.xpath('//div[@class="artist"]/text()')
song = tree.xpath('//a[@class="link"]/@href')

for i in name:
		print "Song Name's Available : ",i


raw_input("> Press Enter to Download All Songs")
time.sleep(3)
for j in song:
	wget.download(j)
	print "Downloading : ",j

