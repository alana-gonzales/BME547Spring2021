def interface():
    print("Blood Test Analysis")
    while True:
        print("\nOptions")
        print("1 - HDL Analysis")
        print("2 - LDL Analysis")
        print("9 - Quit")
        choice = input("Enter an option: ") # input will always return a string
        if choice == "9":
            return
        elif choice == "1":
            hdl = input("\nPlease enter your HDL value: ")
            return hdl
        elif choice == "2":
            hdl = input("\nPlease enter your LDL value: ")
            return ldl

def check_HDL(user_hdl):
    if user_hdl >= 60:
        hdl_level = "Normal"
    elif 40 <= user_hdl < 60:
        hdl_level = "Borderline Low"
    else:
        hdl_level = "Low"
    return hdl_level

def check_LDL(user_ldl):
    if user_ldl < 130:
        ldl_level = "Normal"
    elif 130 <= user_ldl <= 159:
        ldl_level = "Borderline High"
    elif 160 <= user_ldl <= 189:
        ldl_level = "High"
    else:
        ldl_level = "Very High"
    return ldl_level

def HDL_driver():
    hdl = interface()
    hdl = int(hdl)
    hdl_level = check_HDL(hdl)
    print("Your HDL value is " + str(hdl))
    print(hdl_level)

HDL_driver()
