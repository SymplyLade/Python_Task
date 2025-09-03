# # import re
# # def validate_email(email):
# #     # Regular expression to validate email format
# #     pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
# #     return re.match(pattern, email) is not None
# # def email_slicer():
# #     while True:
# #         # Get user input
# #         email = input("Enter your email (or 'quit' to exit): ")
# #         if email.lower() == 'quit':
# #             break
# #         # Validate email format
# #         if not validate_email(email):
# #             print("Invalid email format! Please try again.")
# #             continue
# #         # Split email into username and domain
# #         username, domain = email.split('@')
# #         # Display extracted username and domain
# #         print(f"Username: {username}")
# #         print(f"Domain: {domain}\n")
# # if __name__ == "__main__":
# #     email_slicer()




# # import re
# # print("=== Email Slicer in Python ===")
# # # 1. Case-insensitive input handling
# # email = input("Enter your email: ").strip().lower()


# # # 2. Validate email using regex
# # pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'



# # if re.match(pattern, email):
# #     # Slice into username and domain
# #     username = email.split("@")[0]
# #     domain = email.split("@")[1]


# #     # 3. Domain categorization (personal vs corporate)
# #     personal_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
# #     if domain in personal_domains:
# #         category = "Personal Email"
# #     else:
# #         category = "Corporate/Other Email"



# #     # 5. Enhance output formatting with extra details
# #     print("\n--- Email Details ---")
# #     print(f"Full Email : {email}")
# #     print(f"Username   : {username}")
# #     print(f"Domain     : {domain}")
# #     print(f"Category   : {category}")
# #     print(f"Email Length: {len(email)} characters")
# #     print("----------------------")





# # To-Do List Application
# # List to store tasks
# tasks = []
# # Function to add

# def add_task():
#     task = input("Enter a task: ")
#     tasks.append({"task": task, "completed": False})
#     print(f"Task '{task}' added successfully!")

# # Function to remove
# def remove_task():
#     if not tasks:
#         print("No tasks to remove!")
#         return
#     print("Tasks:")
#     for i, task in enumerate(tasks, start=1):
#         print(f"{i}. {task['task']} {'(Completed)' if task['completed'] else ''}")
#     task_number = int(input("Enter task number to remove: ")) - 1
#     if task_number < 0 or task_number >= len(tasks):
#         print("Invalid task number!")
#         return
#     task = tasks.pop(task_number)
#     print(f"Task '{task['task']}' removed successfully!")

# # Function to complete task

# def complete_task():
#     if not tasks:
#         print("No tasks to complete!")
#         return
#     print("Tasks:")
#     for i, task in enumerate(tasks, start=1):
#         print(f"{i}. {task['task']} {'(Completed)' if task['completed'] else ''}")
#     task_number = int(input("Enter task number to complete: ")) - 1
#     if task_number < 0 or task_number >= len(tasks):
#         print("Invalid task number!")
#         return
#     tasks[task_number]["completed"] = True
#     print(f"Task '{tasks[task_number]['task']}' marked as completed!")

# # Function to display
# def display_tasks():
#     if not tasks:
#         print("No tasks!")
#         return
#     print("Tasks:")
#     for i, task in enumerate(tasks, start=1):
#         print(f"{i}. {task['task']} {'(Completed)' if task['completed'] else ''}")
# # Function to display all task

# def main():
#     while True:
#         print("\nTo-Do List Application")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. Complete Task")
#         print("4. Display Tasks")
#         print("5. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             add_task()
#         elif choice == "2":
#             remove_task()
#         elif choice == "3":
#             complete_task()
#         elif choice == "4":
#             display_tasks()
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice!")
# if __name__ == "__main__":
#     main()

