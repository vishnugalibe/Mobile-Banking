customername=input("\nWhat Should I Call You ?\t ")
print("\nDear",customername,",\n\nHello! Welcome to our new MOBILE BANKING SYSTEM.\nWhere Banking runs on your Finger Tips.\nIf you are interested ,\nfollow the instructions carefully :)\n\n")

# creating the function of count down timer
def timer():
    import time
    timer_second=5
    while True:
        print("\t",timer_second)
        timer_second-=1
        time.sleep(1)
        
        if timer_second==0:
            print("\nMini Statement Will Generated Below")
            break
           
#asking do you have bank account
print("------------------------------------------")
print("\t MOBILE BANKING")
print("------------------------------------------\n")
print("Do you have BANK ACCOUNT in Legend Mobile Banking: ")
print("1. Yes\n2. No\n")
a=int(input("Enter the option: "))

#if asnwer was yes then it causually shows the login options
#but it only says to create a account
#login
if a==1:
    print("\nLogin to the BANK ACCOUNT: \n")
    print("LOGIN: ")
    print("------------------------------------------")
    account=int(input("Account Number : "))
    passcode=int(input("Login Passcode : "))
    print("------------------------------------------")
    print("\n------------------------------------------")
    print("\tBank Account doesn't exist\nCreate a account by selecting Option 2\n\t\tThank You")
    print("------------------------------------------")
    
 #if answer was no then it asks for details and then login according to your interest
 #sign up    
