import sqlite3

#creating a Database named BASIC and connection with localhost server
conn=sqlite3.connect('BASIC.db')

#creating cursor to execute SQL commands
c=conn.cursor()

#creating table in the database
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS basics(Name TEXT,Salary TEXT)')

#function used to add entries in the database table
def data_entry():
	name=str(input("Enter name : "));
	salary=str(input("Enter salary : "));
	c.execute("INSERT INTO basics(Name,Salary) VALUES(?,?)",(name,salary))
	conn.commit()
	print (" ")

#dynamic entry to the table	
def dynamic_data_entry():
	x=int(input("How many rows do you want to enter ? "))
	for i in range (0,x):
		data_entry()

#reading entries from the database table
def read_from_db():
	print("Press 1 to view the entire database.")
	print("Press 2 to view database by name.")
	print(" ")
	choice=int(input(">>>"));
	if choice==2:
		name_db=input("Enter Name of the person to acquire details : ")
		c.execute("SELECT * FROM basics WHERE Name=?",(name_db,))
	elif choice==1 :
		c.execute("SELECT * FROM basics")
	else:
		print("INVALID ENTRY")
		print(" ")
	print(" ")
	print("(NAME   |  SALARY)")
	print(" ")
	print("-----------------")
	for row in c.fetchall():
		print (row)
	print(" ")

#updating database table entries
def update_db():
	print("Please enter the name whose information you want to update : ")
	name_query=str(input(">>"))
	print(" ")
	print("Press 1 to update Name.")
	print("Press 2 to update Salary.")
	print("Press 3 to update Both.")
	ch=int(input(">>>"))
	if ch==1 :
		name_dba=str(input("Enter new Name : "))
		c.execute('UPDATE basics SET Name=? WHERE Name=?',(name_dba,name_query))
	elif ch==2 :
		salary_dba=str(input("Enter new Salary : "))
		c.execute('UPDATE basics SET Salary=? WHERE Name=?',(salary_dba,name_query))
	elif ch==3 :
		name_dba=str(input("Enter new Name : "))
		salary_dba=str(input("Enter new Salary : "))
		c.execute('UPDATE basics SET Name=? ,Salary=? WHERE Name=?',(name_dba,salary_dba,name_query))
	else:
		print("INVALID ENTRY")
		print(" ")
	conn.commit()
	print(" ")
	print("DATABASE SUCCESSFULLY UPDATED")
	print(" ")

#deleting table or table entries from the database
def delete_db():
	print(" ")
	print("Press 1 to empty the entire database.")
	print("Press 2 to delete an invidual from database.")
	choice_del=int(input(">>>"))
	if choice_del ==1:
		c.execute('DELETE FROM basics');
	elif choice_del==2 :
		name_del=str(input("Enter Name : "))
		c.execute('DELETE FROM basics WHERE Name=?',(name_del,))
	else:
		print("INVALID ENTRY")
		print(" ")
	conn.commit()
	
while True:
	print("""WELCOME TO DATABSE MANAGEMENT SYSTEM
	
Press 1 to add entries.
Press 2 to read entries.
Press 3 to update entries.
Press 4 to delete entries.
Press 5 to create table.
Press 5 to Exit Control.
	
     	      """)
	ch=int(input(">>>"))
	if ch==1 :
		dynamic_data_entry()
	elif ch==2:
		read_from_db()
	elif ch==3:
		update_db()
	elif ch==4:
		delete_db()
	elif ch==5:
		create_table()
	elif ch==6:
		break
	else :
		print("INVALID ENTRY")

	print(" ")

#closing cursor 
c.close()

#declining connection to the localhost
conn.close()


