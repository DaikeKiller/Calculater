def checkHDL(HDL_result):
	if HDL_result >= 60:
		return "Normal"
	elif 40 <= HDL <60:
		return "Borderline low"
	else:
		return "low"

def cholestoral_interface():
	

def interface():
	print('My calculator program')
	keep_running == True
	while keep_running:		
		print('Options:')
		print('9 - Quit')
		choice = input('Enter your choice:')
		if choice == '9':
			keep_running = False
	return

if __name__ == '__main__':
	interface()
