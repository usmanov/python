# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
''' version 1 '''
# row = int(position) % 10 # row = 3
# column = int(int(position) / 10) # column = 2
# if row == 1:
#     row1[column-1] = 'X '
# if row == 2:
#     row2[column-1] = 'X '
# if row == 3:
#     row3[column-1] = 'X '

''' version 2 '''
# row = int(position[1])
# column = int(position[0])
# map[row-1][column-1] = 'X '

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}") 