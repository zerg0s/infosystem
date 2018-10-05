import urllib.request
import urllib.parse
import os
response = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
r = response.read().decode("cp1251")
r = str(r)
r = r[r.find('Бразильский реал'):]
r = float(r[r.find('<Value>')+7:r.find('</Value>')].replace(',', '.'))
print('1 рубль стоит ', 1/r, 'Бразильских реалов')
os.system('pause')
