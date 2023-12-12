import playbook

my_playbook = playbook.play_structure()
data_set = []
name_sets = [["Doubles Right 24 Read", "Trips Left 23", "Doubles Left 25 Bash"],
             ["Trips Right 322 Y Cross", "Doubles Left 93 H", "Trips Right 60 Smash/Colorado"],
             ["Bunch Right 25 Z Jet", "Trips Right Y Zoom 25 Y Jet", "Trips Left Y Zoom 22"],
             ["Trips Left H Scoot 60 Rocket", "Bunch Left 323 Y Cross", "Doubles Right 60 Spout"],
             ["Doubles Left 22 Reaper", "Trips Left 25 Bash", "Bunch Right 23"],
             ["Doubles Right 390 Z", "Doubles Right 97 Y", "Bunch Left 50 Mesh"],
             ["Trips Left 24 Bash", "Trips Right H Scoot 24", "Doubles Left 24"],
             ["Doubles Left 23 Reaper H Pop", "Trips Left 393 H", "Doubles Right Y Zoom 322 Y Cross"],
             ["Bunch left 24 Y Jet", "Doubles Right 24 Bash", "Bunch Left 25 Z Jet"],
             ["Bunch Right 50 Gopher R Snake", "Doubles Left 94 R", "Doubles Left 60 Hitches"],
             ["Doubles Right H Scoot 24", "Doubles Left 22", "Trips Right 23"],
             ["Trips Left 50 Spout", "Doubles Right 60 Smash", "Doubles Right H Zap 91 X"]]

for i in range(1, 5):
    for j in range(1, 4):
        for k in range(1, 3):
            data_set.append(my_playbook.find_playset(i, j, k))

for i in range(len(name_sets)):
    for j in range(len(name_sets[i])):
        my_playbook.add_play(data_set[i], name_sets[i][j])

print("\nYou are a coach for the NFL. This tool will help you select your next play call.")

run = True
while run == True:

    print("Please enter what down it is:\n(1) First Down \n(2) Second Down \n(3) Third Down \n(4) Fourth Down")
    my_down = int(input())

    print("Please enter the distance needed for a first down.")
    print("(1) Short Yardage \n(2) Medium Yardage \n(3) Long Yardage")
    my_dst = int(input())

    print("Please enter whether you want to Run or Pass.")
    print("(1) Run Play \n(2) Pass Play")
    my_type = int(input())

    suggested_plays = my_playbook.find_playset(my_down, my_dst, my_type)
    print("\nHere are the suggested plays based on your inputs:")
    for i in range(len(suggested_plays)):
        print(str(i+1) + ". " + suggested_plays[i].playName)

    print("\nWould you like to try another situation? (Y/N)")
    cont = str(input()).upper()
    if cont == "N":
        run = False