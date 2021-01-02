import hashlib
from random import *
from multiprocessing import Process, Queue

def work(start, end, key):
	for j in range(start,end):
		tmp=str(j)
		#print(tmp)
		data=tmp+"salt_for_you"
		for i in range(0,500):
			data = hashlib.sha1(data.encode('utf-8')).hexdigest()
		
		if data == key:
		 	print(tmp+"salt_for_you")
		 	break

if __name__ == "__main__":
	pr1 = Process(target=work, args=(10000000,20000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	pr2 = Process(target=work, args=(20000000,30000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	pr3 = Process(target=work, args=(30000000,40000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	pr4 = Process(target=work, args=(40000000,50000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	pr5 = Process(target=work, args=(50000000,60000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	pr6 = Process(target=work, args=(60000000,70000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	pr7 = Process(target=work, args=(70000000,80000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	pr8 = Process(target=work, args=(80000000,90000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	pr9 = Process(target=work, args=(90000000,100000000,"76f7863a772c7844d9c9fd016dba5bac3d7f7046"))
	
	pr1.start()
	pr2.start()
	pr3.start()
	pr4.start()
	pr5.start()
	pr6.start()
	pr7.start()
	pr8.start()
	pr9.start()
	
	pr1.join()
	pr2.join()
	pr3.join()
	pr4.join()
	pr5.join()
	pr6.join()
	pr7.join()
	pr8.join()
	pr9.join()

