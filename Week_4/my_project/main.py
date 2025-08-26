
# 4. main.py 
# Using the package. 
# Main.py 
# Import the whole package
import my_package
print(my_package.add(5, 3))
print(my_package.subtract(10, 4))
print(my_package.capitalize_text("python"))  # Python

# OR import specific modules
from my_package import string_utils

print(string_utils.reverse_text("hello"))  # olleh

# 5.CODE REUSABILITY 
# **What is Code Reusability?**

# - Code reusability means writing code once and using it multiple times instead of rewriting it.

# - It helps make programs cleaner, faster to develop, and easier to maintain.

# - In Python, code reusability is achieved using;

#     - Functions (reusing blocks of code)

#     - Modules (saving functions in .py files to import later)

#     - Packages (organizing modules in folders)

#     - Classes & Objects (OOP makes reusable blueprints)

#     - Libraries (built-in or third-party)


    

# 🔹 Why Reuse Code?

#     - Saves time – no need to rewrite the same logic.

#     - Avoids duplication – reduces errors from copy and paste.

#     - Improves readability – your code is modular and organized.

#     - Easy to maintain – update once, reuse everywhere.

# 6. ORGANIZING A PYTHON PROJECT
# - A modular project is a way of organizing your code into separate files and folders, each responsible for a specific task.

# - This makes the project easier to read, test, and maintain.
# **Why Use Modular Structure?**

# - Separates concerns – Each file has one responsibility.

# - Easier to debug – You can fix issues in one place without breaking others.

# - Reusability – Functions/modules can be reused in other projects.

# - Collaboration-friendly – Multiple developers can work on different parts.
# ```**Folder & File Structure**

# - Let’s say we want to build a Student Records Project.
# - We will first structure our folder and files like this.
# student_project/
# │
# ├── data.py        # Handles storing and retrieving student data
# ├── utils.py       # Contains helper functions (e.g., calculations, formatting)
# ├── main.py        # Entry point to run the project