elif a==2:
    def atm():
        print("\nSign up to create a BANK ACCOUNT: ")
        #all details
        print("\nEnter Bank Details: ")
        print("------------------------------------------")
        print("\tBANK ACCOUNT DETAILS  ")
        print("------------------------------------------")
        print(("PERSONAL DETAILS : "))
        print("------------------------------------------")
        #name should be entered here
        name=input("1. Enter Full Name      : ")
        #age of the person should be enetredf and it must be above 18
        age=int(input("2. Enter Age            : "))
        if age>=18:
            #gender must be 2 male and female 
            gender=input("3. Enter Gender         : ")
            if gender=="Male" or gender=="male" or gender=="MALE" or gender=='M' or gender=='m' or gender=="Female" or gender=="female" or gender=="FEMALE" or gender=='f' or gender=='F':
                #mobile number should be only 10 digits
                mobile=int(input("4. Enter Mobile Number  : +91 "))
                if mobile>=1000000000 and mobile<=9999999999:
                    #address should be entered
                    address=input("5. Enter Address        : ")
                    print("------------------------------------------")
                    print("BANK DETAILS : ")
                    print("------------------------------------------")
                    #account number should only contain 10 digits
                    import random
                    accnum=random.randint(1000000000,9999999999)
                    print("6. Generated Account Number       :",accnum)
                    if accnum>=1000000000 and accnum<=9999999999:
                        #initial shouldn't be more than limit i.e 2000 to upto 100000
                        balance=int(input("7. Enter Initial Amount           : "))
                        if balance>=2000 and balance<=100000:
                            #login passcode must be 6 digits
                            loginpin=int(input("8. Enter 6 Digits Login Passcode  : "))
                            if loginpin>=100000 and loginpin<=999999:
                                conpin=int(input("|| Enter Confirm Passcode         : "))
                                if loginpin==conpin:
                                    b=int(input("\nDo You Want To Change Any Details: \n1. Yes\n2. No\n\nEnter Option: "))
                                    #from here it ask for the update of the person from his detials taht he entered 
                                    if b==1:
                                        update=int(input("\nEnter Serial Number Of Your Details You Want To Update: "))
                                        print("\n")
                                        if update==1:
                                            name1=input("\nEnter Full Name         : ")
                                            if name==name1:
                                                print("\n------------------------------------------")
                                                print("\tAlready Existing Name")
                                                print("------------------------------------------")
                                            else:
                                                print("Updated Full Name       : ",name.replace(name,name1))
                                                print("\n------------------------------------------")
                                                print("\tDetails Saved Successfully")
                                                print("------------------------------------------")
                                            
                                                #asking the user do you want to login or not
                                                ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                                if ulogin==1:
                                                    
                                                    #now login into atm system
                                                    print("\n\nLOGIN: ")
                                                    print("------------------------------------------")
                                                    account=int(input("Account Number : "))
                                                    if account==accnum:
                                                        passcode=int(input("Login Passcode : "))
                                                        if passcode==loginpin:
                                                            print("------------------------------------------")
                                                            print("\t\tLogin Successfully")
                                                            print("------------------------------------------")
                                                            print("\n\n")
                                                            print("\t•••••••• ATM ••••••••")
                                                            print("------------------------------------------")
                                                            print("Hello",name1,"...")
                                                            print("Welcome to ATM")
                                                            
                                                            # displaying the language on the screen
                                                            print("------------------------------------------")
                                                            print("\tINSERT DEBIT CARD")
                                                            print("------------------------------------------")
                                                            print("\nSelect Language: \n")
                                                            print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                            
                                                            # selecting the language
                                                            language=int(input("Enter option number for Langauge Selection: "))
                                                            
                                                            #telugu version
                                                            if language==1:
                                                                
                                                                #typing the passcode
                                                                passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                                if passcode>=1000 and passcode<=9999:
                                                                    print("\n------------------------------------------")
                                                                    print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                                    print("------------------------------------------")
                                                                    
                                                                    #options in ATM
                                                                    print("ఎంపికను ఎంచుకోండి: \n")
                                                                    print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                                
                                                                    #after passcode showing the options: 
                                                                    # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                    # selection is about the options in ATM
                                                                    
                                                                    selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                                
                                                                    #deposit
                                                                    if selection==1:
                                                                        print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                        #deposite pin must be only 4 digits
                                                                        depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                        if depin==passcode:
                                                                            #deposite amount has limit i.e 100 to 100000
                                                                            depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                            if depamo>=100 and depamo <=100000:
                                                                                print("\n------------------------------------------")
                                                                                print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                                #asking for mini statement
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\ndeposited amount : ",depamo)
                                                                                    print("balance amount   : ",balance+depamo,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                            print("------------------------------------------")
                                                                
                                                                    #withdrawal
                                                                    elif selection==2:
                                                                        print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                        drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                        if drapin==passcode:
                                                                            draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                            if draw<=balance:
                                                                                print("\n------------------------------------------")
                                                                                print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                                print("------------------------------------------")                               
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nwithdraw amount : ",draw)
                                                                                    print("balance amount  : ",balance-draw,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                            print("------------------------------------------")
                                                                
                                                                    #change pin 
                                                                    elif selection==3:
                                                                        print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                        chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                        if chapin==passcode:
                                                                            chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                            if chanew!=chapin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nyour new passcode is activated")
                                                                                    print("Balance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                            print("------------------------------------------")
                                                                
                                                                    #balance enquiry
                                                                    elif selection==4:
                                                                        print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                        balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                        if passcode==balpin:
                                                                            print("\n------------------------------------------")
                                                                            print("\tసంతులనం: ",balance)
                                                                            print("------------------------------------------")
                                                                            print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                            opt=int(input("Enter Option: "))
                                                                            if opt==1:
                                                                                timer()
                                                                                print("\n\n------------------------------------------")
                                                                                print("\t\tMINI STATEMENT\t\t")
                                                                                print("------------------------------------------")
                                                                                from datetime import datetime
                                                                                today=datetime.today().date()
                                                                                from datetime import datetime
                                                                                week=datetime.today()
                                                                                print("Date & Day     : ",today,week.strftime("%A"))
                                                                                print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                print("------------------------------------------")
                                                                                print("NAME           : ",name1)
                                                                                print("ACCOUNT NUMBER : ",accnum)
                                                                                print("------------------------------------------")
                                                                                print("\nBalance amount : ",balance,"\n")
                                                                                print("------------------------------------------")
                                                                                print("\t\tTHANK YOU\t\t")
                                                                                print("------------------------------------------")
                                                                            elif opt==2:
                                                                                print("------------------------------------------")
                                                                                print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tNo Option\n\tThank You")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tతప్పు పాస్‌కోడ్")
                                                                            print("------------------------------------------")
                                                                    else: 
                                                                        print("------------------------------------------")
                                                                        print("\tచెల్లని సంఖ్య")
                                                                        print("------------------------------------------")
                                                                elif passcode==0000:
                                                                    print("\n------------------------------------------")
                                                                    print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                                    print("------------------------------------------")
                                                                else:
                                                                    print("\n------------------------------------------")
                                                                    print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                                    print("------------------------------------------")

                                                            #hindi version
                                                            elif language==2:
                                                                #typing the passcode
                                                                passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                                if passcode>=1000 and passcode<=9999:
                                                                    print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                                
                                                                    #options in ATM
                                                                    print("\nविकल्प दर्ज करें: ")
                                                                    print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                                
                                                                    #after passcode showing the options: 
                                                                    # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                    # selection is about the options in ATM
                                                                    selection=int(input("\nविकल्प दर्ज करें: "))
                                                                
                                                                    #deposit
                                                                    if selection==1:
                                                                        print("\nराशि जमा करें: \n")
                                                                        depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                        if depin==passcode:
                                                                            print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                            depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                            if depamo>=100 and depamo <=100000:
                                                                                print("\n------------------------------------------")
                                                                                print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nDeposited Amount : ",depamo)
                                                                                    print("Balance Amount   : ",balance+depamo,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                            print("------------------------------------------")
                                                                
                                                                    #withdrawal
                                                                    elif selection==2:
                                                                        print("\nराशि वापस लें: n")
                                                                        print("न्यूनतम निकासी एक सौ")
                                                                        wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                        if wipin==passcode:
                                                                            draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                            if draw<=balance:
                                                                                print("\n------------------------------------------")
                                                                                print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nWithdraw Amount : ",draw)
                                                                                    print("Balance Amount  : ",balance-draw,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tगलत पासकोड\n\tधन्यवाद")
                                                                            print("------------------------------------------")
                                                                
                                                                    #change pin 
                                                                    elif selection==3:
                                                                        print("\nपासकोड बदलें: ")
                                                                        chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                        if chapin==passcode:
                                                                            chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                            if chanew!=chapin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tनया पासकोड सक्रिय")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nYour New Passcode Is Activated")
                                                                                    print("Balance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tपहले से मौजूद पासकोड")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                            print("------------------------------------------")
                                                                
                                                                    #balance enquiry
                                                                    elif selection==4:
                                                                        print("\nबैलेंस पूछताछ: \n")
                                                                        balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                        if passcode==balpin:
                                                                            print("\n------------------------------------------")
                                                                            print("\tसंतुलन: ",balance)
                                                                            print("------------------------------------------")
                                                                            print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                            opt=int(input("Enter Option: "))
                                                                            if opt==1:
                                                                                timer()
                                                                                print("\n\n------------------------------------------")
                                                                                print("\t\tMINI STATEMENT\t\t")
                                                                                print("------------------------------------------")
                                                                                from datetime import datetime
                                                                                today=datetime.today().date()
                                                                                from datetime import datetime
                                                                                week=datetime.today()
                                                                                print("Date & Day     : ",today,week.strftime("%A"))
                                                                                print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                print("------------------------------------------")
                                                                                print("NAME           : ",name1)
                                                                                print("ACCOUNT NUMBER : ",accnum)
                                                                                print("------------------------------------------")
                                                                                print("\nBalance  Amount : ",balance,"\n")
                                                                                print("------------------------------------------")
                                                                                print("\t\tTHANK YOU\t\t")
                                                                                print("------------------------------------------")
                                                                            elif opt==2:
                                                                                print("------------------------------------------")
                                                                                print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tNo Option\n\tThank You")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tग़लत पासकोड")
                                                                            print("------------------------------------------")
                                                                    else: 
                                                                        print("------------------------------------------")
                                                                        print("\tअमान्य संख्या")
                                                                        print("------------------------------------------")
                                                                elif passcode==0000:
                                                                    print("------------------------------------------")
                                                                    print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                                    print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                                    print("------------------------------------------")
                                                            #9tabs english version//
                                                            elif language==3:
                                                                #typing the passcode
                                                                passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                                if passcode>=1000 and passcode<=9999:
                                                                    print("------------------------------------------")
                                                                    print("\tPasscode Confirmed\t")
                                                                    print("------------------------------------------\n")
                                                                
                                                                    #options in ATM 
                                                                    print("Enter Options: ")
                                                                    print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                                
                                                                    #after passcode showing the options: 
                                                                    # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                    # selection is about the options in ATM
                                                                    selection=int(input("Enter Options: "))
                                                                
                                                                    #deposit
                                                                    if selection==1:
                                                                        print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                        depin=int(input("\nEnter passcode to deposite: "))
                                                                        if depin==passcode:
                                                                            print("\tMinimum deposit one hundred to one lakh \n")
                                                                            depamo=int(input("\nEnter the deposit amount: "))
                                                                            if depamo>=100 and depamo <=100000:
                                                                                print("\n------------------------------------------")
                                                                                print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nDeposited Amount : ",depamo)
                                                                                    print("Balance Amount   : ",balance+depamo,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\t",depamo,"is can't be deposited")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tIncorrect Passcode\n\tThank You")
                                                                            print("------------------------------------------")
                                                                
                                                                    #withdrawal
                                                                    elif selection==2:
                                                                        print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                        print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                        wipin=int(input("Enter passcode to withdrawal: "))
                                                                        if wipin==passcode: 
                                                                            draw=int(input("\nEnter the withdrawal amount: "))
                                                                            if draw<=balance:
                                                                                print("\n------------------------------------------")
                                                                                print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nwithdraw amount : ",draw)
                                                                                    print("balance amount  : ",balance-draw,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\t",draw,"can't be withdraw")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tIncorrect Passcode\n\tThank You")
                                                                            print("------------------------------------------")
                                                                
                                                                    #change pin 
                                                                    elif selection==3:
                                                                        print("\nCHANGE THE PASSCODE: ")
                                                                        chapin=int(input("\nenter the old pin: "))
                                                                        if chapin==passcode:
                                                                            chanew=int(input("\nenter new pin: "))
                                                                            if chanew==chapin:
                                                                                print("\nalready existing passcode")
                                                                            else:    
                                                                                print("\n------------------------------------------")
                                                                                print("\tNew Passcode Activated")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name1)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nYour New Passcode Is Activated")
                                                                                    print("Balance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tIncorrect Passcode\n\tThank You")
                                                                            print("------------------------------------------")
                                                                
                                                                    #balance enquiry
                                                                    elif selection==4:
                                                                        print("\nBALANCE ENQUIRY: ")
                                                                        balpin=int(input("\nEnter the passcode to check balance: "))
                                                                        if passcode==balpin:
                                                                            print("\n------------------------------------------")
                                                                            print("\tBalance: ",balance)
                                                                            print("------------------------------------------")
                                                                            print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                            opt=int(input("Enter Option: "))
                                                                            if opt==1:
                                                                                timer()
                                                                                print("\n\n------------------------------------------")
                                                                                print("\t\tMINI STATEMENT\t\t")
                                                                                print("------------------------------------------")
                                                                                from datetime import datetime
                                                                                today=datetime.today().date()
                                                                                from datetime import datetime
                                                                                week=datetime.today()
                                                                                print("Date & Day     : ",today,week.strftime("%A"))
                                                                                print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                print("------------------------------------------")
                                                                                print("NAME           : ",name1)
                                                                                print("ACCOUNT NUMBER : ",accnum)
                                                                                print("------------------------------------------")
                                                                                print("\nBalance Amount : ",balance,"\n")
                                                                                print("------------------------------------------")
                                                                                print("\t\tTHANK YOU\t\t")
                                                                                print("------------------------------------------")
                                                                            elif opt==2:
                                                                                print("------------------------------------------")
                                                                                print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                print("------------------------------------------")
                                                                            else:    
                                                                            
                                                                                print("------------------------------------------")
                                                                                print("\tNo Option\n\tThank You")
                                                                                print("------------------------------------------")
                                                                                
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tIncorrect Passcode")
                                                                            print("------------------------------------------")
                                                                    else: 
                                                                        print("------------------------------------------")
                                                                        print("\tInvalid Number")
                                                                        print("------------------------------------------")
                                                                elif passcode==0000:
                                                                    print("\n------------------------------------------")
                                                                    print("\tWeak Passcode\n\tTry Another")
                                                                    print("------------------------------------------")
                                                                else:
                                                                    print("\n------------------------------------------")
                                                                    print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                                    print("------------------------------------------")
                                                                    print("\n\t\tThank You")
                                                            else:
                                                                print("------------------------------------------")
                                                                print("\tInvalid Number")
                                                                print("------------------------------------------")
                                                        else:
                                                            print("------------------------------------------")
                                                            print("\tIncorrect Passcode")
                                                            print("------------------------------------------")
                                                    else:
                                                        print("------------------------------------------")
                                                        print("\tAccount Number Not Exist")
                                                        print("------------------------------------------")   
                                                elif ulogin==2:
                                                    print("\n------------------------------------------")
                                                    print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                                    print("------------------------------------------")
                                                else:
                                                    print("\n------------------------------------------")
                                                    print("\tNo Option\n\tThank You")
                                                    print("------------------------------------------")            
                                        elif update==2:
                                            age1=int(input("\nEnter Age               : "))
                                            if age==age1:
                                                print("\n------------------------------------------")
                                                print("\tAlready Existing Age")
                                                print("------------------------------------------")
                                            else:    
                                                if age1>=18:
                                                    print("Updated Age             : ",age1) 
                                                    print("\n------------------------------------------")
                                                    print("\tDetails Saved Successfully")
                                                    print("------------------------------------------")
                                                
                                                    ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                                    if ulogin==1:
                                                        #now login into atm system
                                                        print("\n\nLOGIN: ")
                                                        print("------------------------------------------")
                                                        account=int(input("Account Number : "))
                                                        if account==accnum:
                                                            passcode=int(input("Login Passcode : "))
                                                            if passcode==loginpin:
                                                                print("------------------------------------------")
                                                                print("\t\tLogin Successfully")
                                                                print("------------------------------------------")
                                                                print("\n\n")
                                                                print("\t•••••••• ATM ••••••••")
                                                                print("------------------------------------------")
                                                                print("Hello",name,"...")
                                                                print("Welcome to ATM")
                                                                
                                                                # displaying the language on the screen
                                                                print("------------------------------------------")
                                                                print("\tINSERT DEBIT CARD")
                                                                print("------------------------------------------")
                                                                print("\nSelect Language: \n")
                                                                print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                                
                                                                # selecting the language
                                                                language=int(input("Enter option number for Langauge Selection: "))
                                                                
                                                                #telugu version
                                                                if language==1:
                                                                    
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                                        print("------------------------------------------")
                                                                        
                                                                        #options in ATM
                                                                        print("ఎంపికను ఎంచుకోండి: \n")
                                                                        print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        
                                                                        selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                            depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if depin==passcode:
                                                                                depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\ndeposited amount : ",depamo)
                                                                                        print("balance amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                            drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if drapin==passcode:
                                                                                draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")                               
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                                
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                            chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nyour new passcode is activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tతప్పు పాస్‌కోడ్")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                            balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tసంతులనం: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tచెల్లని సంఖ్య")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                                        print("------------------------------------------")

                                                                #hindi version
                                                                elif language==2:
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                                    
                                                                        #options in ATM
                                                                        print("\nविकल्प दर्ज करें: ")
                                                                        print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("\nविकल्प दर्ज करें: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nराशि जमा करें: \n")
                                                                            depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                            if depin==passcode:
                                                                                print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                                depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nराशि वापस लें: n")
                                                                            print("न्यूनतम निकासी एक सौ")
                                                                            wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                            if wipin==passcode:
                                                                                draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nWithdraw Amount : ",draw)
                                                                                        print("Balance Amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nपासकोड बदलें: ")
                                                                            chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tनया पासकोड सक्रिय")        
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tपहले से मौजूद पासकोड")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nबैलेंस पूछताछ: \n")
                                                                            balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tसंतुलन: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance  Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tग़लत पासकोड")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tअमान्य संख्या")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("------------------------------------------")
                                                                        print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                                        print("------------------------------------------")
                                                                #9tabs english version//
                                                                elif language==3:
                                                                    #typing the passcode
                                                                    passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("------------------------------------------")
                                                                        print("\tPasscode Confirmed\t")
                                                                        print("------------------------------------------\n")
                                                                    
                                                                        #options in ATM 
                                                                        print("Enter Options: ")
                                                                        print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("Enter Options: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                            depin=int(input("\nEnter passcode to deposite: "))
                                                                            if depin==passcode:
                                                                                print("\tMinimum deposit one hundred to one lakh \n")
                                                                                depamo=int(input("\nEnter the deposit amount: "))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",depamo,"is can't be deposited")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                            print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                            wipin=int(input("Enter passcode to withdrawal: "))
                                                                            if wipin==passcode: 
                                                                                draw=int(input("\nEnter the withdrawal amount: "))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"can't be withdraw")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nCHANGE THE PASSCODE: ")
                                                                            chapin=int(input("\nenter the old pin: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nenter new pin: "))
                                                                                if chanew==chapin:
                                                                                    print("\nalready existing passcode")
                                                                                else:    
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tNew Passcode Activated")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nBALANCE ENQUIRY: ")
                                                                            balpin=int(input("\nEnter the passcode to check balance: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tBalance: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:    
                                                                                
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                                    
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tInvalid Number")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tWeak Passcode\n\tTry Another")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                                        print("------------------------------------------")
                                                                        print("\n\t\tThank You")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tInvalid Number")
                                                                    print("------------------------------------------")
                                                            else:
                                                                print("------------------------------------------")
                                                                print("\tIncorrect Passcode")
                                                                print("------------------------------------------")
                                                        else:
                                                            print("------------------------------------------")
                                                            print("\tAccount Number Not Exist")
                                                            print("------------------------------------------")
                                                    elif ulogin==2:
                                                        print("\n------------------------------------------")
                                                        print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                                        print("------------------------------------------")
                                                    else:
                                                        print("\n------------------------------------------")
                                                        print("\tNo Option\n\tThank You")
                                                        print("------------------------------------------")         
                                                else:
                                                    print("\n------------------------------------------")
                                                    print("\tMinors Can't Create Bank Accountt\n\t\t\t\tThank You")
                                                    print("------------------------------------------")        
                                        elif update==3:
                                            gender1=input("\nEnter Gender            : ")
                                            if gender==gender1:
                                                print("------------------------------------------") 
                                                print("\tAlready Existing Gender")
                                                print("------------------------------------------") 
                                            else:
                                                if gender1=="MALE" or gender1=="Male" or gender1=="male" or gender1=="M" or gender=="m" or gender1=="FEMALE" or gender1=="Female" or gender1=="female" or gender1=="F" or gender1=="f":
                                                    print("Updated Gender          : ",gender.replace(gender,gender1))
                                                    print("\n------------------------------------------")
                                                    print("\tDetails Saved Successfully")
                                                    print("------------------------------------------")
                                                
                                                    #asking the user do you want to login or not
                                                    ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                                    if ulogin==1:
                                                        #now login into atm system
                                                        print("\n\nLOGIN: ")
                                                        print("------------------------------------------")
                                                        account=int(input("Account Number : "))
                                                        if account==accnum:
                                                            passcode=int(input("Login Passcode : "))
                                                            if passcode==loginpin:
                                                                print("------------------------------------------")
                                                                print("\t\tLogin Successfully")
                                                                print("------------------------------------------")
                                                                print("\n\n")
                                                                print("\t•••••••• ATM ••••••••")
                                                                print("------------------------------------------")
                                                                print("Hello",name,"...")
                                                                print("Welcome to ATM")
                                                                
                                                                # displaying the language on the screen
                                                                print("------------------------------------------")
                                                                print("\tINSERT DEBIT CARD")
                                                                print("------------------------------------------")
                                                                print("\nSelect Language: \n")
                                                                print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                                
                                                                # selecting the language
                                                                language=int(input("Enter option number for Langauge Selection: "))
                                                                
                                                                #telugu version
                                                                if language==1:
                                                                    
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                                        print("------------------------------------------")
                                                                        
                                                                        #options in ATM
                                                                        print("ఎంపికను ఎంచుకోండి: \n")
                                                                        print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        
                                                                        selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                            depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if depin==passcode:
                                                                                depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\ndeposited amount : ",depamo)
                                                                                        print("balance amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                            drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if drapin==passcode:
                                                                                draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")                               
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                            chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nyour new passcode is activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tతప్పు పాస్‌కోడ్")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                            balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tసంతులనం: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tచెల్లని సంఖ్య")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                                        print("------------------------------------------")

                                                                #hindi version
                                                                elif language==2:
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                                    
                                                                        #options in ATM
                                                                        print("\nविकल्प दर्ज करें: ")
                                                                        print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("\nविकल्प दर्ज करें: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nराशि जमा करें: \n")
                                                                            depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                            if depin==passcode:
                                                                                print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                                depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nराशि वापस लें: n")
                                                                            print("न्यूनतम निकासी एक सौ")
                                                                            wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                            if wipin==passcode:
                                                                                draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nWithdraw Amount : ",draw)
                                                                                        print("Balance Amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nपासकोड बदलें: ")
                                                                            chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tनया पासकोड सक्रिय")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tपहले से मौजूद पासकोड")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nबैलेंस पूछताछ: \n")
                                                                            balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tसंतुलन: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance  Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tग़लत पासकोड")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tअमान्य संख्या")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("------------------------------------------")
                                                                        print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                                        print("------------------------------------------")
                                                                #9tabs english version//
                                                                elif language==3:
                                                                    #typing the passcode
                                                                    passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("------------------------------------------")
                                                                        print("\tPasscode Confirmed\t")
                                                                        print("------------------------------------------\n")
                                                                    
                                                                        #options in ATM 
                                                                        print("Enter Options: ")
                                                                        print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("Enter Options: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                            depin=int(input("\nEnter passcode to deposite: "))
                                                                            if depin==passcode:
                                                                                print("\tMinimum deposit one hundred to one lakh \n")
                                                                                depamo=int(input("\nEnter the deposit amount: "))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",depamo,"is can't be deposited")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                            print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                            wipin=int(input("Enter passcode to withdrawal: "))
                                                                            if wipin==passcode: 
                                                                                draw=int(input("\nEnter the withdrawal amount: "))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"can't be withdraw")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nCHANGE THE PASSCODE: ")
                                                                            chapin=int(input("\nenter the old pin: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nenter new pin: "))
                                                                                if chanew==chapin:
                                                                                    print("\nalready existing passcode")
                                                                                else:    
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tNew Passcode Activated")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nBALANCE ENQUIRY: ")
                                                                            balpin=int(input("\nEnter the passcode to check balance: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tBalance: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:    
                                                                                
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tInvalid Number")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tWeak Passcode\n\tTry Another")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                                        print("------------------------------------------")
                                                                        print("\n\t\tThank You")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tInvalid Number")
                                                                    print("------------------------------------------")
                                                            else:
                                                                print("------------------------------------------")
                                                                print("\tIncorrect Passcode")
                                                                print("------------------------------------------")
                                                        else:
                                                            print("------------------------------------------")
                                                            print("\tAccount Number Not Exist")
                                                            print("------------------------------------------") 
                                                    elif ulogin==2:
                                                        print("\n------------------------------------------")
                                                        print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                                        print("------------------------------------------")
                                                    else:
                                                        print("\n------------------------------------------")
                                                        print("\tNo Option\n\tThank You")
                                                        print("------------------------------------------")                    
                                                else:
                                                    print("\n------------------------------------------")
                                                    print("\t\tMental Illness\n\tGender Doesn't Exist")
                                                    print("------------------------------------------")
                                        elif update==4:
                                            mobile1=int(input("\nEnter Mobile Number     : "))
                                            if mobile==mobile1:
                                                print("\n------------------------------------------")
                                                print("\tAlready Existing Mobile Number")
                                                print("------------------------------------------")
                                            else:
                                                if mobile1>=1000000000 and mobile1<=9999999999:
                                                    print("Updated Mobile Number   : +91 ",mobile1) 
                                                    print("\n------------------------------------------")
                                                    print("\tDetails Saved Successfully")
                                                    print("------------------------------------------")
                                                
                                                    #asking the user do you want to login or not
                                                    ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                                    if ulogin==1:
                                                        #now login into atm system
                                                        print("\n\nLOGIN: ")
                                                        print("------------------------------------------")
                                                        account=int(input("Account Number : "))
                                                        if account==accnum:
                                                            passcode=int(input("Login Passcode : "))
                                                            if passcode==loginpin:
                                                                print("------------------------------------------")
                                                                print("\t\tLogin Successfully")
                                                                print("------------------------------------------")
                                                                print("\n\n")
                                                                print("\t•••••••• ATM ••••••••")
                                                                print("------------------------------------------")
                                                                print("Hello",name,"...")
                                                                print("Welcome to ATM")
                                                                
                                                                # displaying the language on the screen
                                                                print("------------------------------------------")
                                                                print("\tINSERT DEBIT CARD")
                                                                print("------------------------------------------")
                                                                print("\nSelect Language: \n")
                                                                print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                                
                                                                # selecting the language
                                                                language=int(input("Enter option number for Langauge Selection: "))
                                                                
                                                                #telugu version
                                                                if language==1:
                                                                    
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                                        print("------------------------------------------")
                                                                        
                                                                        #options in ATM
                                                                        print("ఎంపికను ఎంచుకోండి: \n")
                                                                        print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        
                                                                        selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                            depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if depin==passcode:
                                                                                depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\ndeposited amount : ",depamo)
                                                                                        print("balance amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                            drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if drapin==passcode:
                                                                                draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")                               
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                                
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                            chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nyour new passcode is activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tతప్పు పాస్‌కోడ్")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                            balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tసంతులనం: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tచెల్లని సంఖ్య")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                                        print("------------------------------------------")

                                                                #hindi version
                                                                elif language==2:
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                                    
                                                                        #options in ATM
                                                                        print("\nविकल्प दर्ज करें: ")
                                                                        print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("\nविकल्प दर्ज करें: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nराशि जमा करें: \n")
                                                                            depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                            if depin==passcode:
                                                                                print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                                depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nराशि वापस लें: n")
                                                                            print("न्यूनतम निकासी एक सौ")
                                                                            wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                            if wipin==passcode:
                                                                                draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nWithdraw Amount : ",draw)
                                                                                        print("Balance Amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nपासकोड बदलें: ")
                                                                            chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tनया पासकोड सक्रिय")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tपहले से मौजूद पासकोड")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nबैलेंस पूछताछ: \n")
                                                                            balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tसंतुलन: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance  Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tग़लत पासकोड")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tअमान्य संख्या")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("------------------------------------------")
                                                                        print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                                        print("------------------------------------------")
                                                                #9tabs english version//
                                                                elif language==3:
                                                                    #typing the passcode
                                                                    passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("------------------------------------------")
                                                                        print("\tPasscode Confirmed\t")
                                                                        print("------------------------------------------\n")
                                                                    
                                                                        #options in ATM 
                                                                        print("Enter Options: ")
                                                                        print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("Enter Options: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                            depin=int(input("\nEnter passcode to deposite: "))
                                                                            if depin==passcode:
                                                                                print("\tMinimum deposit one hundred to one lakh \n")
                                                                                depamo=int(input("\nEnter the deposit amount: "))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",depamo,"is can't be deposited")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                            print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                            wipin=int(input("Enter passcode to withdrawal: "))
                                                                            if wipin==passcode: 
                                                                                draw=int(input("\nEnter the withdrawal amount: "))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"can't be withdraw")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nCHANGE THE PASSCODE: ")
                                                                            chapin=int(input("\nenter the old pin: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nenter new pin: "))
                                                                                if chanew==chapin:
                                                                                    print("\nalready existing passcode")
                                                                                else:    
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tNew Passcode Activated")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nBALANCE ENQUIRY: ")
                                                                            balpin=int(input("\nEnter the passcode to check balance: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tBalance: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:    
                                                                                
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                                    
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tInvalid Number")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tWeak Passcode\n\tTry Another")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                                        print("------------------------------------------")
                                                                        print("\n\t\tThank You")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tInvalid Number")
                                                                    print("------------------------------------------")
                                                            else:
                                                                print("------------------------------------------")
                                                                print("\tIncorrect Passcode")
                                                                print("------------------------------------------")
                                                        else:
                                                            print("------------------------------------------")
                                                            print("\tAccount Number Not Exist")
                                                            print("------------------------------------------")  
                                                    elif ulogin==2:
                                                        print("\n------------------------------------------")
                                                        print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                                        print("------------------------------------------")
                                                    else:
                                                        print("\n------------------------------------------")
                                                        print("\tNo Option\n\tThank You")
                                                        print("------------------------------------------")                  
                                                else:
                                                    print("\n------------------------------------------")
                                                    print("\tRecheck Your Mobile Number\n\tEnter 10 Digit Mobile Number")
                                                    print("------------------------------------------")        
                                        elif update==5:
                                            address1=input("Enter Address           : ")
                                            if address==address1:
                                                print("\n------------------------------------------")
                                                print("\tAlready Existing Address")
                                                print("------------------------------------------")
                                            else:
                                                print("Updated Address         : ",address.replace(address,address1))
                                                print("\n------------------------------------------")
                                                print("\tDetails Saved Successfully")
                                                print("------------------------------------------")
                                            
                                                #asking the user do you want to login or not
                                                ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                                if ulogin==1:
                                                    #now login into atm system
                                                    print("\n\nLOGIN: ")
                                                    print("------------------------------------------")
                                                    account=int(input("Account Number : "))
                                                    if account==accnum:
                                                        passcode=int(input("Login Passcode : "))
                                                        if passcode==loginpin:
                                                            print("------------------------------------------")
                                                            print("\t\tLogin Successfully")
                                                            print("------------------------------------------")
                                                            print("\n\n")
                                                            print("\t•••••••• ATM ••••••••")
                                                            print("------------------------------------------")
                                                            print("Hello",name,"...")
                                                            print("Welcome to ATM")
                                                            # displaying the language on the screen
                                                            print("------------------------------------------")
                                                            print("\tINSERT DEBIT CARD")
                                                            print("------------------------------------------")
                                                            print("\nSelect Language: \n")
                                                            print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                            # selecting the language
                                                            language=int(input("Enter option number for Langauge Selection: "))
                                                            
                                                            #telugu version
                                                            if language==1:
                                                                #typing the passcode
                                                                passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                                if passcode>=1000 and passcode<=9999:
                                                                    print("\n------------------------------------------")
                                                                    print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                                    print("------------------------------------------")
                                                                    
                                                                    #options in ATM
                                                                    print("ఎంపికను ఎంచుకోండి: \n")
                                                                    print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                                
                                                                    #after passcode showing the options: 
                                                                    # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                    # selection is about the options in ATM
                                                                    
                                                                    selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                                
                                                                    #deposit
                                                                    if selection==1:
                                                                        print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                        depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                        if depin==passcode:
                                                                            depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                            if depamo>=100 and depamo <=100000:
                                                                                print("\n------------------------------------------")
                                                                                print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\ndeposited amount : ",depamo)
                                                                                    print("balance amount   : ",balance+depamo,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                            print("------------------------------------------")
                                                                
                                                                    #withdrawal
                                                                    elif selection==2:
                                                                        print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                        drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                        if drapin==passcode:
                                                                            draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                            if draw<=balance:
                                                                                print("\n------------------------------------------")
                                                                                print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                                print("------------------------------------------")                               
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nwithdraw amount : ",draw)
                                                                                    print("balance amount  : ",balance-draw,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                            print("------------------------------------------")
                                                                            
                                                                
                                                                    #change pin 
                                                                    elif selection==3:
                                                                        print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                        chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                        if chapin==passcode:
                                                                            chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                            if chanew!=chapin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nyour new passcode is activated")
                                                                                    print("Balance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                            print("------------------------------------------")
                                                                
                                                                    #balance enquiry
                                                                    elif selection==4:
                                                                        print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                        balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                        if passcode==balpin:
                                                                            print("\n------------------------------------------")
                                                                            print("\tసంతులనం: ",balance)
                                                                            print("------------------------------------------")
                                                                            print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                            opt=int(input("Enter Option: "))
                                                                            if opt==1:
                                                                                timer()
                                                                                print("\n\n------------------------------------------")
                                                                                print("\t\tMINI STATEMENT\t\t")
                                                                                print("------------------------------------------")
                                                                                from datetime import datetime
                                                                                today=datetime.today().date()
                                                                                from datetime import datetime
                                                                                week=datetime.today()
                                                                                print("Date & Day     : ",today,week.strftime("%A"))
                                                                                print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                print("------------------------------------------")
                                                                                print("NAME           : ",name)
                                                                                print("ACCOUNT NUMBER : ",accnum)
                                                                                print("------------------------------------------")
                                                                                print("\nBalance amount : ",balance,"\n")
                                                                                print("------------------------------------------")
                                                                                print("\t\tTHANK YOU\t\t")
                                                                                print("------------------------------------------")
                                                                            elif opt==2:
                                                                                print("------------------------------------------")
                                                                                print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tNo Option\n\tThank You")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tతప్పు పాస్‌కోడ్")
                                                                            print("------------------------------------------")
                                                                    else: 
                                                                        print("------------------------------------------")
                                                                        print("\tచెల్లని సంఖ్య")
                                                                        print("------------------------------------------")
                                                                elif passcode==0000:
                                                                    print("\n------------------------------------------")
                                                                    print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                                    print("------------------------------------------")
                                                                else:
                                                                    print("\n------------------------------------------")
                                                                    print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                                    print("------------------------------------------")

                                                            #hindi version
                                                            elif language==2:
                                                                #typing the passcode
                                                                passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                                if passcode>=1000 and passcode<=9999:
                                                                    print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                                
                                                                    #options in ATM
                                                                    print("\nविकल्प दर्ज करें: ")
                                                                    print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                                
                                                                    #after passcode showing the options: 
                                                                    # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                    # selection is about the options in ATM
                                                                    selection=int(input("\nविकल्प दर्ज करें: "))
                                                                
                                                                    #deposit
                                                                    if selection==1:
                                                                        print("\nराशि जमा करें: \n")
                                                                        depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                        if depin==passcode:
                                                                            print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                            depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                            if depamo>=100 and depamo <=100000:
                                                                                print("\n------------------------------------------")
                                                                                print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nDeposited Amount : ",depamo)
                                                                                    print("Balance Amount   : ",balance+depamo,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                            print("------------------------------------------")
                                                                
                                                                    #withdrawal
                                                                    elif selection==2:
                                                                        print("\nराशि वापस लें: n")
                                                                        print("न्यूनतम निकासी एक सौ")
                                                                        wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                        if wipin==passcode:
                                                                            draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                            if draw<=balance:
                                                                                print("\n------------------------------------------")
                                                                                print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nWithdraw Amount : ",draw)
                                                                                    print("Balance Amount  : ",balance-draw,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tगलत पासकोड\n\tधन्यवाद")
                                                                            print("------------------------------------------")
                                                                
                                                                    #change pin 
                                                                    elif selection==3:
                                                                        print("\nपासकोड बदलें: ")
                                                                        chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                        if chapin==passcode:
                                                                            chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                            if chanew!=chapin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tनया पासकोड सक्रिय")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nYour New Passcode Is Activated")
                                                                                    print("Balance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tपहले से मौजूद पासकोड")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                            print("------------------------------------------")
                                                                
                                                                    #balance enquiry
                                                                    elif selection==4:
                                                                        print("\nबैलेंस पूछताछ: \n")
                                                                        balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                        if passcode==balpin:
                                                                            print("\n------------------------------------------")
                                                                            print("\tसंतुलन: ",balance)
                                                                            print("------------------------------------------")
                                                                            print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                            opt=int(input("Enter Option: "))
                                                                            if opt==1:
                                                                                timer()
                                                                                print("\n\n------------------------------------------")
                                                                                print("\t\tMINI STATEMENT\t\t")
                                                                                print("------------------------------------------")
                                                                                from datetime import datetime
                                                                                today=datetime.today().date()
                                                                                from datetime import datetime
                                                                                week=datetime.today()
                                                                                print("Date & Day     : ",today,week.strftime("%A"))
                                                                                print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                print("------------------------------------------")
                                                                                print("NAME           : ",name)
                                                                                print("ACCOUNT NUMBER : ",accnum)
                                                                                print("------------------------------------------")
                                                                                print("\nBalance  Amount : ",balance,"\n")
                                                                                print("------------------------------------------")
                                                                                print("\t\tTHANK YOU\t\t")
                                                                                print("------------------------------------------")
                                                                            elif opt==2:
                                                                                print("------------------------------------------")
                                                                                print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tNo Option\n\tThank You")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tग़लत पासकोड")
                                                                            print("------------------------------------------")
                                                                    else: 
                                                                        print("------------------------------------------")
                                                                        print("\tअमान्य संख्या")
                                                                        print("------------------------------------------")
                                                                elif passcode==0000:
                                                                    print("------------------------------------------")
                                                                    print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                                    print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                                    print("------------------------------------------")
                                                            #9tabs english version//
                                                            elif language==3:
                                                                #typing the passcode
                                                                passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                                if passcode>=1000 and passcode<=9999:
                                                                    print("------------------------------------------")
                                                                    print("\tPasscode Confirmed\t")
                                                                    print("------------------------------------------\n")
                                                                
                                                                    #options in ATM 
                                                                    print("Enter Options: ")
                                                                    print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                                
                                                                    #after passcode showing the options: 
                                                                    # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                    # selection is about the options in ATM
                                                                    selection=int(input("Enter Options: "))
                                                                
                                                                    #deposit
                                                                    if selection==1:
                                                                        print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                        depin=int(input("\nEnter passcode to deposite: "))
                                                                        if depin==passcode:
                                                                            print("\tMinimum deposit one hundred to one lakh \n")
                                                                            depamo=int(input("\nEnter the deposit amount: "))
                                                                            if depamo>=100 and depamo <=100000:
                                                                                print("\n------------------------------------------")
                                                                                print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nDeposited Amount : ",depamo)
                                                                                    print("Balance Amount   : ",balance+depamo,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\t",depamo,"is can't be deposited")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tIncorrect Passcode\n\tThank You")
                                                                            print("------------------------------------------")
                                                                
                                                                    #withdrawal
                                                                    elif selection==2:
                                                                        print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                        print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                        wipin=int(input("Enter passcode to withdrawal: "))
                                                                        if wipin==passcode: 
                                                                            draw=int(input("\nEnter the withdrawal amount: "))
                                                                            if draw<=balance:
                                                                                print("\n------------------------------------------")
                                                                                print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nwithdraw amount : ",draw)
                                                                                    print("balance amount  : ",balance-draw,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\t",draw,"can't be withdraw")
                                                                                print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tIncorrect Passcode\n\tThank You")
                                                                            print("------------------------------------------")
                                                                
                                                                    #change pin 
                                                                    elif selection==3:
                                                                        print("\nCHANGE THE PASSCODE: ")
                                                                        chapin=int(input("\nenter the old pin: "))
                                                                        if chapin==passcode:
                                                                            chanew=int(input("\nenter new pin: "))
                                                                            if chanew==chapin:
                                                                                print("\nalready existing passcode")
                                                                            else:    
                                                                                print("\n------------------------------------------")
                                                                                print("\tNew Passcode Activated")
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nYour New Passcode Is Activated")
                                                                                    print("Balance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tIncorrect Passcode\n\tThank You")
                                                                            print("------------------------------------------")
                                                                
                                                                    #balance enquiry
                                                                    elif selection==4:
                                                                        print("\nBALANCE ENQUIRY: ")
                                                                        balpin=int(input("\nEnter the passcode to check balance: "))
                                                                        if passcode==balpin:
                                                                            print("\n------------------------------------------")
                                                                            print("\tBalance: ",balance)
                                                                            print("------------------------------------------")
                                                                            print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                            opt=int(input("Enter Option: "))
                                                                            if opt==1:
                                                                                timer()
                                                                                print("\n\n------------------------------------------")
                                                                                print("\t\tMINI STATEMENT\t\t")
                                                                                print("------------------------------------------")
                                                                                from datetime import datetime
                                                                                today=datetime.today().date()
                                                                                from datetime import datetime
                                                                                week=datetime.today()
                                                                                print("Date & Day     : ",today,week.strftime("%A"))
                                                                                print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                print("------------------------------------------")
                                                                                print("NAME           : ",name)
                                                                                print("ACCOUNT NUMBER : ",accnum)
                                                                                print("------------------------------------------")
                                                                                print("\nBalance Amount : ",balance,"\n")
                                                                                print("------------------------------------------")
                                                                                print("\t\tTHANK YOU\t\t")
                                                                                print("------------------------------------------")
                                                                            elif opt==2:
                                                                                print("------------------------------------------")
                                                                                print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                print("------------------------------------------")
                                                                            else:    
                                                                            
                                                                                print("------------------------------------------")
                                                                                print("\tNo Option\n\tThank You")
                                                                                print("------------------------------------------")
                                                                                
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tIncorrect Passcode")
                                                                            print("------------------------------------------")
                                                                    else: 
                                                                        print("------------------------------------------")
                                                                        print("\tInvalid Number")
                                                                        print("------------------------------------------")
                                                                elif passcode==0000:
                                                                    print("\n------------------------------------------")
                                                                    print("\tWeak Passcode\n\tTry Another")
                                                                    print("------------------------------------------")
                                                                else:
                                                                    print("\n------------------------------------------")
                                                                    print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                                    print("------------------------------------------")
                                                                    print("\n\t\tThank You")
                                                            else:
                                                                print("------------------------------------------")
                                                                print("\tInvalid Number")
                                                                print("------------------------------------------")
                                                        else:
                                                            print("------------------------------------------")
                                                            print("\tIncorrect Passcode")
                                                            print("------------------------------------------")
                                                    else:
                                                        print("------------------------------------------")
                                                        print("\tAccount Number Not Exist")
                                                        print("------------------------------------------") 
                                                elif ulogin==2:
                                                    print("\n------------------------------------------")
                                                    print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                                    print("------------------------------------------")
                                                else:
                                                    print("\n------------------------------------------")
                                                    print("\tNo Option\n\tThank You")
                                                    print("------------------------------------------")                        
                                        elif update==6:
                                            accnum1=int(input("Enter Account Number  : "))
                                            if accnum==accnum1:
                                                print("\n------------------------------------------")
                                                print("\tAlready Existing Account Number")
                                                print("------------------------------------------")
                                            else:
                                                if accnum1>=1000000000 and accnum1<=9999999999:
                                                    print("Updated ccount Number : ",accnum1)
                                                    print("\n------------------------------------------")
                                                    print("\tDetails Saved Successfully")
                                                    print("------------------------------------------")
                                                
                                                    #asking the user do you want to login or not
                                                    ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                                    if ulogin==1:
                                                        #now login into atm system
                                                        print("\n\nLOGIN: ")
                                                        print("------------------------------------------")
                                                        account=int(input("Account Number : "))
                                                        if account==accnum1:
                                                            passcode=int(input("Login Passcode : "))
                                                            if passcode==loginpin:
                                                                print("------------------------------------------")
                                                                print("\t\tLogin Successfully")
                                                                print("------------------------------------------")
                                                                print("\n\n")
                                                                print("\t•••••••• ATM ••••••••")
                                                                print("------------------------------------------")
                                                                print("Hello",name,"...")
                                                                print("Welcome to ATM")
                                                                
                                                                # displaying the language on the screen
                                                                print("------------------------------------------")
                                                                print("\tINSERT DEBIT CARD")
                                                                print("------------------------------------------")
                                                                print("\nSelect Language: \n")
                                                                print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                                
                                                                # selecting the language
                                                                language=int(input("Enter option number for Langauge Selection: "))
                                                                
                                                                #telugu version
                                                                if language==1:
                                                                    
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                                        print("------------------------------------------")
                                                                        
                                                                        #options in ATM
                                                                        print("ఎంపికను ఎంచుకోండి: \n")
                                                                        print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        
                                                                        selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                            depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if depin==passcode:
                                                                                depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\ndeposited amount : ",depamo)
                                                                                        print("balance amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                            drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if drapin==passcode:
                                                                                draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")                               
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                                
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                            chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\nyour new passcode is activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tతప్పు పాస్‌కోడ్")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                            balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tసంతులనం: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum1)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tచెల్లని సంఖ్య")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                                        print("------------------------------------------")
                                                                #hindi version
                                                                elif language==2:
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                                    
                                                                        #options in ATM
                                                                        print("\nविकल्प दर्ज करें: ")
                                                                        print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("\nविकल्प दर्ज करें: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nराशि जमा करें: \n")
                                                                            depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                            if depin==passcode:
                                                                                print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                                depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nराशि वापस लें: n")
                                                                            print("न्यूनतम निकासी एक सौ")
                                                                            wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                            if wipin==passcode:
                                                                                draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\nWithdraw Amount : ",draw)
                                                                                        print("Balance Amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nपासकोड बदलें: ")
                                                                            chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tनया पासकोड सक्रिय")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tपहले से मौजूद पासकोड")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nबैलेंस पूछताछ: \n")
                                                                            balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tसंतुलन: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum1)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance  Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tग़लत पासकोड")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tअमान्य संख्या")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("------------------------------------------")
                                                                        print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                                        print("------------------------------------------")
                                                                #9tabs english version//
                                                                elif language==3:
                                                                    #typing the passcode
                                                                    passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("------------------------------------------")
                                                                        print("\tPasscode Confirmed\t")
                                                                        print("------------------------------------------\n")
                                                                    
                                                                        #options in ATM 
                                                                        print("Enter Options: ")
                                                                        print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("Enter Options: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                            depin=int(input("\nEnter passcode to deposite: "))
                                                                            if depin==passcode:
                                                                                print("\tMinimum deposit one hundred to one lakh \n")
                                                                                depamo=int(input("\nEnter the deposit amount: "))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",depamo,"is can't be deposited")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                            print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                            wipin=int(input("Enter passcode to withdrawal: "))
                                                                            if wipin==passcode: 
                                                                                draw=int(input("\nEnter the withdrawal amount: "))
                                                                                if draw<=balance:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"can't be withdraw")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nCHANGE THE PASSCODE: ")
                                                                            chapin=int(input("\nenter the old pin: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nenter new pin: "))
                                                                                if chanew==chapin:
                                                                                    print("\nalready existing passcode")
                                                                                else:    
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tNew Passcode Activated")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum1)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nBALANCE ENQUIRY: ")
                                                                            balpin=int(input("\nEnter the passcode to check balance: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tBalance: ",balance)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum1)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance Amount : ",balance,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:    
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tInvalid Number")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tWeak Passcode\n\tTry Another")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                                        print("------------------------------------------")
                                                                        print("\n\t\tThank You")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tInvalid Number")
                                                                    print("------------------------------------------")
                                                            else:
                                                                print("------------------------------------------")
                                                                print("\tIncorrect Passcode")
                                                                print("------------------------------------------")
                                                        else:
                                                            print("------------------------------------------")
                                                            print("\tAccount Number Not Exist")
                                                            print("------------------------------------------")
                                                    elif ulogin==2:
                                                        print("\n------------------------------------------")
                                                        print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                                        print("------------------------------------------")
                                                    else:
                                                        print("\n------------------------------------------")
                                                        print("\tNo Option\n\tThank You")
                                                        print("------------------------------------------")                 
                                                else:
                                                    print("\n------------------------------------------")
                                                    print("\tRecheck The Account Number\n\tEnter 10 digit account number")
                                                    print("------------------------------------------")    
                                        elif update==7:
                                            balance1=int(input("Enter Initial Amount   : "))
                                            if balance==balance1:
                                                print("\n------------------------------------------")
                                                print("\tAlready Existing Balance")
                                                print("------------------------------------------")
                                            else:
                                                if balance1>=2000 and balance1<=100000:
                                                    print("Updated Initial Amount : ")
                                                    print("\n------------------------------------------")
                                                    print("\tDetails Saved Successfully")
                                                    print("------------------------------------------")
                                                
                                                    #asking the user do you want to login or not
                                                    ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                                    if ulogin==1:
                                                        #now login into atm system
                                                        print("\n\nLOGIN: ")
                                                        print("------------------------------------------")
                                                        account=int(input("Account Number : "))
                                                        if account==accnum:
                                                            passcode=int(input("Login Passcode : "))
                                                            if passcode==loginpin:
                                                                print("------------------------------------------")
                                                                print("\t\tLogin Successfully")
                                                                print("------------------------------------------")
                                                                print("\n\n")
                                                                print("\t•••••••• ATM ••••••••")
                                                                print("------------------------------------------")
                                                                print("Hello",name,"...")
                                                                print("Welcome to ATM")
                                                                
                                                                # displaying the language on the screen
                                                                print("------------------------------------------")
                                                                print("\tINSERT DEBIT CARD")
                                                                print("------------------------------------------")
                                                                print("\nSelect Language: \n")
                                                                print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                                
                                                                # selecting the language
                                                                language=int(input("Enter option number for Langauge Selection: "))
                                                                
                                                                #telugu version
                                                                if language==1:
                                                                    
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                                        print("------------------------------------------")
                                                                        
                                                                        #options in ATM
                                                                        print("ఎంపికను ఎంచుకోండి: \n")
                                                                        print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        
                                                                        selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                            depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if depin==passcode:
                                                                                depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\ndeposited amount : ",depamo)
                                                                                        print("balance amount   : ",balance1+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                            drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if drapin==passcode:
                                                                                draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                if draw<=balance1:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")                               
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance1-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                                
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                            chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nyour new passcode is activated")
                                                                                        print("Balance Amount : ",balance1,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tతప్పు పాస్‌కోడ్")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                            balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tసంతులనం: ",balance1)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance amount : ",balance1,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tతప్పు పాస్‌కోడ్")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tచెల్లని సంఖ్య")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                                        print("------------------------------------------")

                                                                #hindi version
                                                                elif language==2:
                                                                    #typing the passcode
                                                                    passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                                    
                                                                        #options in ATM
                                                                        print("\nविकल्प दर्ज करें: ")
                                                                        print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("\nविकल्प दर्ज करें: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nराशि जमा करें: \n")
                                                                            depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                            if depin==passcode:
                                                                                print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                                depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance1+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                                print("------------------------------------------")
                                                                    
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nराशि वापस लें: n")
                                                                            print("न्यूनतम निकासी एक सौ")
                                                                            wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                            if wipin==passcode:
                                                                                draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                                if draw<=balance1:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nWithdraw Amount : ",draw)
                                                                                        print("Balance Amount  : ",balance1-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nपासकोड बदलें: ")
                                                                            chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                                if chanew!=chapin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tनया पासकोड सक्रिय")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance1,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tपहले से मौजूद पासकोड")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nबैलेंस पूछताछ: \n")
                                                                            balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tसंतुलन: ",balance1)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance  Amount : ",balance1,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tग़लत पासकोड")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tअमान्य संख्या")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("------------------------------------------")
                                                                        print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                                        print("------------------------------------------")
                                                                #9tabs english version//
                                                                elif language==3:
                                                                    #typing the passcode
                                                                    passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                                    if passcode>=1000 and passcode<=9999:
                                                                        print("------------------------------------------")
                                                                        print("\tPasscode Confirmed\t")
                                                                        print("------------------------------------------\n")
                                                                    
                                                                        #options in ATM 
                                                                        print("Enter Options: ")
                                                                        print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                                    
                                                                        #after passcode showing the options: 
                                                                        # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                        # selection is about the options in ATM
                                                                        selection=int(input("Enter Options: "))
                                                                    
                                                                        #deposit
                                                                        if selection==1:
                                                                            print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                            depin=int(input("\nEnter passcode to deposite: "))
                                                                            if depin==passcode:
                                                                                print("\tMinimum deposit one hundred to one lakh \n")
                                                                                depamo=int(input("\nEnter the deposit amount: "))
                                                                                if depamo>=100 and depamo <=100000:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nDeposited Amount : ",depamo)
                                                                                        print("Balance Amount   : ",balance1+depamo,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",depamo,"is can't be deposited")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                        #withdrawal
                                                                        elif selection==2:
                                                                            print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                            print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                            wipin=int(input("Enter passcode to withdrawal: "))
                                                                            if wipin==passcode: 
                                                                                draw=int(input("\nEnter the withdrawal amount: "))
                                                                                if draw<=balance1:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nwithdraw amount : ",draw)
                                                                                        print("balance amount  : ",balance1-draw,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\t",draw,"can't be withdraw")
                                                                                    print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #change pin 
                                                                        elif selection==3:
                                                                            print("\nCHANGE THE PASSCODE: ")
                                                                            chapin=int(input("\nenter the old pin: "))
                                                                            if chapin==passcode:
                                                                                chanew=int(input("\nenter new pin: "))
                                                                                if chanew==chapin:
                                                                                    print("\nalready existing passcode")
                                                                                else:    
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tNew Passcode Activated")
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nYour New Passcode Is Activated")
                                                                                        print("Balance Amount : ",balance1,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode\n\tThank You")
                                                                                print("------------------------------------------")
                                                                    
                                                                        #balance enquiry
                                                                        elif selection==4:
                                                                            print("\nBALANCE ENQUIRY: ")
                                                                            balpin=int(input("\nEnter the passcode to check balance: "))
                                                                            if passcode==balpin:
                                                                                print("\n------------------------------------------")
                                                                                print("\tBalance: ",balance1)
                                                                                print("------------------------------------------")
                                                                                print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                opt=int(input("Enter Option: "))
                                                                                if opt==1:
                                                                                    timer()
                                                                                    print("\n\n------------------------------------------")
                                                                                    print("\t\tMINI STATEMENT\t\t")
                                                                                    print("------------------------------------------")
                                                                                    from datetime import datetime
                                                                                    today=datetime.today().date()
                                                                                    from datetime import datetime
                                                                                    week=datetime.today()
                                                                                    print("Date & Day     : ",today,week.strftime("%A"))
                                                                                    print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                    print("------------------------------------------")
                                                                                    print("NAME           : ",name)
                                                                                    print("ACCOUNT NUMBER : ",accnum)
                                                                                    print("------------------------------------------")
                                                                                    print("\nBalance Amount : ",balance1,"\n")
                                                                                    print("------------------------------------------")
                                                                                    print("\t\tTHANK YOU\t\t")
                                                                                    print("------------------------------------------")
                                                                                elif opt==2:
                                                                                    print("------------------------------------------")
                                                                                    print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                    print("------------------------------------------")
                                                                                else:    
                                                                                
                                                                                    print("------------------------------------------")
                                                                                    print("\tNo Option\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                                    
                                                                            else:
                                                                                print("------------------------------------------")
                                                                                print("\tIncorrect Passcode")
                                                                                print("------------------------------------------")
                                                                        else: 
                                                                            print("------------------------------------------")
                                                                            print("\tInvalid Number")
                                                                            print("------------------------------------------")
                                                                    elif passcode==0000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tWeak Passcode\n\tTry Another")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("\n------------------------------------------")
                                                                        print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                                        print("------------------------------------------")
                                                                        print("\n\t\tThank You")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tInvalid Number")
                                                                    print("------------------------------------------")
                                                            else:
                                                                print("------------------------------------------")
                                                                print("\tIncorrect Passcode")
                                                                print("------------------------------------------")
                                                        else:
                                                            print("------------------------------------------")
                                                            print("\tAccount Number Not Exist")
                                                            print("------------------------------------------") 
                                                    elif ulogin==2:
                                                        print("\n------------------------------------------")
                                                        print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                                        print("------------------------------------------")
                                                    else:
                                                        print("\n------------------------------------------")
                                                        print("\tNo Option\n\tThank You")
                                                        print("------------------------------------------")                         
                                                else:
                                                    print("\n------------------------------------------")
                                                    print("\tDeposit more than\n\t Rs. 2000 and below Rs. 100000")
                                                    print("------------------------------------------")    
                                        elif update==8:
                                            loginpin1=int(input("Enter 6 Digit Login Pin : ")) 
                                            if loginpin==loginpin1:
                                                print("\n------------------------------------------")
                                                print("\tAlready Existing Login Passcode")
                                                print("------------------------------------------")
                                            else:    
                                                if loginpin1>=100000 and loginpin1<=999999:
                                                    conpin1=int(input("Enter Confirm Login Pin : "))
                                                    if loginpin1==conpin1:
                                                        print("Updated Login Pin       : ",loginpin1)
                                                        print("\n------------------------------------------")
                                                        print("\tDetails Saved Successfully")
                                                        print("------------------------------------------")
                                                    
                                                        #asking the user do you want to login or not
                                                        ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                                        if ulogin==1:
                                                            #now login into atm system
                                                            print("\n\nLOGIN: ")
                                                            print("------------------------------------------")
                                                            account=int(input("Account Number : "))
                                                            if account==accnum:
                                                                passcode=int(input("Login Passcode : "))
                                                                if passcode==loginpin1:
                                                                    print("------------------------------------------")
                                                                    print("\t\tLogin Successfully")
                                                                    print("------------------------------------------")
                                                                    print("\n\n")
                                                                    print("\t•••••••• ATM ••••••••")
                                                                    print("------------------------------------------")
                                                                    print("Hello",name,"...")
                                                                    print("Welcome to ATM")
                                                                    
                                                                    # displaying the language on the screen
                                                                    print("------------------------------------------")
                                                                    print("\tINSERT DEBIT CARD")
                                                                    print("------------------------------------------")
                                                                    print("\nSelect Language: \n")
                                                                    print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                                    
                                                                    # selecting the language
                                                                    language=int(input("Enter option number for Langauge Selection: "))
                                                                    
                                                                    #telugu version
                                                                    if language==1:
                                                                        
                                                                        #typing the passcode
                                                                        passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                                        if passcode>=1000 and passcode<=9999:
                                                                            print("\n------------------------------------------")
                                                                            print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                                            print("------------------------------------------")
                                                                            
                                                                            #options in ATM
                                                                            print("ఎంపికను ఎంచుకోండి: \n")
                                                                            print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                                        
                                                                            #after passcode showing the options: 
                                                                            # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                            # selection is about the options in ATM
                                                                            
                                                                            selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                                        
                                                                            #deposit
                                                                            if selection==1:
                                                                                print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                                depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                                if depin==passcode:
                                                                                    depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                    if depamo>=100 and depamo <=100000:
                                                                                        print("\n------------------------------------------")
                                                                                        print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                                        print("------------------------------------------")
                                                                                        print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\ndeposited amount : ",depamo)
                                                                                            print("balance amount   : ",balance+depamo,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                                        print("------------------------------------------")
                                                                                else: 
                                                                                    print("------------------------------------------")
                                                                                    print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")
                                                                        
                                                                            #withdrawal
                                                                            elif selection==2:
                                                                                print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                                drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                                if drapin==passcode:
                                                                                    draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                                    if draw<=balance:
                                                                                        print("\n------------------------------------------")
                                                                                        print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                                        print("------------------------------------------")                               
                                                                                        print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\nwithdraw amount : ",draw)
                                                                                            print("balance amount  : ",balance-draw,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")
                                                                                    
                                                                        
                                                                            #change pin 
                                                                            elif selection==3:
                                                                                print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                                chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                                if chapin==passcode:
                                                                                    chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                                    if chanew!=chapin:
                                                                                        print("\n------------------------------------------")
                                                                                        print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                                        print("------------------------------------------")
                                                                                        print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\nyour new passcode is activated")
                                                                                            print("Balance Amount : ",balance,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tతప్పు పాస్‌కోడ్")
                                                                                        print("------------------------------------------")
                                                                                else: 
                                                                                    print("------------------------------------------")
                                                                                    print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                                    print("------------------------------------------")
                                                                        
                                                                            #balance enquiry
                                                                            elif selection==4:
                                                                                print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                                balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                                if passcode==balpin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tసంతులనం: ",balance)
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nBalance amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tతప్పు పాస్‌కోడ్")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\tచెల్లని సంఖ్య")
                                                                                print("------------------------------------------")
                                                                        elif passcode==0000:
                                                                            print("\n------------------------------------------")
                                                                            print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("\n------------------------------------------")
                                                                            print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                                            print("------------------------------------------")
                                                                    #hindi version
                                                                    elif language==2:
                                                                        #typing the passcode
                                                                        passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                                        if passcode>=1000 and passcode<=9999:
                                                                            print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                                        
                                                                            #options in ATM
                                                                            print("\nविकल्प दर्ज करें: ")
                                                                            print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                                        
                                                                            #after passcode showing the options: 
                                                                            # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                            # selection is about the options in ATM
                                                                            selection=int(input("\nविकल्प दर्ज करें: "))
                                                                        
                                                                            #deposit
                                                                            if selection==1:
                                                                                print("\nराशि जमा करें: \n")
                                                                                depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                                if depin==passcode:
                                                                                    print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                                    depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                                    if depamo>=100 and depamo <=100000:
                                                                                        print("\n------------------------------------------")
                                                                                        print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                                        print("------------------------------------------")
                                                                                        print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\nDeposited Amount : ",depamo)
                                                                                            print("Balance Amount   : ",balance+depamo,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                                    print("------------------------------------------")
                                                                        
                                                                            #withdrawal
                                                                            elif selection==2:
                                                                                print("\nराशि वापस लें: n")
                                                                                print("न्यूनतम निकासी एक सौ")
                                                                                wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                                if wipin==passcode:
                                                                                    draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                                    if draw<=balance:
                                                                                        print("\n------------------------------------------")
                                                                                        print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                                        print("------------------------------------------")
                                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\nWithdraw Amount : ",draw)
                                                                                            print("Balance Amount  : ",balance-draw,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tगलत पासकोड\n\tधन्यवाद")
                                                                                    print("------------------------------------------")
                                                                        
                                                                            #change pin 
                                                                            elif selection==3:
                                                                                print("\nपासकोड बदलें: ")
                                                                                chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                                if chapin==passcode:
                                                                                    chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                                    if chanew!=chapin:
                                                                                        print("\n------------------------------------------")
                                                                                        print("\tनया पासकोड सक्रिय")
                                                                                        print("------------------------------------------")
                                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\nYour New Passcode Is Activated")
                                                                                            print("Balance Amount : ",balance,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tपहले से मौजूद पासकोड")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                                    print("------------------------------------------")
                                                                        
                                                                            #balance enquiry
                                                                            elif selection==4:
                                                                                print("\nबैलेंस पूछताछ: \n")
                                                                                balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                                if passcode==balpin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tसंतुलन: ",balance)
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nBalance  Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tग़लत पासकोड")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\tअमान्य संख्या")
                                                                                print("------------------------------------------")
                                                                        elif passcode==0000:
                                                                            print("------------------------------------------")
                                                                            print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                                            print("------------------------------------------")
                                                                    #9tabs english version//
                                                                    elif language==3:
                                                                        #typing the passcode
                                                                        passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                                        if passcode>=1000 and passcode<=9999:
                                                                            print("------------------------------------------")
                                                                            print("\tPasscode Confirmed\t")
                                                                            print("------------------------------------------\n")
                                                                        
                                                                            #options in ATM 
                                                                            print("Enter Options: ")
                                                                            print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                                        
                                                                            #after passcode showing the options: 
                                                                            # [ deposit, withdrawal, pin change, balance enquiry ]
                                                                            # selection is about the options in ATM
                                                                            selection=int(input("Enter Options: "))
                                                                        
                                                                            #deposit
                                                                            if selection==1:
                                                                                print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                                depin=int(input("\nEnter passcode to deposite: "))
                                                                                if depin==passcode:
                                                                                    print("\tMinimum deposit one hundred to one lakh \n")
                                                                                    depamo=int(input("\nEnter the deposit amount: "))
                                                                                    if depamo>=100 and depamo <=100000:
                                                                                        print("\n------------------------------------------")
                                                                                        print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                                        print("------------------------------------------")
                                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\nDeposited Amount : ",depamo)
                                                                                            print("Balance Amount   : ",balance+depamo,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\t",depamo,"is can't be deposited")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tIncorrect Passcode\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                        
                                                                            #withdrawal
                                                                            elif selection==2:
                                                                                print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                                print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                                wipin=int(input("Enter passcode to withdrawal: "))
                                                                                if wipin==passcode: 
                                                                                    draw=int(input("\nEnter the withdrawal amount: "))
                                                                                    if draw<=balance:
                                                                                        print("\n------------------------------------------")
                                                                                        print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                                        print("------------------------------------------")
                                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\nwithdraw amount : ",draw)
                                                                                            print("balance amount  : ",balance-draw,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                    else:
                                                                                        print("------------------------------------------")
                                                                                        print("\t",draw,"can't be withdraw")
                                                                                        print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tIncorrect Passcode\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                        
                                                                            #change pin 
                                                                            elif selection==3:
                                                                                print("\nCHANGE THE PASSCODE: ")
                                                                                chapin=int(input("\nenter the old pin: "))
                                                                                if chapin==passcode:
                                                                                    chanew=int(input("\nenter new pin: "))
                                                                                    if chanew==chapin:
                                                                                        print("\nalready existing passcode")
                                                                                    else:    
                                                                                        print("\n------------------------------------------")
                                                                                        print("\tNew Passcode Activated")
                                                                                        print("------------------------------------------")
                                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                                        opt=int(input("Enter Option: "))
                                                                                        if opt==1:
                                                                                            timer()
                                                                                            print("\n\n------------------------------------------")
                                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                                            print("------------------------------------------")
                                                                                            from datetime import datetime
                                                                                            today=datetime.today().date()
                                                                                            from datetime import datetime
                                                                                            week=datetime.today()
                                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                            print("------------------------------------------")
                                                                                            print("NAME           : ",name)
                                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                                            print("------------------------------------------")
                                                                                            print("\nYour New Passcode Is Activated")
                                                                                            print("Balance Amount : ",balance,"\n")
                                                                                            print("------------------------------------------")
                                                                                            print("\t\tTHANK YOU\t\t")
                                                                                            print("------------------------------------------")
                                                                                        elif opt==2:
                                                                                            print("------------------------------------------")
                                                                                            print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                            print("------------------------------------------")
                                                                                        else:
                                                                                            print("------------------------------------------")
                                                                                            print("\tNo Option\n\tThank You")
                                                                                            print("------------------------------------------")
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tIncorrect Passcode\n\tThank You")
                                                                                    print("------------------------------------------")
                                                                        
                                                                            #balance enquiry
                                                                            elif selection==4:
                                                                                print("\nBALANCE ENQUIRY: ")
                                                                                balpin=int(input("\nEnter the passcode to check balance: "))
                                                                                if passcode==balpin:
                                                                                    print("\n------------------------------------------")
                                                                                    print("\tBalance: ",balance)
                                                                                    print("------------------------------------------")
                                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                                    opt=int(input("Enter Option: "))
                                                                                    if opt==1:
                                                                                        timer()
                                                                                        print("\n\n------------------------------------------")
                                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                                        print("------------------------------------------")
                                                                                        from datetime import datetime
                                                                                        today=datetime.today().date()
                                                                                        from datetime import datetime
                                                                                        week=datetime.today()
                                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                                        print("------------------------------------------")
                                                                                        print("NAME           : ",name)
                                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                                        print("------------------------------------------")
                                                                                        print("\nBalance Amount : ",balance,"\n")
                                                                                        print("------------------------------------------")
                                                                                        print("\t\tTHANK YOU\t\t")
                                                                                        print("------------------------------------------")
                                                                                    elif opt==2:
                                                                                        print("------------------------------------------")
                                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                                        print("------------------------------------------")
                                                                                    else:    
                                                                                    
                                                                                        print("------------------------------------------")
                                                                                        print("\tNo Option\n\tThank You")
                                                                                        print("------------------------------------------")
                                                                                        
                                                                                else:
                                                                                    print("------------------------------------------")
                                                                                    print("\tIncorrect Passcode")
                                                                                    print("------------------------------------------")
                                                                            else: 
                                                                                print("------------------------------------------")
                                                                                print("\tInvalid Number")
                                                                                print("------------------------------------------")
                                                                        elif passcode==0000:
                                                                            print("\n------------------------------------------")
                                                                            print("\tWeak Passcode\n\tTry Another")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("\n------------------------------------------")
                                                                            print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                                            print("------------------------------------------")
                                                                            print("\n\t\tThank You")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tInvalid Number")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tIncorrect Passcode")
                                                                    print("------------------------------------------")
                                                            else:
                                                                print("------------------------------------------")
                                                                print("\tAccount Number Not Exist")
                                                                print("------------------------------------------")
                                                        elif ulogin==2:
                                                            print("\n------------------------------------------")
                                                            print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                                            print("------------------------------------------")
                                                        else:
                                                            print("\n------------------------------------------")
                                                            print("\tNo Option\n\tThank You")
                                                            print("------------------------------------------")   
                                                    else:
                                                        print("\n------------------------------------------")
                                                        print("Login Pin Is Not Matched With Confirm Login Pin") 
                                                        print("------------------------------------------")                                     
                                                elif loginpin1==000000:
                                                    print("\n------------------------------------------")
                                                    print("\tWeek Passcode")
                                                    print("------------------------------------------")
                                                else:
                                                    print("\n------------------------------------------")
                                                    print("\t\tWeek Passcode\nMake Sure Your Passcode Must Contain Only 6digits ")
                                                    print("------------------------------------------")       
                                        else:
                                            print("------------------------------------------")
                                            print("\tOption Doesn't Exist")
                                            print("------------------------------------------")
                                    elif b==2:        
                                        print("------------------------------------------")
                                        print("\tDetails Saved Successfully")
                                        print("------------------------------------------")
                                        
                                        #asking the user do you want to login or not
                                        ulogin=int(input("\nDo You Want To Login In Your New Account ?\n1. Yes\n2. No\n\nEnter Option: "))
                                        if ulogin==1:
                                            #now login into atm system
                                            print("\n\nLOGIN: ")
                                            print("------------------------------------------")
                                            account=int(input("Account Number : "))
                                            if account==accnum:
                                                passcode=int(input("Login Passcode : "))
                                                if passcode==loginpin:
                                                    print("------------------------------------------")
                                                    print("\t\tLogin Successfully")
                                                    print("------------------------------------------")
                                                    print("\n\n")
                                                    print("\t•••••••• ATM ••••••••")
                                                    print("------------------------------------------")
                                                    print("Hello",name,"...")
                                                    print("Welcome to ATM")
                                                    
                                                    # displaying the language on the screen
                                                    print("------------------------------------------")
                                                    print("\tINSERT DEBIT CARD")
                                                    print("------------------------------------------")
                                                    print("\nSelect Language: \n")
                                                    print(" 1. Telugu\n","2. Hindi\n","3. English\n")
                                                    
                                                    # selecting the language
                                                    language=int(input("Enter option number for Langauge Selection: "))
                                                    
                                                    #telugu version
                                                    if language==1:
                                                        
                                                        #typing the passcode
                                                        passcode=int(input("\n4 అంకెల డెబిట్ కార్డ్ పాస్‌కోడ్‌ని నమోదు చేయండి: "))
                                                        if passcode>=1000 and passcode<=9999:
                                                            print("\n------------------------------------------")
                                                            print("\tపాస్‌కోడ్ నిర్ధారించబడింది\t")
                                                            print("------------------------------------------")
                                                            
                                                            #options in ATM
                                                            print("ఎంపికను ఎంచుకోండి: \n")
                                                            print(" 1. డిపాజిట్\n","2. ఉపసంహరణ\n","3. పిన్ మార్పు\n","4. సంతులనం\n")
                                                        
                                                            #after passcode showing the options: 
                                                            # [ deposit, withdrawal, pin change, balance enquiry ]
                                                            # selection is about the options in ATM
                                                            
                                                            selection=int(input("ఎంపికలను నమోదు చేయండి: "))
                                                        
                                                            #deposit
                                                            if selection==1:
                                                                print("\n\t\tమొత్తాన్ని డిపాజిట్ చేయండి \n\tకనీస డిపాజిట్ వంద నుండి లక్ష \n")
                                                                depin=int(input("\nడిపాజిట్ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                if depin==passcode:
                                                                    depamo=int(input("\nడిపాజిట్ మొత్తాన్ని నమోదు చేయండి:"))
                                                                    if depamo>=100 and depamo <=100000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tమొత్తం ",depamo,"డిపాజిట్ చేయబడింది ","\n\t\tధన్యవాదాలు")
                                                                        print("------------------------------------------")
                                                                        print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\ndeposited amount : ",depamo)
                                                                            print("balance amount   : ",balance+depamo,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tమొత్తం",depamo, "డిపాజిట్ చేయలేదు")
                                                                        print("------------------------------------------")
                                                                else: 
                                                                    print("------------------------------------------")
                                                                    print("\t తప్పు పాస్‌కోడn\n\tధన్యవాదాలు")
                                                                    print("------------------------------------------")
                                                        
                                                            #withdrawal
                                                            elif selection==2:
                                                                print("\n\t\tమొత్తాన్ని ఉపసంహరించుకోండి\n\tకనీస ఉపసంహరణ వంద నుండి లక్ష వరకు\n")
                                                                drapin=int(input("\nఉపసంహరణ కోసం పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                if drapin==passcode:
                                                                    draw=int(input("\nఉపసంహరణ మొత్తాన్ని నమోదు చేయండి:"))
                                                                    if draw<=balance:
                                                                        print("\n------------------------------------------")
                                                                        print("\t",draw,"మీ ఖాతా నుండి డెబిట్ చేయబడింది\n\t\tధన్యవాదాలు")
                                                                        print("------------------------------------------")                               
                                                                        print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\nwithdraw amount : ",draw)
                                                                            print("balance amount  : ",balance-draw,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\t",draw,"ఉపసంహరించుకోలేము")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                    print("------------------------------------------")
                                                                    
                                                        
                                                            #change pin 
                                                            elif selection==3:
                                                                print("\n పాస్‌కోడ్ మార్చండి : \n")
                                                                chapin=int(input("\nపాత పిన్‌ను నమోదు చేయండి:"))
                                                                if chapin==passcode:
                                                                    chanew=int(input("\nకొత్త పిన్‌ను నమోదు చేయండి: "))
                                                                    if chanew!=chapin:
                                                                        print("\n------------------------------------------")
                                                                        print("\tకొత్త పాస్‌కోడ్ యాక్టివేట్ చేయబడింది")
                                                                        print("------------------------------------------")
                                                                        print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\nyour new passcode is activated")
                                                                            print("Balance Amount : ",balance,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tతప్పు పాస్‌కోడ్")
                                                                        print("------------------------------------------")
                                                                else: 
                                                                    print("------------------------------------------")
                                                                    print("\tతప్పు పాస్‌కోడ్\n\tధన్యవాదాలు")
                                                                    print("------------------------------------------")
                                                        
                                                            #balance enquiry
                                                            elif selection==4:
                                                                print("\n బ్యాలెన్స్ విచారణ: \n")
                                                                balpin=int(input("\nబ్యాలెన్స్ తనిఖీ చేయడానికి పాస్‌కోడ్‌ను నమోదు చేయండి: "))
                                                                if passcode==balpin:
                                                                    print("\n------------------------------------------")
                                                                    print("\tసంతులనం: ",balance)
                                                                    print("------------------------------------------")
                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                    opt=int(input("Enter Option: "))
                                                                    if opt==1:
                                                                        timer()
                                                                        print("\n\n------------------------------------------")
                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                        print("------------------------------------------")
                                                                        from datetime import datetime
                                                                        today=datetime.today().date()
                                                                        from datetime import datetime
                                                                        week=datetime.today()
                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                        print("------------------------------------------")
                                                                        print("NAME           : ",name)
                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                        print("------------------------------------------")
                                                                        print("\nBalance amount : ",balance,"\n")
                                                                        print("------------------------------------------")
                                                                        print("\t\tTHANK YOU\t\t")
                                                                        print("------------------------------------------")
                                                                    elif opt==2:
                                                                        print("------------------------------------------")
                                                                        print("\n\tTHANK YOU FOR SAVING PAPERS\n ")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tNo Option\n\tThank You")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tతప్పు పాస్‌కోడ్")
                                                                    print("------------------------------------------")
                                                            else: 
                                                                print("------------------------------------------")
                                                                print("\tచెల్లని సంఖ్య")
                                                                print("------------------------------------------")
                                                        elif passcode==0000:
                                                            print("\n------------------------------------------")
                                                            print("\tబలహీనమైన పాస్‌కోడ్\n\tమరొకటి ప్రయత్నించండి")
                                                            print("------------------------------------------")
                                                        else:
                                                            print("\n------------------------------------------")
                                                            print("\tపాస్‌కోడ్‌ని రీచెక్ చేయండి\nపాస్కోడ్ 4 అంకెలను మాత్రమే కలిగి ఉంటుంది")
                                                            print("------------------------------------------")

                                                    #hindi version
                                                    elif language==2:
                                                        #typing the passcode
                                                        passcode=int(input("\n4 अंकों का डेबिट कार्ड पासकोड दर्ज करें: "))
                                                        if passcode>=1000 and passcode<=9999:
                                                            print("\n\tपासकोड की पुष्टि की गई\t\n")
                                                        
                                                            #options in ATM
                                                            print("\nविकल्प दर्ज करें: ")
                                                            print(" 1. जमा\n","2. निकासी\n","3. पिन परिवर्तन\n","4. संतुलन\n")
                                                        
                                                            #after passcode showing the options: 
                                                            # [ deposit, withdrawal, pin change, balance enquiry ]
                                                            # selection is about the options in ATM
                                                            selection=int(input("\nविकल्प दर्ज करें: "))
                                                        
                                                            #deposit
                                                            if selection==1:
                                                                print("\nराशि जमा करें: \n")
                                                                depin=int(input("\n जमा करने के लिए पास कोड दर्ज करें: \n"))
                                                                if depin==passcode:
                                                                    print("\tन्यूनतम जमा एक सौ से एक लाख तक")
                                                                    depamo=int(input("\nजमा राशि दर्ज करें: \n"))
                                                                    if depamo>=100 and depamo <=100000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tमात्रा ",depamo,"जमा किया जाता है","\n\t\tधन्यवाद")
                                                                        print("------------------------------------------")
                                                                        print("\nDo you want Mini Statemate ?\n1. yes\n2. no\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\nDeposited Amount : ",depamo)
                                                                            print("Balance Amount   : ",balance+depamo,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tमात्रा",depamo, "जमा नहीं किया गया है")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tगलत पासकोड\nध\tन्यवाद")    
                                                                    print("------------------------------------------")
                                                            #withdrawal
                                                            elif selection==2:
                                                                print("\nराशि वापस लें: n")
                                                                print("न्यूनतम निकासी एक सौ")
                                                                wipin=int(input("\nनिकासी के लिए पासकोड दर्ज करें: "))
                                                                if wipin==passcode:
                                                                    draw=int(input("\nनिकासी राशि दर्ज करें: "))
                                                                    if draw<=balance:
                                                                        print("\n------------------------------------------")
                                                                        print("\t",draw,"आपके खाते से डेबिट कर दिया गया है\n\t\tधन्यवाद")
                                                                        print("------------------------------------------")
                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\nWithdraw Amount : ",draw)
                                                                            print("Balance Amount  : ",balance-draw,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\tTHANK YOU FOR SAVING PAPERS")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\t",draw,"वापस नहीं लिया जा सकता")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tगलत पासकोड\n\tधन्यवाद")
                                                                    print("------------------------------------------")
                                                        
                                                            #change pin 
                                                            elif selection==3:
                                                                print("\nपासकोड बदलें: ")
                                                                chapin=int(input("\nपुराना पिन दर्ज करें: "))
                                                                if chapin==passcode:
                                                                    chanew=int(input("\nनया पिन दर्ज करें: "))
                                                                    if chanew!=chapin:
                                                                        print("\n------------------------------------------")
                                                                        print("\tनया पासकोड सक्रिय")
                                                                        print("------------------------------------------")
                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\nYour New Passcode Is Activated")
                                                                            print("Balance Amount : ",balance,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\tTHANK YOU FOR SAVING PAPERS ")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tपहले से मौजूद पासकोड")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tगलत पासकोड\n\tधन्यवाद")       
                                                                    print("------------------------------------------")
                                                        
                                                            #balance enquiry
                                                            elif selection==4:
                                                                print("\nबैलेंस पूछताछ: \n")
                                                                balpin=int(input("\nबैलेंस चेक करने के लिए पासकोड दर्ज करें:"))
                                                                if passcode==balpin:
                                                                    print("\n------------------------------------------")
                                                                    print("\tसंतुलन: ",balance)
                                                                    print("------------------------------------------")
                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                    opt=int(input("Enter Option: "))
                                                                    if opt==1:
                                                                        timer()
                                                                        print("\n\n------------------------------------------")
                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                        print("------------------------------------------")
                                                                        from datetime import datetime
                                                                        today=datetime.today().date()
                                                                        from datetime import datetime
                                                                        week=datetime.today()
                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                        print("------------------------------------------")
                                                                        print("NAME           : ",name)
                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                        print("------------------------------------------")
                                                                        print("\nBalance  Amount : ",balance,"\n")
                                                                        print("------------------------------------------")
                                                                        print("\t\tTHANK YOU\t\t")
                                                                        print("------------------------------------------")
                                                                    elif opt==2:
                                                                        print("------------------------------------------")
                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                        print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\tNo Option\n\tThank You")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tग़लत पासकोड")
                                                                    print("------------------------------------------")
                                                            else: 
                                                                print("------------------------------------------")
                                                                print("\tअमान्य संख्या")
                                                                print("------------------------------------------")
                                                        elif passcode==0000:
                                                            print("------------------------------------------")
                                                            print("\tकमजोरकोड पास\n\tकोई अन्य प्रयास करें")
                                                            print("------------------------------------------")
                                                        else:
                                                            print("------------------------------------------")
                                                            print("\tपासकोड दोबारा जांचें\nपासकोड में केवल 4 अंक होते हैं")
                                                            print("------------------------------------------")
                                                            
                                                            #9tabs english version//
                                                    elif language==3:
                                                        #typing the passcode
                                                        passcode=int(input("Set 4 Digit Debit Card Passcode: "))
                                                        if passcode>=1000 and passcode<=9999:
                                                            print("------------------------------------------")
                                                            print("\tPasscode Confirmed\t")
                                                            print("------------------------------------------\n")
                                                        
                                                            #options in ATM 
                                                            print("Enter Options: ")
                                                            print(" 1. Deposit\n","2. Withdrawal\n","3. Pin Change\n","4. Balance\n")
                                                        
                                                            #after passcode showing the options: 
                                                            # [ deposit, withdrawal, pin change, balance enquiry ]
                                                            # selection is about the options in ATM
                                                            selection=int(input("Enter Options: "))
                                                        
                                                            #deposit
                                                            if selection==1:
                                                                print("\nDEPOSITE YOUR AMOUNT:  \n")
                                                                depin=int(input("\nEnter passcode to deposite: "))
                                                                if depin==passcode:
                                                                    print("\tMinimum deposit one hundred to one lakh \n")
                                                                    depamo=int(input("\nEnter the deposit amount: "))
                                                                    if depamo>=100 and depamo <=100000:
                                                                        print("\n------------------------------------------")
                                                                        print("\tAmount ",depamo," is deposited","\n\t\tThank You")
                                                                        print("------------------------------------------")
                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\nDeposited Amount : ",depamo)
                                                                            print("Balance Amount   : ",balance+depamo,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\tTHANK YOU FOR SAVING PAPERS")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\t",depamo,"is can't be deposited")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tIncorrect Passcode\n\tThank You")
                                                                    print("------------------------------------------")
                                                        
                                                            #withdrawal
                                                            elif selection==2:
                                                                print("\nWITHDRAWAL YOUR AMOUNT:  ")
                                                                print("\nMinimum withdrawal One Hundred to One Lakh\n")
                                                                wipin=int(input("Enter passcode to withdrawal: "))
                                                                if wipin==passcode: 
                                                                    draw=int(input("\nEnter the withdrawal amount: "))
                                                                    if draw<=balance:
                                                                        print("\n------------------------------------------")
                                                                        print("\t",draw,"is debited from your account\n\t\tthank you")
                                                                        print("------------------------------------------")
                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\nwithdraw amount : ",draw)
                                                                            print("balance amount  : ",balance-draw,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\tTHANK YOU FOR SAVING PAPERS")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                    else:
                                                                        print("------------------------------------------")
                                                                        print("\t",draw,"can't be withdraw")
                                                                        print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tIncorrect Passcode\n\tThank You")
                                                                    print("------------------------------------------")
                                                        
                                                            #change pin 
                                                            elif selection==3:
                                                                print("\nCHANGE THE PASSCODE: ")
                                                                chapin=int(input("\nenter the old pin: "))
                                                                if chapin==passcode:
                                                                    chanew=int(input("\nenter new pin: "))
                                                                    if chanew==chapin:
                                                                        print("\nalready existing passcode")
                                                                    else:    
                                                                        print("\n------------------------------------------")
                                                                        print("\tNew Passcode Activated")
                                                                        print("------------------------------------------")
                                                                        print("\nDo you want mini statemate ?\n1. Yes\n2. No\n")
                                                                        opt=int(input("Enter Option: "))
                                                                        if opt==1:
                                                                            timer()
                                                                            print("\n\n------------------------------------------")
                                                                            print("\t\tMINI STATEMENT\t\t")
                                                                            print("------------------------------------------")
                                                                            from datetime import datetime
                                                                            today=datetime.today().date()
                                                                            from datetime import datetime
                                                                            week=datetime.today()
                                                                            print("Date & Day     : ",today,week.strftime("%A"))
                                                                            print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                            print("------------------------------------------")
                                                                            print("NAME           : ",name)
                                                                            print("ACCOUNT NUMBER : ",accnum)
                                                                            print("------------------------------------------")
                                                                            print("\nYour New Passcode Is Activated")
                                                                            print("Balance Amount : ",balance,"\n")
                                                                            print("------------------------------------------")
                                                                            print("\t\tTHANK YOU\t\t")
                                                                            print("------------------------------------------")
                                                                        elif opt==2:
                                                                            print("------------------------------------------")
                                                                            print("\tTHANK YOU FOR SAVING PAPERS")
                                                                            print("------------------------------------------")
                                                                        else:
                                                                            print("------------------------------------------")
                                                                            print("\tNo Option\n\tThank You")
                                                                            print("------------------------------------------")
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tIncorrect Passcode\n\tThank You")
                                                                    print("------------------------------------------")
                                                        
                                                            #balance enquiry
                                                            elif selection==4:
                                                                print("\nBALANCE ENQUIRY: ")
                                                                balpin=int(input("\nEnter the passcode to check balance: "))
                                                                if passcode==balpin:
                                                                    print("\n------------------------------------------")
                                                                    print("\tBalance: ",balance)
                                                                    print("------------------------------------------")
                                                                    print("\nDo you want Mini Statemate ?\n1. Yes\n2. No\n")
                                                                    opt=int(input("Enter Option: "))
                                                                    if opt==1:
                                                                        timer()
                                                                        print("\n\n------------------------------------------")
                                                                        print("\t\tMINI STATEMENT\t\t")
                                                                        print("------------------------------------------")
                                                                        from datetime import datetime
                                                                        today=datetime.today().date()
                                                                        from datetime import datetime
                                                                        week=datetime.today()
                                                                        print("Date & Day     : ",today,week.strftime("%A"))
                                                                        print("Time           : ",week.strftime("%I"),":",week.strftime("%M"),":",week.strftime("%S"),week.strftime("%p"))
                                                                        print("------------------------------------------")
                                                                        print("NAME           : ",name)
                                                                        print("ACCOUNT NUMBER : ",accnum)
                                                                        print("------------------------------------------")
                                                                        print("\nBalance Amount : ",balance,"\n")
                                                                        print("------------------------------------------")
                                                                        print("\t\tTHANK YOU\t\t")
                                                                        print("------------------------------------------")
                                                                    elif opt==2:
                                                                        print("------------------------------------------")
                                                                        print("\tTHANK YOU FOR SAVING PAPERS")
                                                                        print("------------------------------------------")
                                                                    else:    
                                                                    
                                                                        print("------------------------------------------")
                                                                        print("\tNo Option\n\tThank You")
                                                                        print("------------------------------------------")
                                                                        
                                                                else:
                                                                    print("------------------------------------------")
                                                                    print("\tIncorrect Passcode")
                                                                    print("------------------------------------------")
                                                            else: 
                                                                print("------------------------------------------")
                                                                print("\tInvalid Number")
                                                                print("------------------------------------------")
                                                        elif passcode==0000:
                                                            print("\n------------------------------------------")
                                                            print("\tWeak Passcode\n\tTry Another")
                                                            print("------------------------------------------")
                                                        else:
                                                            print("\n------------------------------------------")
                                                            print("\t\tRecheck Passcode\nPasscode Contains Only 4 digits")
                                                            print("------------------------------------------")
                                                            print("\n\t\tThank You")
                                                    else:
                                                        print("------------------------------------------")
                                                        print("\tInvalid Number")
                                                        print("------------------------------------------")
                                                else:
                                                    print("------------------------------------------")
                                                    print("\tIncorrect Passcode")
                                                    print("------------------------------------------")
                                            else:
                                                print("------------------------------------------")
                                                print("\tAccount Number Not Exist")
                                                print("------------------------------------------")
                                        elif ulogin==2:
                                            print("\n------------------------------------------")
                                            print("Try To Login Into Your Created Account\nCheck Out Our ATM Features\n\n\tThank You")
                                            print("------------------------------------------")
                                        else:
                                            print("\n------------------------------------------")
                                            print("\tNo Option\n\tThank You")
                                            print("------------------------------------------")                                
                                    else:
                                        print("------------------------------------------")
                                        print("\tOption Doesn't Exist")      
                                        print("------------------------------------------")  
                                else:
                                    print("\n---------------------------------------------------------")
                                    print("\tConfirm Passcode Is Unmatch With Login Passcode")
                                    print("---------------------------------------------------------")
                            elif loginpin==000000:
                                print("\n------------------------------------------")
                                print("\tWeek Passcode\n\tChange It")
                                print("------------------------------------------")
                            else:
                                print("\n------------------------------------------")
                                print("\tYour Passcode Must Contain 6 Digits")
                                print("------------------------------------------")
                        else:
                            print("\n------------------------------------------")
                            print("minimum initial deposite should more than\n\tRs. 2000 upto Rs. 100000")
                            print("------------------------------------------")      
                    else:
                        print("\n------------------------------------------")
                        print("\tRecheck Your Account Number\n\tEnter 10 Digits Account Number")
                        print("------------------------------------------")
                else:
                    print("\n------------------------------------------")
                    print("\tRecheck Your Mobile Number\n\tEnter 10 Digit Mobile Number")
                    print("------------------------------------------")  
            else:
                print("\n------------------------------------------")
                print("\t\tMental Illness\n\tGender Doesn't Exist")
                print("------------------------------------------")
        else:
            print("\n------------------------------------------")
            print("\tMinors Can't Create Bank Accountt\n\t\t\t\tThank You")
            print("------------------------------------------")
        print("\n\n")    
   
    #using whole banking function in one line function        
    atm()
    
    #asking for multiple bank account new bank account
    newacc=int(input("\nDo You Want To Create Second Bank Account: \n1. Create New Account\n2. Logout Existing Account\n\nEnter Option: "))
    if newacc==1:
        atm()
        noofnewacc=int(input("\nDear Customer ,\n\tHow Many Bank Accounts You Want To Create Further ?\n\nEnter Number Of New Bank Account To Create: "))        
        for i in range(noofnewacc):
            atm()
        print("\n------------------------------------------")
        print("Total",noofnewacc+2,"Bank Accounts Have Been Created\n\t\tThank You\n\tYour Data Is Safe\n\tAll Accounts has Been Loged Out")
        print("------------------------------------------")    
    elif newacc==2:
        print("\n------------------------------------------")
        print("You Have Succesfully Logout from The\n\tLEGEND MOBILE BANKING\n\n\tThank You")
        print("------------------------------------------")    
    else:
        print("\n------------------------------------------")
        print("\tNo Option\n\tThank You")
        print("------------------------------------------")           
else:
    print("\n------------------------------------------")
    print("\tNo Option\n\tThank You")
    print("------------------------------------------")
                                                                                            
                                                                        