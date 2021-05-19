import hashtable

tableMade = False

print("\nType 'help' for commands\n")

tableSize = int(input("Table size (int > 0): "))

table = hashtable.HashTable(tableSize)
print("\n")

while True:
    _input = input("Example > ")
    if _input.lower() == 'help':
        print("\n")
        print("add [string]          - adds data to the table")
        print("exit                  - exits example")
        print("remove_data [string]  - remove data by data")
        print("remove_position [int] - removes data by position")
        print("find [string]         - finds the position of data")
        print("in_table [string]     - returns true if data input is in the table")
        print("show_table            - shows the table")
        print("\n")
    
    func = _input.split()[0]

    if func.lower() == 'add': table.insert(str(_input.split()[1]))
    elif func.lower() == 'remove_data' or func.lower() == 'removedata': table.removeData(str(_input.split()[1]))
    elif func.lower() == 'remove_position' or func.lower() == 'removeposition': table.removePos(int(_input.split()[1]))
    elif func.lower() == 'find': print("\n" + str(table.find(str(_input.split()[1]))))
    elif func.lower() == 'in_table' or func.lower() == 'intable': print("\n" + table.inTable(str(_input.split()[1])))
    elif func.lower() == 'show_table' or func.lower() == 'showtable': print("\n" + table.__repr__())
    elif func.lower() == 'exit': exit()

    print("\n")
    #print(func)