
First_name=str(input("Please enter your first name. :- "))
Secend_name=str(input("Please enter your secend name. :- "))
Email_ID=(input("Please create your new email i'd but please not write @gamil.com . :- "))
Email_ID=Email_ID.__add__("@gmail.com")
def PASS():
    Password=int and str(input("Please enter your new password. :- "))
    Conform_password=int and str(input("Conform your password. :- "))
    word_of_id = Conform_password
    if Conform_password==Password:
        age=int(input("Please enter your age. :- "))
        DOB=int and str (input("Please enter your birth date. :- "))
        DOM=int and str (input("Please input your birth month. :- "))
        DOY=int and str (input("Please input your birth Year. :- "))
        DOB_DOM_DOY=(DOB,DOM,DOY)
        print(DOB_DOM_DOY)
        Gender=str(input("Please input your Gender. Male/Female/Other :- "))
        print("Congratulation you have make a new i'd.")
        Message=int and str (input("Plese input your message. :- "))
        print("ydi aap message dubara dekna chahte hain to apna id fir se login karen.")
        login=input(" kya aap id login karna chahenge. :- ")
        if login=="yes" or login=="Yes" or login=="YES":
            def login_email():
                Email_ID_login=input("Please enter your email i'd. :- ")
                if Email_ID_login==Email_ID:
                    def Pass_word():
                        PASS2=input("Plese enter your password. :- ")
                        if PASS2 == word_of_id:
                            print(Message)
                        else:
                            print("Your password is wrong.")
                            PASS2=""
                            Pass_word()
                    Pass_word()
                else:
                    print("Your email i'd is wrong.")
                    Email_ID_login=""
                    login_email()
            login_email()
        elif login == "no"or login=="No"or login=="NO":
            print("Thankyou.")
        else:
            print("Thankyou.")
    else:
        print("Your conform password is wrong.")
        Conform_password=""
        Password=""
        PASS()
PASS()