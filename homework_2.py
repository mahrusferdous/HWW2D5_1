# Shopping list maker

def adding_item(list):
    item = input("Enter an item to add to your shopping list: ")
    list.append(item)
    return list
    
def removing_item(list):    
    print(list)
    remove_item = input("Enter the item you would like to remove: ")
    list.remove(remove_item)
    return list


def shopping():
    shopping_list = []
    print("Welcome to the shopping list.")
    
    while True:
        adding_item(shopping_list)
        choice = input("Would you like to add another item? (Press enter to continue or type 'no' to exit): ")
        if choice == "no":
            break
    
    while list:
        choice = input("Would you like to remove an item from your shopping list? (y/n): ")
        if choice == "y": 
            removing_item(shopping_list)
        else:
            break
    
    print("Here is your shopping list: ")
    for item in shopping_list:
         print(item)
        
shopping()
        
