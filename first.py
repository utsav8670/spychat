from userdetail import spy ,Spy,chatMessage # importing a file with specific variables
from datetime import datetime#importing date time

time=datetime.now() # current date and time
print time#Display to the user
from steganography.steganography import Steganography#importing Steganography module

print 'Hello Buddy' #greetings given to the user
print 'Let\'s get started' #initialising
STATUS_MESSAGE=['Sleeping', 'Eating', 'I can see you']#predefined status
frnds1 =Spy['MR.','Naman',26,2.3]
frnds2 =Spy['MR.','Chandan',27,2.5]
friends = [frnds1,frnds2]

def add_status(c_status):#function for statud
    if c_status != None:#checking condition if status is not none
        print "Your current status is "+ c_status#Displaying for the user
    else:
        print"You don't have any status currently.."#Displaying for the user
    existing_status = raw_input("You want to select from old status? Y/N")#Asking user to select desired options
    if existing_status.upper() == 'N':#Checking condition
        new_status = raw_input('Enter your status : ')#Required user input for the status
        if len(new_status) > 0:#validating
            STATUS_MESSAGE.append(new_status)#add the status in the list
    elif existing_status.upper() == 'Y':#checking condition
        serial_no = 1#initialising of the seriol number which is placed before any
        for old_status in STATUS_MESSAGE:#traversing the list
            print str(serial_no)+'. '+old_status#displaying for the user
            serial_no = serial_no+1#incrementing
        user_choice = input('Enter your choice :')#required input for the user
        new_status = STATUS_MESSAGE[user_choice-1]#Index value decremented not start with zero
    updated_status = new_status#updating the status
    return updated_status#returning back

def add_friend():
    frnd = {#defining a list
       'name':'',
        'age': 0,
        'rating':0.0,
        'online':True,
        'chats':[]

    }
    frnd['name'] = raw_input('What is your name ? ')#required an input
    frnd['age'] = input('What is your age ? ')#required an input
    frnd['rating'] = input('What is your rating ? ')#required an input
    if len(frnd['name']) > 2 and 12 < frnd['age'] < 50 and frnd['rating'] > spy.rating and frnd['name'].isalpha():#checking for the condition
        friends.append(frnd)#appending in the list

    else:
        print 'Friend cannot be added..'#displaying for the user
    return len(friends)#returning the value for the function

def select_frnd():#display all friend
    serial_no = 1#initialising
    for frnd in friends:#showing all friends using loop
        print str(serial_no) +" "+frnd.name#displaying for the user
        serial_no = serial_no +1 #incrementing
    user_selected_frnd=input("Enter your choice")#input from the user
    user_selected_frnd_index=user_selected_frnd-1#decrementing because list does not start with zero
    return user_selected_frnd_index#returning value to the function


def send_message():#sending a message
    select_friend = select_frnd()#index value
    original_image = raw_input('What is the name of original image ? ')  # asking the user for an input of image
    secret_text = raw_input('What is your secret text ? ')# secret text to be entered
    output_path = "output.jpg"#predefined name of an image
    secret_text = str(select_friend)+secret_text#assigning the index with the text fro a reading a message validation
    Steganography.encode(original_image, output_path, secret_text)  # encoding the message with image
    print 'Message successfully encoded.'#displaying for the user
    new_chat=chatMessage[secret_text,True]
    friends[select_friend].chats.append( new_chat )  # appending the friend chat detail
    print'Your message is ready.'#displaying for the user

def read_message():#reading a message
    select_friend = select_frnd()#index value
    output_path = raw_input('Which image you want to decode ? ')# asking the user for an input of image
    secret_text = Steganography.decode(output_path)#decoding message
    a=int(secret_text[:1])#checking if the right person is decoding the message or not
    if a == select_friend:
        secret_text=secret_text.replace(str(a),'')
        print 'Secret text is:' + secret_text#Displaying for the user
        new_chat = chatMessage[secret_text,False]
        friends[select_friend].chats.append(new_chat)  # appending the friend chat detail
        print'Your secret message has been saved...'#Displaying for the user
    else:

        print "You are not correct person for decoding this message"#displaying it for the user



