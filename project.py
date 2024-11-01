###################################################### Library Management System #################################################################################
from datetime import date
import tkinter as tk
from tkinter import ttk

# Dictionaries for genres
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

genres = {"fiction": fiction, "mystery": mystery, "sci-fi": sci_fi, "non-fiction": non_fi}

# Initialize the main window
root = tk.Tk()
root.title("Library Management System")

# Create a variable to store the selected option
selected_genre = tk.StringVar(root)
selected_genre.set("fiction")  # Set the default option

# Dropdown for genre selection
dropdown = tk.OptionMenu(root, selected_genre, *genres.keys())
dropdown.pack(pady=20)

# Function to display books based on selected genre
def show_books():
    genre_key = selected_genre.get()
    books = genres.get(genre_key, {})

    # Create a new window for the selected genre
    book_window = tk.Toplevel(root)
    book_window.title(f"Library - {genre_key.capitalize()} Section")

    # Treeview for displaying books
    columns = ("Title", "Status", "Author")
    tree = ttk.Treeview(book_window, columns=columns, show="headings")
    tree.heading("Title", text="Title")
    tree.heading("Status", text="Status")
    tree.heading("Author", text="Author")
    tree.column("Title", width=200)
    tree.column("Status", width=100)
    tree.column("Author", width=150)
    tree.pack(expand=True, fill="both")

    # Insert data into the Treeview
    for title, details in books.items():
        status, author = details
        tree.insert("", "end", values=(title, status, author))

# Button to confirm the selection and show books
button = tk.Button(root, text="Show Books", command=show_books)
button.pack(pady=10)

root.mainloop()

# Fine calculation function
def book_manager(days_difference):
    fine = 0
    if days_difference > 7:
        fine += 10 * (days_difference - 7)
        print("Your fine is: ₹", fine, "/-")
    else:
        print("The Book is returned successfully!")

# Input and fine calculation
issue_book = date(2024, int(input("Enter month of issue: ")), int(input("Enter date of issue: ")))
return_book = date(2024, int(input("Enter month of return: ")), int(input('Enter date of return: ')))
difference = return_book - issue_book
days_difference = difference.days
book_manager(days_difference)
