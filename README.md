# Overview
SQLite is used as a temporary dataset to get processed with some data within an application. It results in a database single file. In this example I am able to create a budgting system of purchases that the user makes and it is stored to see where the users money is going to. 

If there is one thing that many of us strugle with, it is keeping track of our expenses. Often we think "where did all my money go?" If thats the case this would be something handy for you to use. 

[Software Demo Video](https://youtu.be/9aIZNXcttY4)

# Relational Database
This Software uses SQLITE and Python. It is a "light" database. SQLITE is often known as self-contained, which requires minimal support from the operating system. This makes SQLITE usable in any enviroment like IPhones, Android, 
game consoles etc..

The two main tables I created were a purchase and deposit table. THe purchase contains all the purchases and dates the user has made throught time. The deposit table stores the deposit the user has made and as well as the date. 

# Development Environment

Sqlite3 provides a SQL-like interface to read, query, and write SQL database from Python.
The flexible parth is that it does not require seperate server process and wllows accessing the datebase simpler.

# Useful Websites
- [Python](https://docs.python.org/3.8/library/sqlite3.html#sqlite3-types)
- [SQLITE tutorial](https://www.sqlitetutorial.net/sqlite-aggregate-functions/)

# Future Work
- Use actual DATETIME()
- Make a graph of what months money was spent on 
- Make functions for user errors