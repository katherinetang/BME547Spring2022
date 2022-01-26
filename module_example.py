print("This is the database module and python calls it {}".format(__name__))

import blood_calculator as bc

# from blood_calculator import * #calls all the functions, don't need modifier, but don't know where it came from

# from analysis import check_HDL

HDL_value = 55

classification = bc.check_HDL(HDL_value)
print("55 is {}".format(classification))
x = check_LDL(200)
