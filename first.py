from userdetail import spy_name,spy_age,spy_rating
print"hello buddy"
print"let's get started"

STATUS_MESSAGE = ["GALTI BADI GALTI ENGINEERING", "SLEEPING", "DON'T DESTRUBE", "BUSY CALL U LATER"]
frnd_name = ["ravi"]
frnd_age =[26]
frnd_rating =[3.8]
frnd_is_online =[]


def add_status (c_status):
    if c_status!= None:
        print "current status is none" + c_status
    else:
        print"you dont have any status"
        existing_status=raw_input("Do you want to select from old status ? Y/N ")
        if existing_status.upper()=="N":
            New_status = raw_input("Enter your Status: ")
            if len(New_status)>0:
                STATUS_MESSAGE.append(New_status)
        elif existing_status.upper()=="Y":
            serial_no = 1
            for old_status in STATUS_MESSAGE:
                print str(serial_no)+ " " + old_status
                serial_no = serial_no +1
                user_choise=input("eneter your choise ")
                New_status =  STATUS_MESSAGE[user_choise-1]
                update_status=New_status
                return update_status


            def add_friend():
                friend_name=raw_input("what is your name ?")
                friend_age=input("what is your age")
                friend_rating=input("what is your rating")
                if len (friend_name)>2 and 12<friend_age<50 and friend_rating>spy_rating:
                    frnd_name.append(friend_name)
                    frnd_age.append(friend_age)
                    frnd_rating.append(friend_rating)
                    frnd_is_online.append(True)
                else:
                    print"Friend cannot be added"
                    return len(frnd_name)










def start_chat(spy_name,spy_age,spy_rating):
    print "here is your option" + spy_name
    current_status= None
    show_menu = True
    while show_menu:
        choise = input("what do you want to do? \n 1. Add a status \n 2.Add a friend \n 3. Send a message \n 4. Receive a message \n0. Exit")#Taking choise from the user

        if choise == 1:
            current_status = add_status(current_status)
            print " updated status is " + current_status

        elif choise == 2:
            no_of_frnds = add_friends()
            print "you have " + str(no_of_frnds) + "friends"
        elif choise == 0:
            show_menu = False;
        else:
            print "Invalid input"




spy_exits = raw_input("Are you a new user? Y/N ")
if spy_exits.upper()=="N":
    print "welcome back"  +spy_name + "age " + str(spy_age) +"having rating of" +str(spy_rating)
    start_chat(spy_name, spy_age , spy_rating)

elif spy_exits.upper()=="Y":
    spy_name=raw_input("what is your spy name?")
    if len(spy_name)>2:#checking the length of the name which should greater then two
        print "welcome" + spy_name + "Glad to have you back with us"
    spy_salutation = raw_input("what should i call you(mr. or ms. )?")
    if spy_salutation == "mr." or spy_salutation == "ms.":
        spy_name = spy_salutation + " " + spy_name
        spy_no = input("enter your mobile no")
        print "alright" + spy_salutation + " " + spy_name + " i wolud like to know little bit more about u"
        spy_age = input(" what is your age ")#input taken from the user
        if 16 < 50 > spy_age:#conditional statement
            print("you are most welcome to spy_chat app")

            spy_rating = input("what is your spy_rating")
            if spy_rating > 5.0:#conditional statement
                print "you are an very good spy"
            elif 3.5 < spy_rating <= 5.0:#conditional statement
                print "you are an good spy"
            elif 2.5 < spy_rating <= 3.5:#conditional statement
                print "you are an average spy"
            else:
                print "you have to learn more"

                spy_is_online = True#initilizing the variable
            print "authentication is complete , welcome: " + spy_name + " age: " + str(spy_age) + " rating: " + str(
                spy_rating) + " welcome to spy_chat app "
        else:
            print("you are no eligible for being spy")#message to the user

    else:
        print"invalid salutation"
else:
    print ("oops , this not a valid name")#message to the user
