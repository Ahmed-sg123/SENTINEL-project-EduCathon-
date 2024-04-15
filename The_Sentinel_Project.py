                                                                #    ____   _____  _   _  _____  ___  _   _  _____  _
                                                                #   / ___| | ____|| \ | ||_   _||_ _|| \ | || ____|| |        
                                                                #   \___ \ |  _|  |  \| |  | |   | | |  \| ||  _|  | |        
                                                                #    ___) || |___ | |\  |  | |   | | | |\  || |___ | |___     
                                                                #   |____/ |_____||_| \_|  |_|  |___||_| \_||_____||_____|    

                                                                #             ____   ____    ___       _  _____   ____  _____ 
                                                                #            |  _ \ |  _ \  / _ \     | || ____| / ___||_   _|
                                                                #            | |_) || |_) || | | | _  | ||  _|  | |      | |  
                                                                #            |  __/ |  _ < | |_| || |_| || |___ | |___   | |  
                                                                #            |_|    |_| \_\ \___/  \___/ |_____| \____|  |_|  


#libraries
import os
import re
import hashlib
import time
from art import *

#__________________________________________________________________________________________________________________________________#
# This code will ask about 30 questions to analyze the outcomes and determine your health state


def healthcare_checker():
    
    def feverchecker(ob1, ob2):
        if ob1 == 'yes':
            return 1
        elif ob2 == 'yes':
            return 1
        else:
            return 0



#__________________________________________________________________________________________________________________________________#
#greetings

    print('Hello',name, '!')
    print('Let\'s check your health state.')



#_____________________________________________________________________________________________________________________________________#
# Ask questions about symptoms
    
    
    q1 = input("Have you been experiencing fever? (yes/no): ")
    q2 = input("Have you been feeling cold? (yes/no): ")
    q3 = input("Have you been experiencing cough? (yes/no): ")
    q4 = input("Have you been experiencing shortness of breath? (yes/no): ")
    q5 = input("Have you been experiencing headache? (yes/no): ")
    q6 = input("Have you been experiencing muscle pain? (yes/no): ")
    q7 = input("Have you been experiencing fatigue? (yes/no): ")
    q8 = input("Have you been experiencing loss of appetite? (yes/no): ")
    q9 = input("Have you been experiencing sore throat? (yes/no): ")
    q10 = input("Have you been experiencing diarrhea? (yes/no): ")
    q11 = input("Have you been experiencing nausea? (yes/no): ")
    q12 = input("Have you been experiencing vomiting? (yes/no): ")
    q13 = input("Have you been experiencing abdominal pain? (yes/no): ")
    q14 = input("Have you been experiencing chest pain? (yes/no): ")
    q15 = input("Have you been experiencing swelling? (yes/no): ")
    q16 = input("Have you been experiencing rash? (yes/no): ")
    q17 = input("Have you been experiencing joint pain? (yes/no): ")
    q18 = input("Have you been experiencing difficulty sleeping? (yes/no): ")
    q19 = input("Have you been experiencing changes in vision? (yes/no): ")
    q20 = input("Have you been experiencing changes in urination? (yes/no): ")
    q21 = input("Have you been experiencing dizziness? (yes/no): ")
    q22 = input("Have you been experiencing numbness or tingling? (yes/no): ")
    q23 = input("Have you been experiencing swollen lymph nodes? (yes/no): ")
    q24 = input("Have you been experiencing night sweats? (yes/no): ")
    q25 = input("Have you been experiencing unexplained weight loss or gain? (yes/no): ")
    q26 = input("Have you been experiencing difficulty swallowing? (yes/no): ")
    q27 = input("Have you been experiencing frequent urination? (yes/no): ")
    q28 = input("Have you been experiencing blood in urine or stool? (yes/no): ")
    q29 = input("Have you been experiencing anxiety or depression? (yes/no): ")
    q30 = input("Have you been experiencing memory loss or confusion? (yes/no): ")
    os.system('cls')
    
    
