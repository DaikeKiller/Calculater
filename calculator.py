def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline low"
    else:
        return "low"

def check_LDL(LDL):
	if LDL < 130:
		return 'Normal'
	elif LDL >= 130 and LDL <= 159:
		return "borderline high"
	elif LDL >= 160 and LDL <= 189:
		return "high"
	else:
		return "very high"

def cholestoral_interface():
    print("Cholesterol check")
    chol_input = input("Enter your cholestoral test result: ")
    chol_data = chol_input.split("=")
    if chol_data[0] == "HDL":
        result = check_HDL(int(chol_data[1]))
        print("The result is {}".format(result))
    if chol_data[0] == "LDL":
        result = check_LDL(int(chol_data[1]))
        print("The result is {}".format(result))


def interface():
    print("My calculator program")
    keep_running = True
    while keep_running:
        print("Option: ")
        print("1 - Cholesterol Checks")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
           keep_running = False
        elif choice == '1':
            cholestoral_interface()
    return

if __name__ == "__main__":
    interface()
