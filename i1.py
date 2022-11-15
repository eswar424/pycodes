import os, ipaddress

os.system("cls")

while True:
	ip = input("enter ip")
	try:
		print(ipaddress.ip_address(ip))
	except:
		print("-" *50)
		print("ip is not valid")
	finally:
		if ip == "q":
           print('script Finished')
        break