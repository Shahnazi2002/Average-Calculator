print("With the help of this program you can easily calculate the average of several numbers.")
list = []
print("At first you need to create a list of numbers.")
list.append(int(input("Enter the first element of the list: ")))
print("The first element has been added to your list.")
repeat = True
while repeat:
    new_element = input("Enter another number or just press the ENTER KEY to complete creating the list: ")
    if new_element != "":
        list.append(int(new_element))
        print("The entered number has been added to your list.")
    else:
        repeat = False
        print("End of list creation.")
print("Your list is as follows:", list)
print("Length of list =", len(list))
average = sum(list)/len(list)
print("Average =", average)