#______________________________________________________________________________________________________________________#
# Analyze the outcomes 
    
    
    
    outcome1 = feverchecker(q1, q2)
    outcome2 = 1 if q3 == 'yes' else 0
    outcome3 = 1 if q5 == 'yes' else 0
    outcome4 = 1 if q6 == 'yes' else 0
    outcome5 = 1 if q7 == 'yes' else 0
    outcome6 = 1 if q8 == 'yes' else 0
    outcome7 = 1 if q9 == 'yes' else 0
    outcome8 = 1 if q10 == 'yes' else 0
    outcome9 = 1 if q11 == 'yes' else 0
    outcome10 = 1 if q12 == 'yes' else 0
    outcome11 = 1 if q13 == 'yes' else 0
    outcome12 = 1 if q14 == 'yes' else 0
    outcome13 = 1 if q15 == 'yes' else 0
    outcome14 = 1 if q16 == 'yes' else 0
    outcome15 = 1 if q17 == 'yes' else 0
    outcome16 = 1 if q18 == 'yes' else 0
    outcome17 = 1 if q19 == 'yes' else 0
    outcome18 = 1 if q20 == 'yes' else 0
    outcome19 = 1 if q21 == 'yes' else 0
    outcome20 = 1 if q22 == 'yes' else 0
    outcome21 = 1 if q23 == 'yes' else 0
    outcome22 = 1 if q24 == 'yes' else 0
    outcome23 = 1 if q25 == 'yes' else 0
    outcome24 = 1 if q26 == 'yes' else 0
    outcome25 = 1 if q27 == 'yes' else 0
    outcome26 = 1 if q28 == 'yes' else 0
    outcome27 = 1 if q29 == 'yes' else 0
    outcome28 = 1 if q30 == 'yes' else 0




#_____________________________________________________________________________________________________________#
#outcomes


    print()
    print()
    print("Based on your responses, here are the outcomes:")

    
    
    
    
#_______________________________________________________________________________________________________________#
# Check if there are any symptoms before printing the final message
    
    
    
    if outcome1 + outcome2 + outcome3 + outcome4 + outcome5 + outcome6 + outcome7 + outcome8 + outcome9 + outcome10 + outcome11 + outcome12 + outcome13 + outcome14 + outcome15 + outcome16 + outcome17 + outcome18 + outcome19 + outcome20 + outcome21 + outcome22 + outcome23 + outcome24 + outcome25 + outcome26 + outcome27 + outcome28 == 0:
        print("No significant health concerns detected. However, please maintain a healthy lifestyle and consult a healthcare professional if you experience any new or worsening symptoms.")
    else:
    
    
    
    
    
#_______________________________________________________________________________________________________________#
# symptom analyzing
        
        
        print("You may be experiencing symptoms of the following conditions:")
        conditions = []
        if outcome1 == 1:
            conditions.append("fever")
        if outcome2 == 1:
            conditions.append("respiratory infection")
        if 1 == outcome3 or 1 == outcome4 or 1 == outcome5:
            conditions.append("common cold or flu")
        if 1 == outcome6:
            conditions.append("loss of appetite")
        if 1 == outcome7 or 1 == outcome9 or 1 == outcome10 or 1 == outcome11:
            conditions.append("gastrointestinal infection")
        if 1 == outcome12:
            conditions.append("heart-related symptoms")
        if 1 == outcome13 or 1 == outcome14 or 1 == outcome15:
            conditions.append("musculoskeletal or dermatological condition")
        if 1 == outcome16 or 1 == outcome17 or 1 == outcome18 or 1 == outcome19 or 1 == outcome20 or 1 == outcome21 or 1 == outcome22 or 1 == outcome23 or 1 == outcome24 or 1 == outcome25 or 1 == outcome26:
            conditions.append("neurological or urological condition")
        if 1 == outcome27:
            conditions.append("mental health condition")
        if 1 == outcome28:
            conditions.append("cognitive impairment")

        print()
        print()
        print()
        print(", ".join(conditions))
        print()
        
        
        
        
        
#_____________________________________________________________________________________________________________________#
# the last result_________________
        
        
        
        
        if "fever" in conditions:
            print("You are advised to rest and monitor your temperature. If it persists, please consult a healthcare professional.")
        if "respiratory infection" in conditions:
            print("You are advised to consult a healthcare professional for further evaluation and treatment.")
        if "common cold or flu" in conditions:
            print("Rest and drink plenty of fluids. If symptoms persist, please consult a healthcare professional.")
        if "loss of appetite" in conditions:
            print("You are advised to eat nutritious food and stay hydrated. If symptoms persist, please consult a healthcare professional.")
        if "gastrointestinal infection" in conditions:
            print("Rest and stay hydrated. If symptoms persist, please consult a healthcare professional.")
        if "heart-related symptoms" in conditions:
            print("You are advised to seek immediate medical attention.")
        if "musculoskeletal or dermatological condition" in conditions:
            print("Please consult a healthcare professional for further evaluation.")
        if "neurological or urological condition" in conditions:
            print("Please consult a healthcare professional for further evaluation.")
        if "mental health condition" in conditions:
            print("Please consult a professional Therapist for further evaluation.")
        if "cognitive impairment" in conditions:
            print("Please consult a healthcare professional for further evaluation.")

    print()
    print()
    print()
    print("           please note this is not totally reliable and the software is still under development so if any of the symptoms appeared it's better to take professional healthcare/doctor consult                     ")
    print()
    print("                                                                                                TAKE CARE                                                                                                                                             ")


