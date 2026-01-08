from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




#signin
#Login(Once log in create JWT token and use that for validation everywhere after login and expire it exceeded timelimit or logout)
    #if admin
        #should be redirected to view people list and product list api endpoint and add product and remove product from the store
    #elif user
        #should have his own cart where he can add product and should be a redirect to the cart after the entire code 
#Update(PUT)
#delete


#product list
#people registed list
#cart
#In cart there should be checkout to calculate the total prise and buy the complete product


