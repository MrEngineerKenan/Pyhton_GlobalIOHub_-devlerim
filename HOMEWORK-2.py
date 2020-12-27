
First_Name=input("First name:")
Last_Name=input("Last name:")
Age=input("Age :")
Date_Of_Birth=input("Date of birth:")
Age_counter=2020-int(Date_Of_Birth) 

# I writted "2020" I know I made mistake I can take date with datetime() method 
#for example; I can write "datetime.datetime.now().year" instead of "2020"
#but at first I need to write "import datetime" 

lst=[First_Name,Last_Name,Age,Date_Of_Birth]


print("\n#########################################\n")

for i in range(0,4):
    
    print(lst[i])
    
if Age_counter > 18:
    
    print("You can go out to the street.")
    
else:
    
    print("You can't go out because it's too dangerous.")
    
    
