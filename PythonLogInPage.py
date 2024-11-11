import mysql.connector as mydb

cnx = mydb.connect(user='root', password='123456', host='127.0.0.1', database='Assignment')

mycursor = cnx.cursor()

print("1=Sign Up")
print("2=Sign In")
print("3=Change Password")
print("4=Forget Password")

a = int(input("CHOOSE ONE OF THEM: "))

if a == 1:
    # Sign Up
    print("Sign Up")
    username = input("Enter username:\n")

    # Check if user already exists
    mycursor.execute("SELECT * FROM MyUser WHERE username = %s", (username,))
    existing_user = mycursor.fetchone()

    if existing_user:
        print("User already exists.")
    else:
        password = input("Enter password:\n")
        HintQ = input("Enter Hint Question:\n")
        HintPass = input("Enter Hint Password:\n")

        insert_query = ("INSERT INTO MyUser (username, password, HintQ, HintPass) VALUES (%s, %s, %s, %s)")
        data = (username, password, HintQ, HintPass)

        try:
            mycursor.execute(insert_query, data)
            print("Data saved")
        except Exception as e:
            print("Error:", e)
elif a == 2:
    print("Sign In")
    username = input("Enter username:\n")

       # Check if user already exists
    mycursor.execute("SELECT * FROM MyUser WHERE username = %s", (username,))
    existing_user2 = mycursor.fetchone()
    
    if existing_user2:
        #print("User already exists.")
        password = input("Enter password:\n")
        
        mycursor.execute("SELECT * FROM MyUser WHERE password = %s", (password,))
        existing_user3 = mycursor.fetchone()
        
        if existing_user3:
          print("Login successful")
        else:
          print("INCORRECT PASSWORD")
            
    else:
        print("NOT FOUND")
    
    

elif a == 3:
    # Change Password
    print("Change Password")
    username = input("Enter username:\n")
    password= input("Enter your old password:\n")
    # Check if user exists
    mycursor.execute("SELECT * FROM MyUser WHERE username = %s AND password = %s", (username,password,))
    existing_user4 = mycursor.fetchone()
    

    if existing_user4:
        new_password = input("Enter new password:\n")
        update_query = ("UPDATE MyUser SET password = %s WHERE username = %s")
        data = (new_password, username)
        try:
            mycursor.execute(update_query, data)
            cnx.commit()
            print("Password changed successfully")
        except Exception as e:
            print("Error:", e)
    else:
        print("INVAID DETAILS.")

elif a == 4:
      # Change Password
    print("FORGET PASSWORD")
    username = input("Enter username:\n")
    HintQ = input("Enter Hint Question:\n")
    HintPass = input("Enter Hint Password:\n")


    # Check if user exists
    mycursor.execute("SELECT * FROM MyUser WHERE username = %s AND HintQ = %s AND HintPass = %s", (username, HintQ, HintPass))
    existing_user4 = mycursor.fetchone()
    

    if existing_user4:
        new_password = input("Enter new password:\n")
        update_query = "UPDATE MyUser SET password = %s WHERE username = %s"
        data = (new_password, username)
        try:
            mycursor.execute(update_query, data)
            cnx.commit()
            print("Password changed successfully")
        except Exception as e:
            print("Error:", e)
    else:
        print("INVAID DETAILS.")


else:
    print("Invalid choice")


mycursor.close()
cnx.close()