#--------------------------------------------------------#
def gender_idf(x):
    x = 0
    while x == 0 :
        gender = input('Enter Your Gender (M/F): ').upper()
        if gender == 'M':
            x = 1
            return 'M'  
        elif gender == 'F':
            x = 1
            return  'F'
            
        else:
            x = 0
            print("undefined gender. please try again")


    

#__________________________________________________________________________________________________________________________________#
#sign up  page




def sign_up():
    
    user=input("enter username : ")
    def pass_process():
        pwd=input("enter your password..: ")
        return pwd  
    pwd1 = pass_process()

    while passwordchecker(pwd1)== False:
       pwd1 = pass_process()
    con_pwd=input("confirm your password: ") 
    while not con_pwd == pwd1 :
        print("password confirmation is wrong. please try again")
        con_pwd=input("confirm your password: ")
    email = input('Enter Your Email Address: ')
    if email == '':
        print("email is required")
        email = input('Enter Your Email Address: ')
    phone = input('Enter Your Phone Number: ')
    age = input('Enter Your Age: ')
    gender = input('Enter Your Gender (M/F): ').upper()
    if gender == 'M' or gender == 'F':
        x = 1
        
    else:
        x = 0
        print("undefined gender. please try again")
        gender = gender_idf(x)
    if con_pwd == pwd1:
        enc= con_pwd.encode()
        hash1= hashlib.md5(enc).hexdigest()
        with open("creds.txt", "w") as f:
            f.write(user + "\n")
            f.write(hash1 + "\n")
            f.write(email + "\n")
            f.write(phone + "\n")
            f.write(age + "\n")
            f.write(gender)
        f.close()
        print("registeration was done successfully") 
        
    else: 
        print("passwords do not match")
    
    return user
    
        

#_______________________________________________________________________________________________________________________________#
#login process

def login():
    userlog=input("enter username: ")
    pwdlog=input("enter your password: ")

    with open("creds.txt", "r") as f :
        stored_user, stored_pwd, stored_email, stored_phone, stored_age, stored_gender = f.read().split("\n")
    f.close()
    if userlog == stored_user and hashlib.md5(pwdlog.encode()).hexdigest() == stored_pwd:
        print("login process successful")
        return True,stored_user
    else:
        print("login credentials denied.")
        return False,stored_user
    




#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#
#password checking function




def passwordchecker(password):
    # password checking software
    
    

    def check_password(password):
        if len(password) < 8:
            return False, "unfortunately the Password must be at least 8 characters long"
        if not re.search(r'[A-Z]', password):
            return False, "unfortunately the Password must contain at least one capital letter"
        if not re.search(r'[a-z]', password):
            return False, "unfortunately the Password must contain at least one small letter"
        if not re.search(r'\d', password):
            return False, "unfortunately the Password must contain at least one number"
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False, "unfortunately the Password must contain at least one special character"
        else:
            return True, "password is strong"

    
    result, message = check_password(password)
    if result:
        print(message)
    else:
        print(message)
    return result


#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#
#medical lessons 
def medical_lessons():
    print()
    print()
    tprint("Lessons")
    print("hello",name,"!\nI see you want to take a lesson today. Just to assure you this information was given by Dr.mohammed yasser mohammed shawky.\nthe info might be shortened in case of finishing the project fast and summrarising the lessons.\nthanks for your concern")
    print("of course since you are learning over here you get to choose the lesson from the choices below\n1)simple diffuse goiter\n2)Thyroglossal cyst\n3)Branchial cyst\n ")
    choice=input("--> ")
    os.system('cls')
    if choice == '1' :
        print("simple diffuse goiter is a swelling In front of the neck showing diffuse butterfly shape. the investigations that need to be done are TSH, T3, T4 levels → normal levels in simple goiter Ultrasonography on neck (echo) to detect the size , nodularity, nature, site and presence of goiter CT scan (xray) to detect site and nature “like the echo scan”thyroid scan/Radioactive iodine: to check for uptake of iodine by the gland → normal uptake in simple goiter")
    elif choice == '2' :
        print("Thyroglossal cyst is a lesion which is described as swelling in the midline of the neck. The possible complications of this lesion are infection leading to abscess or fistula, which is due to abscess in a thyroglossal cyst or incomplete removal.The pathological sign of the Thyroglossal cyst lesion is that the lesion moves up with protrusion of the tongue")
    elif choice == '3' :
        print("Branchial cyst is lesion which is located somewhere between the upper and middle third of the neck at the lateral side partially covering the anterior border of sternomastoid muscle.(left side or right side)the possible complications are infection leading to abscess, Branchial fistula, Branchiogenic carcinomathe clinical picture of the Branchial cyst are : Positive transillumination, slowly growing painlessly the treatment of the Branchial cyst lesion is complete excision reaching deep structures near external auditory meatus.")

    elif choice == str():
        print("please note that there is only numbers that you have been given to choose from.\ndon't make up stuff")
    else:
        print("nothing has been detected.")


    print("thanks to Dr.mohammed for his share of the information")


