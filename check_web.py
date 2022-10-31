
'''
This scripts is made to check the website information

'''
from data import web_data as web 
from data import intro as intro_data





def get_web_data():
    intro_data.Intro()
    get_website = input("Type your desire webstie Name : ")
    web.WEB_data(get_website)

get_web_data()

