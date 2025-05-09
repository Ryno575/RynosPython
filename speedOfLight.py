#How long ago was that light?

speed_of_light = 299792.458 # kilometers / second

planets = {
    "mercury": 58000000,
    "venus": 108208930,
    "earth": 149597871,
    "mars": 227000000,
    "jupiter": 764270000,
    "saturn": 1436100000,
    "uranus": 2921800000,
    "neptune": 4471100000,
    "pluto": 5900000000,
}

def balanced_time(time):
    time_string = []
    if time > 31536000:                                  # Num of Years
        years = int(time / 31536000)
        time_string.append("Years: " + str(years))
    if time > 86400:                                     # Num of Days
        days = int((time % 31536000)/ 86400)
        time_string.append("Days: " + str(days))     
    if time > 3600:                                      # Num of Hours
        hours = int((time % 86400) / 3600)
        time_string.append("Hours: " + str(hours))
    if time > 60:                                        # Num of Minutes
        minutes = int((time % 3600) / 60)
        time_string.append("Minutes: " + str(minutes))
    time_string.append(f"Seconds:  {time % 60:.2f}")     # Num of Seconds
    return str(time_string)

def calculate_time(distance, speed_of_light=speed_of_light):
    time = distance / speed_of_light
    time = balanced_time(time)
    return time                                          # Prints in this format: (Years: #, Days: #, Hours: #, Minutes: #, Seconds: ##.##) 

choice = (input("How far away are you from the light source? Enter a planet name or distance in kilometers: "))
if choice.lower() in planets:
    for planet, value in planets.items():
        if planet == choice.lower():
            distance = value
else:
    try:
        distance = float(choice)
    except:
        print("This choice is not allowed")

print(f"It would take {calculate_time(distance, speed_of_light)} to reach {distance}km")
