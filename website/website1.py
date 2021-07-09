from .models import Data
from . import db

 

def block():
    
    web_sites_list = ["www.facebook.com", "facebook.com","www.google.com","www.youtube.com"]
    my_website = db.session.query(Data).all()
    for websites in my_website:
        
        website101 = websites.website
        web_sites_list.append(website101)
        break

    print(web_sites_list)
    import time
    from datetime import datetime as dt
    hosts_path = r"/etc/hosts"   # r is for raw string
    hosts_temp = "hosts"
    redirect = "127.0.0.1"
        # users can modify the list of the websites they want to block

    while True:
        if True:
            print("Working hours")
            with open(hosts_path, "r+") as file:
                content = file.read()
                for website in web_sites_list:
                    if website in content:
                        pass
                    else:
                        file.write(redirect+" "+website+"\n")
                        
        else:
            print("Fun time")
            with open(hosts_path, "r+") as file:
                content = file.readlines()
                file.seek(0)  # reset the pointer to the top of the text file
                for line in content:
                    # here comes the tricky line, basically we overwrite the whole file
                    if not any(website in line for website in web_sites_list):
                        file.write(line)
                    # do nothing otherwise
                file.truncate() # this line is used to delete the trailing lines (that contain DNS)
        time.sleep(5)

        return True