import base64

def replaceit(data):
	data = data.replace("8",")")
	data = data.replace("7","(")
	data = data.replace("6","*")
	data = data.replace("5","&")
	data = data.replace("4","^")
	data = data.replace("3","$")
	data = data.replace("2","@")
	data = data.replace("1","!")
	
	return data

if __name__ == '__main__':
	_id = 'admin'
	_pw = 'nimda'

	for i in range(0,20):
		_id = base64.b64encode(_id.encode("UTF-8")).decode("UTF-8")
		_pw = base64.b64encode(_pw.encode("UTF-8")).decode("UTF-8")

	_id = replaceit(_id)
	_pw = replaceit(_pw)

	print(_id+"\n")
	print(_pw)

