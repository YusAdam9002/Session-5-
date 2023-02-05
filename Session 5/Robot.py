robot_name = "Robot" 
robot_age = 1
Battery_percentage = 100
Robot_on = True

if Robot_on == True:
    print("hello i am",robot_name , "// i am" ,robot_age, "years old", " // my battery is ",Battery_percentage, " %", "// powered on?", Robot_on)
    print( " 0 for command list")

while Robot_on == True:

    if Battery_percentage <=10:
        print( " My Battery is low" )

    if Battery_percentage <= 0:
        print(" See You Soon! ")
        Robot_on == False
        quit()

    Command_List = ["Print : 0","Talk : 1","Charge : 2","Walk : 3 "," Self destuct: 4" ]

    Num = (int(input("number")))

    if Num == 0 :
        print(Command_List)
    if Num == 1 :

        print ("hello i am robot, how is your day??")
        print ( " if you are good press 1    if not press 2")

        Battery = Battery_percentage - 10
        Num = (int(input("number")))

        if Num == 1 :

            print ( "Nice!" )
            Battery = Battery - 10
            print(Command_List)


        if Num == 2 :

            print ( "That Sucks " )
            Battery = Battery - 10
            print(Command_List)

    if Num == 2 and Battery <= 101:
        print ( " I need Charging " )

        Battery = Battery + 20
        if Battery >= 10 and Battery < 20:
            print("**                  ")
        if Battery >= 20 and Battery < 30:
            print("****                ")
        if Battery >= 30 and Battery < 40:
            print("******              ")
        if Battery >= 40 and Battery < 50:
            print("********            ")
        if Battery >= 50 and Battery < 60:
            print("**********          ")
        if Battery >= 60 and Battery < 70:
            print("************        ")
        if Battery >= 70 and Battery < 80:
            print("**************      ")
        if Battery >= 80 and Battery < 90:
            print("****************    ")
        if Battery >= 90 and Battery < 100:
            print("******************    ")
        if Battery >= 100 and Battery < 110:
            print("********************:")
            print(Command_List)

    if Num == 2 and Battery >=100:
        print ( "I am full already " )
        if Battery >= 100 and Battery < 110:
            print("********************:")
            print(Command_List)
    if Num == 3 :
        print(robot_name, "moved a step forward")

    if Num == 4:
        print("Self destruct Countdown Beginning now") 
        if Num == 4 :

            print ("Are u Sure?")
            print ( " Press 1 for Yes   Press 2 for No")

            Battery = Battery_percentage - 10
            Num = (int(input("number")))

            if Num == 1 :

                print ( robot_name, " self distructing now, Bye!" )
                quit()

            if Num == 2 :

                print ( "You Saved me! Hurrah " )
                Battery = Battery - 10
                print(Command_List)