#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#
#quiz charts =D

def quiz():
    print()
    print()
    tprint("Questions")
    print("hello,",name,"and welcome to the quiz of the medical lessons you just took.\nthis is still in beta but hopefully it works just fine.\nlets get started")
    print("question 1: which way can detect the size an nature of the simple difuse goiter?")
    print("1)Ultrasonography on neck\n2)echo scan\n3)Thyroid scan\n4)CT scan")
    x=int(input("--> "))
    if x == 1:
        print("the right answer =D")
    elif x == 2:
        print("wrong answer")
    elif x == 3 :
        print("wrong answer")
    elif x == 4:
        print("wrong answer")
    else:
        print("out numbered choice, please try again")
    

    y=input("ready for another question?(yes,no): ")
    os.system('cls')
    if y =='yes':
        print("question 2 : what are the complications for thyroglossal cyst?")
        print("1)infection and fistula\n2)respiratory obstruction and infection\n3)rapid growing due to aplasia and infection\n4)malignant change and rapid growing due to obstruction.")
        x=int(input("--> "))
        if x ==1:
            print("right answer")
        elif x ==2 :
            print("wrong answer")
        elif x ==3 :
            print(" wrong answer")
        elif x ==4 :
            print("wrong answer")
        else:
            print("undefined choice, try again later.")

    y=input("ready for another question?(yes,no): ")
    os.system('cls')
    if y=='yes':
        print("question 3 : where is the simple diffuse goiter located?")
        print("1)right or left side of the neck\n2)under the tongue\n3)front of the neck\n4)on the limbs")
        x=int(input("--> "))
        if x == 1:
            print("wrong answer")
        elif x == 2:
            print("wrong answer")
        elif x == 3 :
            print("correct answer =D")
        elif x ==4:
            print("wrong answer")
        else:
            print("undefined choice, please try agin later.")
    print()
    print()
    print("there is no more questions..(update soon)")
    
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#
# application choices
# i know its a bad idea to have password checker in the middle of medical stuff codes but its made into that because its important to have a strong password =D the idea is that safety is everything, 

def application(name):
    os.system('cls')
    time.sleep(0.5)
    print("'booting up applications...'(this will take a second)")
    os.system('cls')
    print()
    print()
    tprint("welcome    aboard")
    print("\nhello", name, "first of all let me introduce my self, this is an multi-tasking project\n that is made to ask questions and generates outputs based on your inputs.\n Now to my favorite part""! what would you like to choose?")
    print("\n1)healthcare application\n\n2)medical education and lessons\n\n3)medical quiz(based on the 2nd choice)\n")
    opinion = input("---> ")
    if opinion == "1":
        os.system('cls')
        healthcare_checker()
    elif opinion == "2":
        os.system('cls')
        medical_lessons()
    elif opinion == "3":
        os.system('cls')
        quiz()
    print()
    print()
    x=input("Continue through the rest of the project?(yes,no): ")
    if x == 'yes':
        return 'yes'
    elif x == 'no':
        return 'no'

#__________________________________________________________________________________________________________________________________________________________________________________________________#
#reapeat process so it becomes an active program

os.system('cls')
if os.stat("creds.txt").st_size == 0:
    tprint("            Registration")
    name= sign_up()
    tprint("Hello     There")
    time.sleep(2)
    repeat=application(name)
    while repeat == 'yes':
        os.system('cls')
        repeat = application(name)
else:
    tprint("            Log-in")
    log, name =login()
    if log == True:
        tprint("Hello     There")
        time.sleep(2)
        repeat=application(name)
        while repeat == 'yes':
            os.system('cls')
            repeat = application(name)
    else:
        print ("there is a problem with your username or password")
        print()
        x = input("do you want to change your registration credentials?(Yes,No) ").upper()
        if x == "YES":
            os.system('cls')
            print("wait a moment...")
            time.sleep(2)
            os.system('cls')
            tprint("            Registration")
            name= sign_up()
            tprint("Hello     There")
            time.sleep(2)
            repeat=application(name)
            while repeat == 'yes':
                os.system('cls')
                repeat = application(name)

print()
print()
print()
print("thanks for using the Sentinel project. see you next time.")
print()
