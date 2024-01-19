#To-Do List 2
#1/10/24
#Sofia Richter

#initialize
groceryList = ["milk","eggs","bread","apples","chocolate","spinach","butter"]

#functions 
def menu():
    #Code that runs each task goes here
    print("Please choose an option: (Type in a number between 1-8)")
    print("""1. Add a task to the to-do list \n2. View the current to-do list \n3. Mark a task as completed \n4. Remove a task from the to-do list 
          \n5. Exit the program \n6. Remove all tasks from the to-do list \n7. Sort the list alphabetically \n8. Print the # of items on the list""")
    option = int(input("Option: "))
    if option == 5:
        #exits program
        quit()
    if option == 1:
        #adds a task
        task = input("What task would you like to add? ")
        groceryList.insert(7, task)
        print(groceryList)
    elif option == 2:
        #view the current t-do list
        print(groceryList)
    elif option == 3:
        #marks a task as complete
        complete = input("What task did you complete? ")
        i = groceryList.index(complete) 
        groceryList[i] = complete + " [X]"
        print(groceryList)
    elif option == 4:
        #removes a task from the to do list
        remove = input("What task would you like to remove? ")
        groceryList.remove(remove)
        print(groceryList)
    elif option == 6:
        #remove all tasks from the to do list
        groceryList.clear()
        print(groceryList)
    elif option == 7:
        #sort the list alphabetically
        groceryList.sort()
        print(groceryList)
    elif option == 8:
        #print the # of items on the list
        print("The number of items on the list is: " + str(len(groceryList)))

menu()