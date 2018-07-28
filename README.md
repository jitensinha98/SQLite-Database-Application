# SQLite-Database-Application

SQLite Database Application is a Database management software developed uding SQLite Database system and tkinter to develop th GUI platform of the application.

## Description

This application can be used to manage Database table.Adding , deleting , updating, reading of database table entries are just a few buttons away due to the easy GUI framework and button events . The application is solely created to manage employee database and to calculate the salary as per the wage/day system.The applictaion is also capable of storing the table in a text file for printing purposes and more.The database is stored in localhost server for simplicity purposes.

## Modules used

- tkinter
- SQLite

## Module installation Guidiline

Execute the following commands on linux terminal
```
sudo apt-get install python3-tk
```
Database under normal circumstances cannot be viewed directly by the user.In order to to view .db file , SQLite database browser is required.Execute the below command in linux terminal to install SQLite database browser.
```
sudo apt-get install sqlitebrowser
```

***SQLite is a default python module***

## Programming Languages used

- python 
- SQL

## Creating a standalone application for windows

*PyInstaller* can be used to convert .py file into a executable file.
To know more [click here](https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263)
To install PyInstaller execute the following command on linux shell
```
pip install pyinstaller
```
To convert .py to .exe execute the following command at the folder location of the script
```
pyinstaller --onefile <your_script_name>.py

```
It is not possible to create a Windows executable (.exe) by directly 
running a Pyinstaller command on a Linux Distribution and vice versa.

## Steps to use it

- The first thing to do after running the application is to create a database first.The user can then proceed to add,read,delete,update entries as per their wish.
- If PyInstaller is used then the application can be executed by just double clicking on the executed file.In case, if you are
using the python script ,run the python file in the terminal using the command ***python3 DATABASEapp_GUI.py***.

## AUTHOR
- ***Jiten Sinha***-initial work-[LinkedIn](https://www.linkedin.com/in/jiten-sinha-131043159/)

## LICESNSE
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/jitensinha98/SQLite-Database-Application/blob/master/LICENSE) file for details.
