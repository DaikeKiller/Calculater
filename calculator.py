def interface():
	print('My calculator program')
	print('Options:')
	print('9 - Quit')
	choice = input('Enter your choice:')
	if choice == '9':
		return

if __name__ == '__main__':
	interface()
