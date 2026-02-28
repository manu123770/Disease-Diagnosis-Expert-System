# Rule Based Expert System
# AI Internship project-SyntecxHub
print("\n=== Welcome to Disease Diagnosis System ===\n")
while True:
    print("\nPlease answer with yes/no:\n")
    fever=input("Do you have fever?").lower()
    cough=input("Do you have cough?").lower()
    headache=input("Do you have headache?").lower()
    nausea=input("Do you feel nausea?").lower()
    chest_pain=input("Do you have chest_pain(pressure/tightness)?").lower()
    breathlessness=input("Do you feel short ness of breadth?").lower()
    rash=input("Do you have skin rash?").lower()
    print("\n--- Diagnosis Result---")
    #Rule1:Flu
    if fever=="yes"and cough=="yes":
        print("You may have flu.")
    #Rule2:Migraine
    elif headache=="yes"and nausea=="yes":
        print("You may have Migraine.")
    #Rule3:Heart-related issue(improved)
    elif chest_pain=="yes"and breathlessness=="yes":
        print("Warning:Possible heart related issue.Consult a doctor immediately.")
    #Rule4:Viral Infection
    elif fever=="yes"and rash=="yes":
        print("You may have Viral Infection.")
    #Default case
    else:
        print("Symptoms unclear.Please Consult a doctor.")
    choice=input("\nDo you want to check again?(yes/no):").lower()
    if choice!="yes":
        print("Thank you for using the expert system!")
    break


