
from data import intro as intro_data
from colorama import Fore


def facebook():

    return '''
                Facebook
                Type               : Surface Level
                Active Views today : 6.8 Million
                Most views Months  : 1.5 billion
                Security Ratio     : (7/10)


    '''

def google():

    return '''
                Google
                Type               : Surface Level
                Active Views today : 1.3 Billion
                Most views Months  : 40 billion
                Security Ratio     : (9/10)
    '''


def intstagram():
    return '''
                Instagram
                Type               : Surface Level
                Active Views today : 12 Million
                Most views Months  : 1 billion
                Security Ratio     : (6/10)
    '''

def pinterest():
    return '''
                Pinterest
                Type               : Surface Level
                Active Views today : 1 Million
                Most views Months  : 16 Million
                Security Ratio     : (4.3/10)


    '''    

def showitoff():

    return '''
                Showitoff
                Type               : Deep Level
                Active Views today : 1.3 Million
                Most views Months  : 20 Million
                Security Ratio     : (2/10)


    '''

def twitter():
 
    return '''
                Twitter
                Type               : Surface Level
                Active Views today : 4.9 Million
                Most views Months  : 89 Million
                Security Ratio     : (6.9/10)


    '''

def tumbler():

    return '''
                Tumblr
                Type               : Surface Level
                Active Views today : 3.8 Million
                Most views Months  : 20 Million
                Security Ratio     : (5/10)


    '''

def telegram():

    return '''
                Telegram
                Type               : Surface Level
                Active Views today : 1.1 Million
                Most views Months  : 16 Million
                Security Ratio     : (6.1/10)


    '''
    
def whatsapp():
    return '''
                WhatsApp
                Type               : Surface Level
                Active Views today : 4 Million
                Most views Months  : 1.5 billion
                Security Ratio     : (5.5/10)
    '''

def youtube():
    return '''
                Youtube
                Type               : Surface Level
                Active Views today : 3 Million
                Most views Months  : 20 Billion
                Security Ratio     : (8/10)
    '''

def xnxx():
    return '''
                XNXX
                Type               : Deep Level
                Active Views today : 15.7 Million
                Most views Months  : 78 Billion
                Security Ratio     : (3/10)
    '''






def WEB_data(get_web_name):

    data = {
        "https://facebook.com/":facebook(),
        "https://google.com/":google(),
        "https://showitoff.org/":showitoff(),
        "http://showitoff.org/":showitoff(),
        "https://twitter.com/":twitter(),
        "https://pinterest.com/":pinterest(),
        "https://tumblr.com/":tumbler(),
        "https://youtube.com/":youtube(),
        "https://www.pinterest.com/":pinterest(),
        "https://instagram.com/":intstagram(),
        "https://www.whatsapp.com/":whatsapp(),
        "https://xnxx.com/":xnxx()
        
    }



    if data.get(get_web_name) is None:
        print(f"{Fore.RED}Website Link invalid !!")
    else:
        intro_data.connecting()
        print(data.get(get_web_name))