import mysql.connector
import datetime
import smtplib
import random
my_db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="12345",
      database="rk_ATM"
)

mycursor=my_db.cursor()

def user_data():
     sql="insert into rk_table (customer_name,pin_no,balance_amount) values (%s,%s,%s)"
     x=datetime.datetime.now()
     print(x,x.strftime("%p"))
     
     customer_name=input("enter your name :")
     emailid=input("enter customer mail id :")
     pin_no=1234
     balance_amount=5000
     user_pin=int(input("Enter your  pin number :"))
     if user_pin == pin_no:
        print("1.Deposite\n2.Withdrwal\n3.BalanceEnquiry")
        ch=int(input("Choice your number :"))
        if ch==1:
         damount=int(input("Enter the deposite amount"))
         print("********transaction_status=success*******")
         balance_amount=balance_amount+damount
         print("your available balance",balance_amount)
         
         try:
          
         
         # creates SMTP session
          s = smtplib.SMTP('smtp.gmail.com', 587)
 
         # start TLS for security
          s.starttls()
 
         # Authentication
          s.login("ayyanar.2481996@gmail.com", "lipfcigwfeilcurw")
 
         # message to be sent
          message = f"hi {customer_name} your Rs.{damount} debited transaction is  successfull!!....."
 
         # sending the mail
          s.sendmail("ayyanar.2481996@gmail.com", emailid, message)

 
         # terminating the session
          s.quit()
          print("******mail send successfully*******")

         except:
          print("********sorry mail not send*****")

         
        elif ch==2:
         wamount=int(input("Enter the withdrawl amount"))
         print("transaction_status=success")
         balance_amount=balance_amount-wamount
         print("your available balance",balance_amount)
         try:
          
         
         # creates SMTP session
          s = smtplib.SMTP('smtp.gmail.com', 587)
 
         # start TLS for security
          s.starttls()
 
         # Authentication
          s.login("ayyanar.2481996@gmail.com", "lipfcigwfeilcurw")
 
         # message to be sent
          message = f"hi {customer_name} your Rs.{damount} cridet transaction is  successfull!!....."
 
         # sending the mail
          s.sendmail("ayyanar.2481996@gmail.com", emailid, message)

 
         # terminating the session
          s.quit()
          print("******mail send successfully*******")

         except:
          print("********sorry mail not send*****")

        elif ch==3:
         print("Your available balance",balance_amount)
        else:
         print("wrong input")
     else:
        print("invalid pin number")
     val=(customer_name,pin_no,balance_amount)

     mycursor.execute(sql,val)
     my_db.commit()
     



def admain_view():
    #view data
      mycursor.execute("select * from  rk_table ")
      myresult=mycursor.fetchall()
      for i in myresult:
        print(i)


def update_data():
    #update data
      sql="update  rk_table set vaccien_1='Yes' where vaccien_1='no'"
      mycursor.execute(sql)
      my_db.commit()
      print("data updated successfully!..........")
      

def delete_data():
    #delete data
      column_name=input("which column you want to delete: ")
      delete_data=input(f"which data you want to delete in {column_name} column:")
      sql=f"DELETE FROM  rk_table WHERE {column_name}= %s"
      mycursor.execute(sql,(delete_data,))
      my_db.commit()
      print("Data deleted successfully")    




def main1():
  print("--------->rk ATM<------------")
  print("TAMIL NADU -BANK OF INDIA  ")
  
  print("1->user data")
  print("2->admain view")
  print("3->update data")
  print("4->delete data")

  user=int(input("Enter your number: "))
  if user==1:
        user_data()
  elif user==2:
        admain_view()
  elif user==3:
       update_data()
  elif user==4:
       delete_data()
       
main1()





