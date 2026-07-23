# plp-python-week3
name greeter
<img width="959" height="316" alt="Screenshot 2026-07-23 120757" src="https://github.com/user-attachments/assets/24348f0c-0fd3-4bef-908d-94900b8039da" />
bug hunt
<img width="829" height="335" alt="image" src="https://github.com/user-attachments/assets/f31e47f8-12fd-4b8e-bd99-d5af88c5c1f0" />
ticket checker
<img width="923" height="296" alt="image" src="https://github.com/user-attachments/assets/05511cac-ab31-46ab-bc46-64ee5c70e31e" />

# PLP Python Week 3 – Name Splitter, Bug Hunt & First Decisions

## Files

- **name_greeter.py** – Splits the user's full name using `.split()` and greets them by their first name. If only one name is entered, it asks for the full name.
- **bug_hunt.py** – Fixes three bugs in the provided program and includes `# BUG:` comments explaining each correction.
- **ticket_checker.py** – Checks whether the user is an adult using a Boolean expression and displays the correct ticket price.
- **screenshots/** – Contains screenshots showing each program running successfully.

## Reflection

The bug that took the longest to find was the age calculation because the program stored the age as a string instead of a number. The error message about adding a string and an integer helped identify the problem and showed that the input needed to be converted using `int()`.
