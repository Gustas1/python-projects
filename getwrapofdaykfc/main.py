from datetime import datetime

def main():
    time = datetime.now()
    day = time.weekday()
    print(day)
    wrap = ["Kentucky Mayo", "Spicy SuperCharger Mayo", "Somkey BBQ", "Sweet Chili", "Kentucky Mayo", "None", "None"]
    print("The wrap of the day is " + wrap[day])
   
main()