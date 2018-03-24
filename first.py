print"hello buddy"
print"let's get started"
spy_name = raw_input(" what is your spy name?? ")
if len(spy_name) > 2:
    print "welcome " + spy_name
    spy_salutation = raw_input("what should i call you(mr. or ms. )?")
    if spy_salutation == "mr." or spy_salutation == "ms.":
        spy_name = spy_salutation + " " + spy_name
        spy_no = input("enter your mobile no")
        print "alright" + spy_salutation + " " + spy_name + " i wolud like to know little bit more about u"
        spy_age = input(" what is your age ")
        if 16 < 50 > spy_age:
            print("you are most welcome to spy_chat app")

            spy_rating = input("what is your spy_rating")
            if spy_rating > 5.0:
                print "you are an very good spy"
            elif 3.5 < spy_rating <= 5.0:
                print "you are an good spy"
            elif 2.5 < spy_rating <= 3.5:
                print "you are an average spy"
            else:
                print "you have to learn more"

                spy_is_online = True
            print "authentication is complete , welcome: " + spy_name + " age: " + str(spy_age) + " rating: " + str(
                spy_rating) + " welcome to spy_chat app "
        else:
            print("you are no eligible for being spy")

    else:
        print"invalid salutation"
else:
    print ("oops , this not a valid name")
