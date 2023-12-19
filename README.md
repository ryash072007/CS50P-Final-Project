# LIBRARY MANAGEMENT SYSTEM
#### Video Demo: https://youtu.be/BtgWdnOEObk
#### Description:

This is the final project for CS50P for Ryash072007.
The aim of the project is provide a simple TUI (Textual User Interface) to manage a user's borrowed and returned books as well as to borrow more books from the virtual library.

## How to use

 1. Prompts user if they want to Sign In or Register themself.
	 0 -> Sign In
	 1 -> Register
	 
2. If 0 is entered / Sign In is selected, the user is prompted to enter their username followed by their password. If they are valid, they are taken to the dashboard, otherwise, they are taken back to 1.
3. If 1 is entered / Register is selected, the user is prompted to enter what they want their new username to be followed by what they want to set their password to. Then, they are taken to their dashboard.

4. The user can then see which all books they have borrowed at the moment and which all books they have returned in the past by selecting option 0 and 1 respectively.

5. The user can borrow more books by selecting option 2, upon which they have 3 more options: search by book name (0), list all books (1), and random book (2).

6. The user can return books by selection option 3, upon which they are prompted to enter which book they want to return. This page also shows which books are overdue and which are still within valid range.

7. The user can exit by selection option 4.


## Design
There is a folder in the same level as project.py labelled "library_data" which contains variable amounts (number of users) of '.data' files. The names of these files are the usernames and the data for that user, i.e, the password, borrowed books, and returned books along with their issue dates and return dates are stored there. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNTM4ODg1NTcsLTkxMzE3ODY3NiwtNj
cxNTU3NDE2LC0xMzYzMDg5NjA1LC0xMzA0NzcxMzc4XX0=
-->