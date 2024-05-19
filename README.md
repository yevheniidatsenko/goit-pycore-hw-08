## Serialization and Object Copying in Python

This is the final assignment for the Python Object-Oriented Programming course. In this assignment, you will learn the following useful skills:

- Serialization and deserialization of data using pickle
- Working with files

**Technical Description of the Task**

☝ In this assignment, you need to add functionality to save the address book to disk and restore it from disk.

To do this - you need to choose the pickle data serialization/deserialization protocol and implement methods that allow you to save all data to a file and load it from a file.

The main goal is that the application does not lose data after exiting the application and restores it from a file when launched. The address book that we worked with in the previous session should be saved.

Implement functionality to save the state of AddressBook to a file when closing the program and restore the state when it starts.

**Code Examples that will be useful:**

**Serialization with pickle**

```python
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Return a new address book if the file is not found
```

**Integration of saving and loading into the main loop**

```python
def main():
    book = load_data()

    # Main program loop

    save_data(book)  # Call before exiting the program
```

**Instructions:**

1.  Create a file named `addressbook.py`
2.  Implement the `AddressBook` class as described in the previous assignment.
3.  Implement the `save_data` and `load_data` functions as shown in the code examples above.
4.  Modify the `main` function to load the address book from a file at the beginning, save the address book to a file before exiting, and call the main program loop in between.
5.  Test your code by adding a few contacts to the address book, saving it to a file, exiting the program, restarting the program, and loading the address book from the file.

**Additional Notes:**

- Make sure to use a consistent filename for saving and loading the address book.
- You may want to add error handling to your code to deal with potential problems such as file not found or serialization errors.
- Consider using a different serialization format if pickle is not suitable for your needs.
