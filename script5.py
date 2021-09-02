import datetime


filename = datetime.datetime.now()

#Create empty file
def create_file():
    """Somethong writble"""
    
    with open(filename.strftime("%Y-%m-%d-%H-%M")+"txt","w") as file:
        file.write("")
        
create_file()