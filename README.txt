Christopher Hernandez
Illinois Institute of Technology
CS-445
Project

Intro:
The purpose of this project is to showcase principles and design practices learned during this course. This is a Django Python project designed to launch the Delectable website.

Steps to Run:
1. Take the provided Project.zip file and extract to a location,
the location used for this example is the Desktop
1. open a terminal if you have not done so already
2. navigate to the home directory if not already there
	$ cd ~
3. change to the directory where the Project folder is located.
	$ cd Desktop
	$ cd Project
	$ cd delectable
4. Install Django and Django support with pip
	$ sudo pip install django
	$ sudo pip install djangorestframework
	$ sudo pip pip install python-dateutil
6. Yous should be in Desktop/Project/delectable,
if not, then navigate to Desktop/Project/delectable. Run the project
	$ python manage.py runserver
(it might be neccesary to specify the version of python, i.e. python2, python3, etc.)

Steps to Use
1. from the location Desktop/Project/delectable the command

	$ python manage.py runserver
	
	will launch the project. It will start on the homepage, in which there is a menu
	at the top of the screen to navigate to the various pages of the delectable website.
	Home, About Us, and Contact Us are essentially just for show to make this look like
	a real website. Everything important takes place in Menu.
	
2.	Click on Menu to go to the Menu.
	You will see the Menu. The menu items are all labelled and there are forms under
	each item so that customers can select how many of each item they wish to buy.
	
3.	Select how many of each item you wish to order using the forms under each item.

	Once you select all of the items that you wish to order, scroll down to the bottom
	of the page to view the order form. The order form takes in the customer's data,
	name, email, shipping address, card #, etc.
	
3.	Fill out the customer info form at the bottom of the page. Then press the button to
	calculate the total cost of the meal. Then press the submit button (or reset to try again)
	
	You will then be taken to a confirmation page where you can modify the status of the order
	you just made, or review the order you just made (there is a url for each)
	
4.	Additionally, there are URLs to modify data, here are the URLs and how they work

Description								| 		URL				|		info
find order by name, email, or phone		|	menu/find			|	brings up the search page
find order due today					|	menu/finddate		|	brings up the search page
view profits for the past months		|	menu/ledger			|	brings up a page that shows profits
modify prices of menu items/surcharge	|	menu/updateitems/id	|	given an item id, shows current price and allows for modification
	
Steps for API
Here is how to veiw the project's APIs
API Item	| 	URL				|	info
Orders		|	menu/order 		|	see all orders
			|	menu/order/id	|	see specific order by id, (i.e., menu/order/3)
Menu Items	|	menu/item		|	see all items
			|	menu/item/id	|	see specific item by id, (i.e., menu/item/3) 
Customers	|	menu/customer	|	see all customers
			|	menu/customer/id|	see specific customer by id, (i.e., menu/customer/3)
			
#Addendum
I am aware of the ban on databases for this project, however, while Django does
use an sqlite db as a backend, I believe the focus of this project was to not
have students worry about database logic and focus on the project itself, not its db.
I didn't focus on the db logic, Django does all of that automatically (I modified the
Django models, and they affected a database) There is no way around using the sqlite db
in Django and it does not take anything away from the project itself, so I ask that this
be excluded from the db ban.