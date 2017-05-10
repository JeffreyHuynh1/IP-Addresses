import re

def menu():
	print("********************Menu********************")
	print("1.Print All IP Addresses")
	print("2.Search For an IP Address")
	print("3.Quit")

def main():
	file=open("list_of_ips (1).txt", "r")
	ips=[]
	exit= False
	for line in file:	
		if re.findall(r'\d+\.\d+\.\d+\.\d+', line) != []:
			ips.append(re.findall(r'\d+\.\d+\.\d+\.\d+', line))

	while(exit==False):
		menu()
		x=input("Enter Your Choice: ")

		if x == 1:
			for addresses in ips:
				for address in addresses:
					print address
			print("\n")

		elif x ==2:
			search=raw_input("Enter an IP Address: ")		
			found=False

			for addresses in ips:
				for address in addresses:
					if search == address:
					
						print("Valid IP Address")
						print("\n")
						found=True
						break

			if found==False:
				print("Invalid IP Address")
				print("\n")

		elif x == 3:
			print("Goodbye")
			exit=True
		else:
			print("Not a valid choice")
			print("\n")



main()