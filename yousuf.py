from playsound import playsound
import requests
import time

f= open('data.txt', 'w')
LOOP = True
it = 0
values = []
while LOOP:
	
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
		print(it,'; Congrats asshole, the Bitcoin value is dropping:', valueit)
	else:
		print(it,'; Congrats, the Bitcoin value is above the previous:', valueit)

	f.write(valueit + "\n")

	time.sleep(1)
	it += 1


	