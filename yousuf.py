from playsound import playsound
import requests
import time
#import os
bitdata = []


def bitcoin():
	it = 0
	values = []
	bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
	response = requests.get(bitcoin_api_url)
	response_json = response.json()

	type(response_json)

	response_raw = str(response_json[0])
			
	values.append(response_raw[81:92])

	valueit = values[it]
	calc = values[it-1]

	if float(valueit)<float(calc):
		playsound('audio.mp3')
		print(it,'; ↓ ,the Bitcoin value is dropping:', valueit)
	elif float(valueit)>float(calc):
		print(it,'; ↑ the Bitcoin value is rising', valueit)
	else:
		print(it,'; -- the Bitcoin value is not moveing', valueit)

	
	bitdata.append(valueit)
		#f = open('data.txt', 'w', os.O_NONBLOCK)
		#f.write(valueit + "\n")
		#f.close()
	it += 1