def start_chat(spy_name,spy_age,spy_rating):#user define function created
    print 'Here are your options ' +spy_name#Message given to the user
    current_status = None
    show_menu = True#by default value true for validation
    while show_menu:#using loop for multiple times show the same thing
        choice = input('What do you want to do ?\n1.Add a status\n2.Add a friend\n3.Send a message\n4.Read a message\n5.Read chats from user\n0.Exit ')#choices given to the userinput from the user
        if choice == 1:#conditional Statement
            current_status = add_status(current_status)#calling add  status function
            print'Updated status is ' + current_status#displaying for the user
        elif choice == 2:#conditional Statement
            no_of_friends = add_friend()#calling the add friend function
            print 'You have ' + str(no_of_friends) + ' friends.'#displaying for the user
        elif choice == 3:
            send_message()#calling send function for encoding
        elif choice == 4:
            read_message()#calling read function for decoding
        elif choice == 5:
            print 'this module is in progress'#working on this module
        elif choice == 0:#conditional Statement
            show_menu = False#Terminating the program
        else:#conditional Statement
            print 'Invalid option selected by you.!! '#Message for the user

spy_exist = raw_input('Are you an existing spy Y/N ')#asking the user whether he/she is an spy or not
if spy_exist.upper() == 'Y':#conditional Statement
    print 'Welcome back %s age: %d having spy rating of %d' %(spy.name,spy.age,spy.rating)#Displaying the previous data for the user
    start_chat(spy.name,spy.age,spy.rating)#Calling  a  chat function
elif spy_exist.upper() == 'N':#conditional Statement
    spy = Spy("", "", 0, 0.0)
    spy.name = raw_input('Enter Your spy Name ')#Message for the user and input from the user

    spy.rating = 0.0#Initalising the variable
    spy.age = 0#Initalising the variable
    if spy.name.isalpha():#Checking for name entered by the user as input
        spy.salutation = raw_input('What should we call you(Mr. or Ms.)')  # Message for the user and input from the user
        if len(spy.name) >= 2:#Checking the length of the name which should be greater than two
            if spy.salutation.upper() == 'MR.' or spy.salutation.upper()=='MS.':#conditional Statement
                spy_name = spy.salutation.upper() + '' + spy.name.upper()#Concatinationg  2 string
                print 'Welcome '+spy.name +' Glad to have you back with us'##Concatinationg  2 string
                print 'Alright '+spy.name+'. '+'I\'d like to know a little bit more about you ...'#Concatinationg  2 string
                spy.age=input('what is your age ')#input taken from the user
                if 50>spy.age > 12:#conditional statement
                    print 'You are eligible for being spy '+str(spy.age)#concationating th integer with the string
                    spy.rating=input('Please enter your rating ')#input from the user
                    if spy.rating > 5.0:#Conditional statement
                        print'You are Expert in Spying.You have been assigned a task'#Message given to the user
                    elif 3.5 < spy.rating <= 5.0:#Conditional statement
                        print 'You are Goood in Spying. You will be assigned a task. Soon'#Message given to the user
                    elif 2.5 < spy.rating <= 3.5:#Conditional statement
                        print 'You are not a Spy But Still You are in Queue'#Message given to the user
                    else:#Conditional statement
                        print 'Who hired You? You are fired!!!'#Message given to the user
                    spy_is_online = True#Initialising the variable
                    print 'Authentication Complete.Welcome ' +spy.name+ ' age: ' +str(spy.age)+' and rating is '+str(spy.rating) # Concatinating two integer with a string
                    start_chat(spy.name, spy.age, spy.rating)#calling a  chat function

                else:#Conditional statement
                    print 'You should grow up till now!! Common man'#Message to the user
            else:#Conditional statementn
                print 'Wrong Salutation'#Message given to the user
        else:#Conditional statement
            print 'Enter a valid name'#Message given to the user
    else:#conditional Statement
        print 'invalid name'#Messege given to the user
else:#Conditional statement
    print 'Inavalid Option'#Message given to the user