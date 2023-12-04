from ProgramExersiceXONH import FoodItemJS  # Importing the correct class name

def create_item_list_JS():
    item_list = []
    num_items = int(input("How many items will you order today? "))
    
    while num_items < 1:
        print("Please enter a number greater than 0.")
        num_items = int(input("How many items will you order today? "))
    
    for i in range(1, num_items + 1):
        print(f"Item #{i}-")
        food_name = input("Enter food: ")
        amount = float(input("Enter amount of pounds: "))
        
        while amount <= 0:
            print("Amount of pounds must be greater than 0.")
            amount = float(input("Enter amount of pounds: "))
        
        item = FoodItemJS(food_name, amount)
        item_list.append(item)

    return item_list

def display_items_JS(item_list):
    for item in item_list:
        print(item)
        print()

def calculate_total_cost_JS(item_list):
    total_cost = sum(item.calculatecost_JS() for item in item_list)
    return total_cost

def main_JS():
    items = create_item_list_JS()
    print("\nHere's a summary of the items purchased:")
    display_items_JS(items)
    total_cost = calculate_total_cost_JS(items)
    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main_JS()
