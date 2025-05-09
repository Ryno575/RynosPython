import turtle as trtl

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
accidentals = ['B', 'E', 'A', 'D', 'G', 'C', 'F']
sharp_or_flat = ""
sharp = False
flat = False

# Creates the scale setup
scale_maker = trtl.Turtle(); scale_maker.speed(0); scale_maker.ht(); scale_maker.pu()
y = 200
scale_maker.goto(-300, y)
for i in range(12):
    if (i % 6 == 0):
        y -= 40
        scale_maker.goto(-300, y)
        continue
    scale_maker.pd()
    scale_maker.forward(600)
    y -= 40
    scale_maker.pu()
    scale_maker.goto(-300, y)

### Draws the trebble cleff
scale_maker.pensize(5)
scale_maker.goto(-300, 0)
scale_maker.setheading(-90)
scale_maker.pd()
scale_maker.circle(25, 180); scale_maker.forward(135)
scale_maker.circle(-25, 220); scale_maker.forward(100)
scale_maker.circle(25, 270); scale_maker.circle(15, 180)


### Draws the bass cleff
scale_maker.pu()
scale_maker.goto(-275, 210 - 8*40)
scale_maker.pd()
scale_maker.dot(20)
scale_maker.goto(-280, 210 - 8*40)
scale_maker.setheading(90); scale_maker.circle(-30, 210); scale_maker.forward(100)
scale_maker.pu()
scale_maker.goto(-200, 210 - 8*40); scale_maker.dot(5)
scale_maker.goto(-200, 190 - 8*40); scale_maker.dot(5)
### Gets the starting note off of the amount of accidentals, as well as the type of accidental, the user gives (1 - 6, Sharp/Flat)
def get_start_note(num_accidentals, accidental):
    if accidental == "flats":
        num_accidentals = (num_accidentals * 3) % 7
    elif accidental == "sharps":
        num_accidentals = ((num_accidentals * 3) % 7) * -1
    return notes[num_accidentals]

### Gets the accidentals for the scale based off the number of accidentals and the type (1 - 6, Sharp/Flat)
def get_accidental(num_accidentals, accidental):
    current_accidentals = []
    if accidental == "flats":
        for i in range(num_accidentals):
            current_accidentals.append(accidentals[i] + 'b')
    else:
        for i in range(-1, -num_accidentals - 1, -1):
            current_accidentals.append(accidentals[i] + "#")
    return current_accidentals


### Gets the scale based off the number of accidentals and the starting note
def get_scale(start_note, num_accidentals, accidental):
        scale = []
        current_accidentals = []
        current_accidentals = get_accidental(num_accidentals, accidental)
        if accidental == "flats":
            for i in range(8):
                scale.append(notes[((num_accidentals * 3) + i) % 7])
            
            ### Imserts the flats into the scale
            for i in range(8):
                for j in range(len(current_accidentals)):
                    curr_note = scale[i]
                    if ((curr_note + 'b') == current_accidentals[j]):
                        scale[i] = current_accidentals[j]
        else:
            for i in range(8):
                scale.append(notes[(((num_accidentals * -3) + i) % 7)])
            
            ### Inserts the sharps into the scale
            for i in range(8):
                for j in range(len(current_accidentals)):
                    curr_note = scale[i]
                    if ((curr_note + '#') == current_accidentals[j]):
                        scale[i] = current_accidentals[j]
        return scale

def scale_name(start_note, scale):
    return (str(start_note) + " Major Scale: " + str(scale))

def write_scale(start_note, scale):
    x = -300
    scale_writer.pu()
    scale_writer.goto(x, -275)
    scale_writer.write((str(start_note) + " Major Scale: "), font=("Arial", 20))
    x += 200
    for curr_index in range(len(scale)):
        scale_writer.goto(x, -275)
        scale_writer.write((scale[curr_index] + ","), font=("Arial", 20))
        x += 50



# Gets the number of accidentals and if it is either sharp or flat from the user's entered note
def letter_to_scale(letter):
    global sharp_or_flat
    global num_accidentals
    if letter == "Ab" or letter == "G#":
        sharp_or_flat = "flats"
        num_accidentals = 4
    elif letter == "A":
        sharp_or_flat = "sharps"
        num_accidentals = 3
    elif letter == "Bb" or letter == "A#":
        sharp_or_flat = "flats"
        num_accidentals = 2
    elif letter == "B":
        sharp_or_flat = "sharps"
        num_accidentals = 5
    elif letter == "C":
        sharp_or_flat = '0'
        num_accidentals = 0
    elif letter == "Db":
        sharp_or_flat = "flats"
        num_accidentals = 5
    elif letter == "D":
        sharp_or_flat = "sharps"
        num_accidentals = 2
    elif letter == "Eb" or letter == "D#":
        sharp_or_flat = "flats"
        num_accidentals = 3
    elif letter == "E":
        sharp_or_flat = "sharps"
        num_accidentals = 4
    elif letter == "F" or letter == "E#":
        sharp_or_flat = "flats"
        num_accidentals = 1
    elif letter == "F#":
        sharp_or_flat = "sharps"
        num_accidentals = 6
    elif letter == "Gb":
        sharp_or_flat = "flats"
        num_accidentals = 6
    elif letter == "G":
        sharp_or_flat = "sharps"
        num_accidentals = 1
    else:
        num_accidentals = -1

