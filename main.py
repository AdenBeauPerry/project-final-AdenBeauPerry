import playbook

my_playbook = playbook.play_structure()
data_set = []
name_sets = [["Doubles Right 24 Read", "Trips Left 23", "Doubles Left 25 Bash"],
             ["Trips Right 322 Y Cross", "Doubles Left 93 H", "Trips Right 60 Smash/Colorado"]]

for i in range(1, 5):
    for j in range(1, 4):
        for k in range(1, 3):
            data_set.append(my_playbook.find_playset(i, j, k))

for i in range(len(name_sets)):
    for j in range(len(name_sets[i])):
        my_playbook.add_play(data_set[i], name_sets[i][j])

print("You are a coach for the NFL. This tool will help you select your next play call.")
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