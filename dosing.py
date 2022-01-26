"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""


#def dose_amount():

def input_data():
    print("Day One Dosing Guidelines")
    print("")
    print("Choose diagnosis:")
    print("1 - Acute otitis media")
    print("2 - Acute bacterial sinusitis")
    print("3 - Community-acquired pneumonia")
    print("4 - Pharyngitis/tonsilitis")
    diagnosis = int(input("Enter a number: "))
    weight_input = input("Enter weight: ")
    return diagnosis, weight_input
    

def analysis(diagnosis, weight_input):
    weight_data = weight_input.split(" ")
    weight = float(weight_data[0])
    units = weight_data[1]
    if units == "lb":
        weight = weight / 2.205
    dosages_mg_per_kg = [30, 10, 10, 12]
    dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
    dosage_mg_first_day = weight * dosage_mg_per_kg
    return dosage_mg_first_day, weight

def output(weight, dosage_mg_per_kg):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(weight))
    print("  the correct dosage is {:.1f} mg the first day"
          .format(dosage_mg_first_day))


if __name__ == '__main__':
    #dose_amount()
    diagnosis, weight_input = input_data()
    dosage_mg_first_day, weight = analysis(diagnosis, weight_input)
    output(weight, dosage_mg_first_day)

