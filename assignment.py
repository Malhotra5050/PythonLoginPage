try:
    import mysql.connector as mydb
    mycon = mydb.connect(user='bhavesh', password='bhavesh12345',
                              host='127.0.0.1',database='JALANDHAR')
    mycursor=mycon.cursor()
    print("success")
except:
    print("error occured...")
finally:
    print("goodbye")
    mycon.close()
    print("byee")



