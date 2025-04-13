import time
hour=int(time.strftime("%H"))
minute=time.strftime("%M")
sec=time.strftime("%S")

if(hour>0 and hour<5):
    print("Early Morning")
    print(f"The time is {hour}:{minute}:{sec}")
elif(hour>=5 and hour<12):
    print("Morning")
    print(f"The time is {hour}:{minute}:{sec}")
elif(hour>=12 and hour<16):
    print("Afternoon")
    print(f"The time is {hour}:{minute}:{sec}")
elif(hour>=16 and hour<19):
    print("Evening")
    print(f"The time is {hour}:{minute}:{sec}")
elif(hour>19 and hour<=24):
    print("Night")
    print(f"The time is {hour}:{minute}:{sec}")
print("Thank you")
