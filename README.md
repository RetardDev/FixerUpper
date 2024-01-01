FOR WINDOW USERS:
To run this open any terminal, please note visual code terminal is also a terminal.
Make sure you are in the file directory which is ##/FixerUpper
Now we have to get into the virtual enviroment which in this case is venv 
Follow these commands:
' cd venv/Scripts '
' activate.bat '

Now you should be able to see (venv) keyword at beginning of every line of your terminal.
Go back to the file directory 
Follow these commands:
' cd .. '
' cd .. ' 

Let run our server now
Follow these commands: 
' cd fixerupper '
' py manage.py runserver '

If everthing goes smoothly you should be able to see the url for the server which is usually 127.0.0.1:8000

Important things to know, most of the data there such as images, name, price is all in database. If you want to make changes please change it from the admin portal of django 

Django Admin : 127.0.0.1:8000/admin
I have already created a user, here are the credentials: username: cryptic  password: 1234

You may have noticed the info.txt, those are credentials of the userprofile model which can also be found on the django admin.
In order to purchase anything you need to either create a user account or use the jamal credential which can be used on the site to test out.

The HSBC is a provider. 
Provider portal has not been created yet, probably will never be finished.










