from datetime import datetime

def main():
    time = datetime.now()
    day = time.weekday()
    print(day)

    if(day == 1 or day == 5):
        print("Wrap of the day is Kentucky Mayo")
    elif(day == 2):
        print("Wrap of the day is Spicy SuperCharger Mayo")
    elif(day == 3):
        print("Wrap of the day is Somkey BBQ")
    elif(day == 4):
        print("Wrap of the day is Sweet Chili")
    else:
        print("There is none for today :(")

main()