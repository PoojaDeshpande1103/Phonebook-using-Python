phonebook={}
def display_contact():
     print("Name\t\tContact Number")
     for key in phonebook:
          print("{}\t\t{}".format(key,phonebook.get(key)))
          
while True:
    choice = int(input("1.Add new Contact \n 2.Search COntact \n 3.Display Contact \n 4.Edit Contact \n 5.Delete Contact \n 6.Exit"))
if choice == 1:
     name = input("Enter the contact name: ")
     phone = input("Enter the mobile number: ")
     contact[name]= phone
elif choice ==2:
     search_name = input("Enter the contact name: ")
     if search_name in phonebook:
          print(search_name,"'s contact number is",phonebook[search_name])
     else:
          print("Name is not found")
elif choice ==3:
     if not phonebook:
          print("Empty phonebook")
     else:
          display_contact()
elif choice == 4:
     edit_contact = input("Enter the Contact to be edited")
     if edit_contact in phonebook:
          phone = input("Enter mobile number")
          phonebook(edit_contact)==phone
          print("Contact updated")
          display_contact()
elif choice == 5:
     del_contact = input("Enter the contact to be deleted: ")
     if del_contact in phonebook:
          confirm = input("Are you sure you want to delete this contact y/n?")
          if confirm==y and confirm==Y:
               phonebook.pop(del_contact)
               display_contact()
     else:
          print("Name is not found")
else:
     exit 
     

