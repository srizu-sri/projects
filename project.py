########################################### Library Managemnet System ##################################################################
from datetime import date
import tkinter as tk
from tkinter import ttk
fiction = {"To Kill a Mockingbird": ["Available", "Harper Lee"],
"The Great Gatsby": ["Available", "F. Scott Fitzgerald"],
"1984": ["Available", "George Orwell"],
"The Catcher in the Rye": ["Available", "J.D. Salinger"],
"Pride and Prejudice": ["Available","Jane Austen"],
"The Book Thief":["Available","Markus Zusak"],
"One Hundred Years of Solitude":["Available", "Gabriel García Márquez"],
"The Road":["Available", "Cormac McCarthy"],
"Little Women":["Available","Louisa May Alcott"],
"Beloved":["Available", "Toni Morrison"]}

mystery = {"Gone Girl":["Available", "Gillian Flynn"] ,
"The Girl with the Dragon Tattoo":["Available", "Stieg Larsson"],
"The Da Vinci Code":["Available","Dan Brown"],
"Sherlock Holmes: The Complete Novels and Stories":["Available","Arthur Conan Doyle"],
"Big Little Lies":["Available","Liane Moriarty"],
"The Silent Patient":["Available","Alex Michaelides"],
"In the Woods":["Available","Tana French"],
"The Woman in the Window":["Available","A.J. Finn"],
"And Then There Were None":["Available","Agatha Christie"],
"The Girl on the Train":["Available", "Paula Hawkins"]}

sci_fi = {"Dune":["Available","Frank Herbert"],
"The Hobbit":["Available","J.R.R. Tolkien"],
"Harry Potter and the Sorcerer's Stone":["Available","J.K. Rowling"],
"Ender's Game":["Available","Orson Scott Card"],
"The Name of the Wind":["Available","Patrick Rothfuss"],
"The Fellowship of the Ring":["Available","J.R.R. Tolkien"],
"A Game of Thrones by George":["Available","R.R. Martin"],
"The Left Hand of Darkness":["Available", "Ursula K. Le Guin"],
"The Martian":["Available","Andy Weir"],
"Neuromancer":["Available", "William Gibson"]}

non_fi = {"Sapiens: A Brief History of Humankind":["Available", "Yuval Noah Harari"],
"Educated":["Available","Tara Westover"],
"Becoming":["Available","Michelle Obama"],
"The Immortal Life of Henrietta Lacks":["Available","Rebecca Skloot"],
"Into the Wild":["Available", "Jon Krakauer"],
"The Wright Brothers":["Available", "David McCullough"],
"Unbroken":["Available", "Laura Hillenbrand"],
"Quiet: The Power of Introverts in a World That Can't Stop Talking":["Available", "Susan Cain"],
"Thinking, Fast and Slow":["Available", "Daniel Kahneman"],
"A Brief History of Time":["Available", "Stephen Hawking"]}

gen = [fiction, mystery, sci_fi, non_fi] 
# genre = input("Enter the Genre of book: ") #asks user to input genre 


# Initialize the main window
root = tk.Tk()
root.title("Dropdown Example")

# Create a list of options
genre = ["fiction", "sci-fi", "mystery", "non-fiction"] 

# Create a variable to store the selected option
selected_option = tk.StringVar(root)
selected_option.set(genre[0])  # Set the default option

# Create the dropdown menu
dropdown = tk.OptionMenu(root, selected_option, *genre)
dropdown.pack(pady=20)

# Function to display the selected option
def show_selection():
    print("Selected option:", selected_option.get())

# Button to confirm the selection
button = tk.Button(root, text="Confirm Selection", command=show_selection)
button.pack(pady=10)

root.mainloop()

if genre == "fiction":
    genre = gen[0]
elif genre == "mystery":
    genre = gen[1]
elif genre == "sci-fi":
    genre = gen[2]
elif genre == "non-fi":
    genre = gen[3]

root = tk.Tk()
root.title("Library - Fiction Section")

# Create a Treeview widget with three columns: Title, Status, and Author
columns = ("Title", "Status", "Author")
tree = ttk.Treeview(root, columns=columns, show="headings")

# Set up column headings
tree.heading("Title", text="Title")
tree.heading("Status", text="Status")
tree.heading("Author", text="Author")

# Set up column widths
tree.column("Title", width=200)
tree.column("Status", width=100)
tree.column("Author", width=150)

# Insert data from the dictionary into the Treeview
for title, details in genre.items():
    status, author = details
    tree.insert("", "end", values=(title, status, author))

# Pack the Treeview widget into the window
tree.pack(expand=True, fill="both")

# Run the Tkinter event loop
root.mainloop()








def book_manager(): #func for managing books
    fine = 0
    if days_difference > 7:
        fine+=10*days_difference
        print("Your fine is: ₹",fine,"/-" )
    else:
        print("The Book is returned successfully!")

issue_book = date(2024, int(input("Enter month of issue: ")), int(input("Enter date of issue: ")))
return_book = date(2024, int(input("Enter month of return: ")), int(input('Enter date of return: ')))
difference = return_book - issue_book
days_difference = difference.days
book_manager()

