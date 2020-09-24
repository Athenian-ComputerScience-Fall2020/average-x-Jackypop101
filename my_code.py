# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#

def avg(user_list):
    average = sum(user_list) / len(user_list)
    return average

if __name__ == '__main__':
    x = int(input("Please enter a number:"))
    y = int(input("Please enter another number:"))
    z = int(input("Please enter another number:"))
    q = int(input("Please enter another number:"))
    print(avg([x, y, z, q]))

    # test your fucntion with this print statement before writing the input loop
    # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    user_list = [] # start with an empty list
    # Write a loop to allow the user to input the values to be averaged
