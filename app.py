print("welcome to my python program!")
#add project folder and install app.py with welcome message

hours = input("how many hours did you work today?")
#add user input prompt for hours worked

try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number for hours worked.")  
    exit()
#add error handling for non-numeric input

hours = float(hours)
weekly_hours = hours * 5
#add calculation for weekly hours based on daily input

print(f"you are on track to work {weekly_hours} hours this week!")
#show user their projected weekly hours worked 