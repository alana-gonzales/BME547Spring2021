def create_database_entry(name, id_no, age):
    new_patient = [name, id_no, age, []]

    return new_patient

def print_directory(db):
    other_data = ['Room 2', 'Room 3', 'Room 4', 'Room 5']
    for i, patient in enumerate(db):    # enumerate saves the indexes in a list
        print(i)
        print("Name: {}, ID: {}, Age: {}".format(patient[0], patient[1], patient[2]))
        print('Patient is in {}'.format(other_data[i]))

def find_patient(id_no, db):
    for patient in db:
        if patient[1] == id_no:
            print("The patient with ID number {} is {}.".format(patient[1], patient[0]))
            return patient[0]
    return "Patient not found"

def add_test_result(id_no, db, test_name, test_result):
    for patient in db:
        if patient[1] == id_no:
            patient[3].append((test_name, test_result))
    # don't need to return anything because it is a mutable list, so the list is updated everywhere

def main():
    db = list()
    db.append(create_database_entry("Ann Ables", 1, 30))
    db.append(create_database_entry("Bob Boyles", 2, 31))
    db.append(create_database_entry("Chris Chou", 3, 32))
    db.append(create_database_entry("David Dinkins", 4, 33))
    #print(db[1])    # prints out Bob's entry
    #print(db[-1])   # prints the last entry
    #print(db[0:2])  # starts at index 0 and goes up to but not including index 2
    #print(db[1:])   # starts at index 1 and goes to the end

    # NOTE: can index strings like this too

    #names = [i[0] for i in db]      # list comprehension to print first item in each entry 
    #print(names)

    #print_directory(db)
    #my_name = find_patient(2, db)
    #print(my_name)

    print(db)
    add_test_result(3, db, "HDL", 65)
    print(db)
    add_test_result(3, db, "LDL", 80)
    print(db)

if __name__ == "__main__":
    main()
