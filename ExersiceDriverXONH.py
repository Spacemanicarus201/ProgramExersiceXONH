from ProgramExersiceXONH import food

def createitemlist_JS():
    item_list = []
    num_items = int(input("how Many Items Will Yoju Order Today?"))
    while num_items <1:
        print("please enter a number greater than 0")
        num_items = int(input("how Many Items Will Yoju Order Today?"))
    for i in range(1, num_items + 1):
        print 