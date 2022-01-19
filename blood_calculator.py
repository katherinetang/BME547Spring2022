def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1-HDL")
        print("2-LDL")
        print("3-Total Cholesterol")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver();
        elif choice == "2":
            LDL_driver();
        elif choice == "3":
            cholesterol_driver();
    return

def accept_input(test_name):
    entry = input("Enter the {} test result:".format(test_name))
    return int(entry)

def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)
    return
    
def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal";
    elif 60 > HDL_value >= 40:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer;

def check_LDL(LDL_value):
    if LDL_value < 130:
        answer = "Normal";
    elif 130<= LDL_value <=159:
        answer = "Borderline high"
    elif 160<= LDL_value <=189:
        answer = "High"
    else:
        answer = "Very high";
    return answer;
    
def check_cholesterol(cholesterol_value):
    if cholesterol_value < 200:
        answer = "Normal";
    elif 200<=cholesterol_value <=239:
        answer = "Borderline high";
    else:
        answer = "High";
    return answer;

def HDL_driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
    print_result("HDL", HDL_value, classification)

def LDL_driver():
    LDL_value = accept_input("LDL")
    classification = check_LDL(LDL_value) 
    print_result("LDL", LDL_value, classification)

def cholesterol_driver():
    cholesterol_value = accept_input("total cholesterol")
    classification = check_cholesterol(cholesterol_value)
    print_result("total cholesterol", cholesterol_value, classification)

interface();