print("Hello welcome to the Music Helper! This tool will give you a specific scale based on ")
while True:
    choice = input("Enter 'NOTE' if you have the starting note [C Major Scale] or enter 'ACCIDENTAL' if you have the number/type of accidentals [flats, 3]: ")
    print("")
    if choice.lower() == "note" or choice.lower() == "accidental":
        break

if choice.lower() == "accidental":
    ### This asks the user if they want to get a scale that has flats, sharps, or none
    while True:
        sharp_or_flat = input(str("Enter either 'b' for flat or '#' for sharp or '0' for no flats/sharps: "))
        print("")
        if (sharp_or_flat == 'b'):
            sharp_or_flat = "flats"
            num_accidentals = -1
            break
        elif (sharp_or_flat == '#'):
            sharp_or_flat = "sharps"
            num_accidentals = -1
            break
        elif (sharp_or_flat == '0'):
            break
        else:
            print("Please enter 'b', '#', or '0'.")

if choice.lower() == "note":
    # Asks the user what note the scale starts with and returns the sharps/flats and num of accidentals
    while True:
        num_accidentals = -1
        note = input("Please enter the starting note: ")
        print("")
        letter_to_scale(note)
        if num_accidentals == -1:
            continue
        else:
            break

### Asks the user how many sharps or flats are in the scale
if sharp_or_flat == '0':
    num_accidentals = 0
    starting_note = get_start_note(num_accidentals, 0)
### If the user chooses accidental it will go through the elif path
elif num_accidentals > 0:
        starting_note = get_start_note(num_accidentals, sharp_or_flat)
### If the user chooses notes it will go through the else path
else:
    while True:
        print()
        try:
            num_accidentals = int(input("How many " + str(sharp_or_flat) + " do you want? (pick a number 1 - 6): "))
            if (num_accidentals > 0 and num_accidentals < 7):
                starting_note = get_start_note(num_accidentals, sharp_or_flat)
                break
            else:
                print("Please enter a number 1 - 6")
        except:
            print("Please enter a number 1 - 6")

### Prints the scale that the user is looking for
scale = get_scale(starting_note, num_accidentals, sharp_or_flat)
start_note = scale[0]
print(scale_name(start_note, scale))

### Gets the first note WITHOUT the accidental
starting_note = start_note[0]
index = 0
notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for note in range(len(notes)):
    curr_note = notes[index]
    if starting_note == curr_note:
        break
    else:
        index += 1

notes = scale
### Intializes the turtle that will draw the notes on the scale
scale_writer = trtl.Turtle()
scale_writer.speed(0)
x = -175
y = -237 + (20 * index)

### DRAWS THE SCALE
for note_index in range(15):
    scale_writer.pu()
    scale_writer.goto(x, y)
    scale_writer.pd()
    curr_note = notes[note_index % 7]

    try:
        ## Highlights the note that starts, is in the middle and ends the scale
        if (note_index % 7 == 0):
            scale_writer.pencolor("red")
            for local_index in range(2):
                scale_writer.pensize(3.5)
                scale_writer.circle(15, 90)
                scale_writer.pensize(2)
                scale_writer.circle(20, 90)
                ## Writes the starting note off to the side
                if (local_index < 1):
                    scale_writer.pu()
                    scale_writer.forward(40)
                    scale_writer.write(start_note, font=("Arial", 20))
                    scale_writer.back(40)
                    scale_writer.pd()
        ## Adds a # to a note if it includes a sharp
        elif (curr_note[1] == '#'):
            for local_index in range(2):
                scale_writer.pensize(3.5)
                scale_writer.circle(15, 90)
                scale_writer.pensize(2)
                scale_writer.circle(20, 90)
                if (local_index < 1):
                    scale_writer.pu()
                    scale_writer.forward(40)
                    scale_writer.left(90), scale_writer.forward(20)
                    scale_writer.write("#", font=("Arial", 20))
                    scale_writer.back(20), scale_writer.left(-90)
                    scale_writer.back(40)
                    scale_writer.pd()
        ## Adds a b to a note if it includes a flat
        else:
            for local_index in range(2):
                scale_writer.pensize(3.5)
                scale_writer.circle(15, 90)
                scale_writer.pensize(2)
                scale_writer.circle(20, 90)
                ## Writes the starting note off to the side
                if (local_index < 1):
                    scale_writer.pu()
                    scale_writer.forward(40)
                    scale_writer.left(90), scale_writer.forward(20)
                    scale_writer.write("b", font=("Arial", 30))
                    scale_writer.back(20), scale_writer.left(-90)
                    scale_writer.back(40)
                    scale_writer.pd()
    ## Enters this stage if it does not have a flat or a sharp
    except:
        for i in range(2):
            scale_writer.pensize(3.5)
            scale_writer.circle(15, 90)
            scale_writer.pensize(2)
            scale_writer.circle(20, 90)
    ## Draws the middle C line
    if (scale_writer.ycor() < -55 and scale_writer.ycor() > -60):
            scale_writer.pensize(3.5)
            scale_writer.circle(15, 90)
            scale_writer.setheading(0), scale_writer.pensize(1.5)
            scale_writer.forward(30), scale_writer.backward(80), scale_writer.forward(50)
            scale_writer.setheading(90)
            scale_writer.pensize(3.5)
            scale_writer.circle(15, -90)
    scale_writer.pencolor("black")
    x += 33
    y += 20
### Writes out the scale at the bottom of the 
write_scale(start_note, scale)

wn = trtl.Screen()
wn.mainloop()
