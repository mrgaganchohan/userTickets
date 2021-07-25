# How to view README.md:
  For better preview, go to https://github.com/mrgaganchohan/userTickets  to see in good format, or in vscode right click on README.md => 'Open Preview'

## Structure of Project
  - main.py: main.py sits in the root of the project. This is the main file which sits in 'userTickets' folder

  - **json-files** : This folder in turn contains two folders, which are "users" and "tickets". These folders are used for placing files which are meant to be read. For example:
      - Multiple user files(.json) can be placed inside json-files/users, and data of all of them will be combined for search purposes. By default: both have files inside them
      - Similarly, tickets folder can have multiple tickets file whose data will be combined while running
    
  - **src**: src folder has two main things
      - run.py: contains main workflow, which calls other services like search, read or print
      - **services**: It contains category specific service files like search(search_service.py) or read_service or print_service. For example read only performs reading from files, and printing takes care of strings which gets displayed on console.
    
  - **tests**: tests folder contains test for services files and run.py file.For testing  whether users.json or tickets.json's read functionality, it also has a foldeer called test_json-files which contains tickets and users json files for testing

## Installation & set up
   **Language used** : Python 3.9.6 has been used to run the project. For best results please make sure you have at least 3.9 installed on your system. You can download it from here https://www.python.org/downloads/

   **OS** : Project has been tested on OSX (MAC)

## Set up
Requirements: python installed on system. check your version by running following command in terminal
```
python3 -V
   
Output:   Python 3.9.6
```

Assuming you have installed python 3.9.6(might work with python 3.7+ but hasn't been tested) and cloned the project from github in your local machine, do as follows:
    
   - cd into root folder, the root folder will have main.py file, src folder json-files and tests folder
   - **set up Virtual environment**: To set up virtual env run following command(make sure your terminal is in project's root folder)
   ```
   python3 -m venv venv
   ```  
   
  - The previous command would have created a **venv/** folder inside project's root folder. (if it is not created make sure python is installed and is available through command line)
  - **Activate virtual env**: To activate virtual environment, make sure you are in project's root folder, and run following command in terminal:
  
  MAC
  ```
  source venv/bin/activate
  ```
  WINDOWS CMD
  ```
  C:\> <venv>\Scripts\activate.bat
  ```
 - **Check if venv is active**: you will see  (venv) in your command line.

 # Executing the project
   **Pre-Requisite**: Installation and set up has been done, and venv is active.  
   
   make sure before execution you are in project's root directory, and you should see following output 
   
   ```
   python -V 

   Python 3.9.6
   ```

   json-files folder already has users and tickets folder, which in turn  has ['users.json', 'users 2.json'], 'users.json'] and ['tickets.json'].So, nothing needs to be done from user's end
   Execution command in root folder of project as :
   ```
   python main.py
   ```
   and it should start, and you should see a welcome message as follows:
   ```
   python main.py
   Welcome to Search
   Type 'quit' to exit at any time, Press 'Enter' to continue 
   ```
# Running Tests
  - To run tests, make sure you are in project's root directory.
  ```
  python -m unittest
  ----------------------------------------------------------------------
  Ran 24 tests in 0.007s

  OK  
  ```
# check code coverage
  ## Install coverage
   - make sure to install coverage before we can see code-coverage. Run following in terminal
   ```
   pip install coverage
   ```

  ## check code coverga
  ### First discover unit tests with following command:
  ```
  coverage run -m unittest discover

  Ran 24 tests in 0.008s
  OK
  ```
  and then  check coverage as follows
  ``` 
  coverage report -m 
  Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src/__init__.py                      0      0   100%
src/run.py                          62      0   100%
src/services/print_service.py       35      0   100%
src/services/read_service.py        18      0   100%
src/services/search_service.py      75      0   100%
--------------------------------------------------------------
TOTAL                              190      0   100%
  ```