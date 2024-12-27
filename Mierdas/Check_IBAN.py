IBAN_num = int(input("Enter the IBAN number: \n"))




def Check_IBAN():

    IBAN_status = False

    while IBAN_status == False:

        IBAN_num = int(input("Incorrect format, please enter an IBAN number formated correctly: \n "))
        
        if IBAN_num == 3:
            print(f"Your IBAN number is : {IBAN_num}")
            IBAN_status = True
        

Check_IBAN()