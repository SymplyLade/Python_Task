# Modularizing Your codes 3 (Object Oriented Programming)
# 1. Introduction to Classes
# 2. Why Classes are Important
# 3. Basic Class Structure
# 4. Objects and Instances
# 5. The __init__ Method
# 6. Understanding `self`
# 7. Attributes
# 8. Methods
# 9. Other Important Methods
# 10. Simple Examples
# 11. Intermediate Examples
# 12. Complex Examples
# 13. Best Practices
# What is a class?
# A class is like a blueprint or template that defines what something should look like and what it can do.
# Think of it as a meat-pie cutter - it defines the shape and characteristics, but it's not the actual meat pie itself.
# take a look at this:
# A house blueprint shows where rooms go, but it's not a house you can live in.
#  A car design document describes features, but you can't drive the design.
# A recipe tells you how to make a cake, but the recipe is not edible.
# Object/instance
#what is an object/instance?
# An object (also called an i stance) is a specific, real item created from a class blueprint. it's the actual "thing" you can use and interact with.
# Take a look at this:
# Your actual house built from the blueprint.
# A specific toyota camry manufactured from car desings.
# The delicious cake baked from the recipe.
# Key characteristics of classes
# Encapuslation: Groups related data and functions together
# Abstraction: hides complex implementation details.
# Inheritance: can create new classes based on existing ones (Reuseablity-write once, use many times)
# Why classes are important
# classes help us:
# Organize code: keep related data and functions together
# Model Real world: Represent real-world entities in code
# Reduce Repetition : Avoid writing the same code multiple times
# Maintain code: Easier to update and fix bugs
# scale applications: Build larger, more complex programs
# ** The foundation**
# -__init__` and `self`
#  - Before we dive into attributes and methods, we need to understand two special concepts that make everything work: __init__ and self.
# Real-world analogy
# When a baby is born in nigeria, certain things happen automatically:
# Birth certificate is created
# Name is assigned
# Parents are recorded
# Date of birth is noted
# Similarly, when an object is "born" (created), __init__ automatically
# Sets up the  object's attributes
# Assigns initial values
# prepares the object for use
# class student:
#     def __init__(self, name, course, level):
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created!")
# # When you create a student, __init__ runs automatically
# kemi = student("Kemi Adebayo", "Computer Science", 300)
# What is self?
# Self is a reference to the specific object you're working with. it's like saying "this particular student"or "this specific bank account."
# Real-world analogy
# in a classroom with many students:
# When the teacher says "Kemi, what is your course?" - "Your" refers to kemi specifically
# When the teacher says "Chinedu, what is your level?" - "Your" refers to chinedu specifically
# in programming:
# Self.name means "this specific object's name"
# Self.course means "this specific object's course"
# **Visual Illustration**
# ```
# Class: Student (The Template)
# ├── def __init__(self, name, course):
# │   ├── self.name = name      ← "Give THIS object a name"
# │   └── self.course = course  ← "Give THIS object a course"
# Creating Objects:
# ├── kemi = Student("Kemi", "CS")
# │   └── self refers to kemi → kemi.name = "Kemi"
# ├── chinedu = Student("Chinedu", "Engineering")
# │   └── self refers to chinedu → chinedu.name = "Chinedu"
# └── fatima = Student("Fatima", "Medicine")
#     └── self refers to fatima → fatima.name = "Fatima"
# how init and self work together
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"step1: Creating student object...")
#         self.name = name               # step2: Assign name to this object
#         self.state_of_origin = state   # step3 : Assign state to this object
#         self.course = course           # step4: Assign course to this object
#         self.student_id = self.generate_id() # step5: Generate ID for this object
#         print(f"step6: {self.name} from {self.state_of_origin} is ready!")
#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"
# # When you create an object, here's what happens:
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
# print(ayo.name)
# print(ayo.student_id)
# More example
# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")
#     def buy_airtime(self, amount):
#         self.airtime += amount  # self ensures it goes to the Right person
#         return f"{self.name} now has #{self.airtime} airtime"
# # Creating Multiple users
# abeeb = PhoneUser("Abeeb Bakare", "MTN")
# onisemo = PhoneUser("Onisemo Williams", "Airtel")
# # Each person's actions affect only their own account
# print(abeeb.buy_airtime(500))    # Tunde now has #500 airtime
# print(onisemo.buy_airtime(1000))  # Blessing now has #1000 airtime
# print(abeeb.airtime)              # 500 (Tunde's airtime unchanged)
# print(onisemo.airtime)            # 1000 (Blessing's airtime unchanged)**Key Rules**
# 1. __init__ always takes self as first parameter
# 2. All methods take self as first parameter
# 3. Never pass self manually when calling methods
# 4. Use self inside methods to access object's attributes
# 5. self refers to the specific object being used
# Attributes
# **What are Attributes?**
# Attributes are the characteristics, properties, or data that describe an object. They answer the question "What does this object look like?" or "What information does this object store?"
# **Real-World Analogy**
# - Think of a Nigerian National ID card
#     - me: "Adebayo Tosin"
#     - Age: 28
#     - State of Origin: "Lagos"
#     - LGA: "Ikeja"
#     - Occupation: "Software Developer"
# - These are all attributes - they describe WHO the person is, not what they can DO.
# Defining Attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.cgpa = 0.0
# # creating a student object
# Fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State", )
# # Accessing attributes
# print(Fathia.name)
# print(Fathia.course)
# print(Fathia.state_of_origin)
# print(Fathia.level)
#Types of Attributes
# #1. Instance Attributes - Unique to each object
# student1 = Student("Anthony Johnson", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 400, "Lagos")
# print(student1.name)
# print(student2.name)
# #2 Class attributes - Shared by all objects of the class

# class Student:
#     university = "Federal University of Technology Akure"
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
# # create attribute of student
# student1 = Student("John", "Chemistry")
# # student2 = Student("Bola", "Biology")
# # print(Student.university)
# # print(student1.university)
# # print(student1.name)
# # print(student2.university)
# #Methods: The Actions (What Objects CAN DO)
# # What are Methods?
# #Methods are functions that belong to a class. 
# # They define what actions an object can perform.
# # They answe the question "What can this object do?"
# # Real-world Analogy
# # Think of what a Nigerian student bcan do
# # Study()
# # WriteExam()
# # PaySchoolFees()
# # RegisterCourses()
# # AttendLectures()
# # There are all methods- they describe what the person can DO, not what they look like. 

# class Student:
#     def __init__(self, name, course, level):
#         # Attributes
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False
    

#      # Method: action the student can do
#     def pay_school_fees(self):                   
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"
    
#     # Method: another action
#     def register_courses(self):                   
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"
    
#       # Method: calculates CGPA
#     def calculate_cgpa(self, grades):           
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided"

# # Using methods
# Abiodun = Student("Abiodun Akinola", "Gistology", 600)
# print(Abiodun.pay_school_fees())        
# print(Abiodun.register_courses())       
# print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))

# # Types of Methods
# # 1. Instance Methods - Work with specific object data
# # 'self' refers to the specific student
# def pay_school_fees(self):  
#     return f"{self.name} has paid school fees"

# # 2. Class Methods - Work with class-level data
# @classmethod
# def get_university(cls):
#     return cls.university

# # 3. Static Methods- Don't need object or class data
# @staticmethod
# def academic_calendar():
#     return "Academic session runs from September to July"

# # How Attributes and Methods Work Together
# # The Relationship:
# # - Atrributes store the data
# # - Methods use and modify that data
# class BankAccount:
#     def __init__(self, owner, bank_name, balance=0):
#         # ATTRIBUTES - What the account HAS
#         self.owner = owner
#         self.bank_name = bank_name
#         self.balance = balance
#         self.account_number = self.generate_account_number()
    
#     # METHODS - What the account can DO
#     def deposit(self, amount):
#         """Add money to the account"""
#         if amount > 0:
#             self.balance += amount  # Method changes attribute
#             return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
#         return "Invalid deposit amount"
    
#     def withdraw(self, amount):
#         """Remove money from the account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount  # Method changes attribute
#             return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
#         return "Insufficient funds or invalid amount"
    
#     def transfer(self, amount, recipient):
#         """Transfer money to another account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
#         return "Transfer failed: Insufficient funds"
    
#     def check_balance(self):
#         """Check current balance"""
#         return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
#     def generate_account_number(self):
#         """Generate a unique account number"""
#         import random
#         return f"01{random.randint(10000000, 99999999)}"

# # Creating and using the account
# adunni_account = BankAccount("Adunni Olaleye", "AXT Bank", 50000)

# # Attributes (characteristics)
# print(f"Owner: {adunni_account.owner}")
# print(f"Bank: {adunni_account.bank_name}")
# print(f"Account Number: {adunni_account.account_number}")

# # Methods (actions)
# print(adunni_account.deposit(25000))    
# print(adunni_account.withdraw(10000))  
# print(adunni_account.transfer(15000, "Sunday James"))  
# print(adunni_account.check_balance())   

# # Practice Exercise 1
# # Given this class, identify the attributes and methods. 
# class NaijaPhone:
#     def __init__(self, brand, model, network_provider):
#         self.brand = brand
#         self.model = model
#         self.network_provider = network_provider
#         self.airtime_balance = 0
#         self.data_balance = 0
#         self.is_on = False
    
#     def power_on(self):
#         self.is_on = True
#         return f"{self.brand} phone is now on. Network: {self.network_provider}"
    
#     def buy_airtime(self, amount):
#         self.airtime_balance += amount
#         return f"₦{amount} airtime purchased. Balance: ₦{self.airtime_balance}"
    
#     def make_call(self, number):
#         if self.is_on and self.airtime_balance > 0:
#             self.airtime_balance -= 10
#             return f"Calling {number}... Remaining airtime: ₦{self.airtime_balance}"
#         return "Cannot make call. Check phone power and airtime balance"
    
#     def send_sms(self, message, number):
#         if self.airtime_balance >= 4:
#             self.airtime_balance -= 4
#             return f"SMS sent to {number}: '{message}'. Remaining airtime: ₦{self.airtime_balance}"
#         return "Insufficient airtime to send SMS"

# # Type in the answer here, also run the code to see the output.
# # create an instance of NaijaPhone
# phone = NaijaPhone ("Apple", "iPhone 16 pro", "GLo")
# # Test the methods
# print(phone.power_on())
# print(phone.buy_airtime(500))
# print(phone.make_call("09033262020"))
# print(phone.send_sms("Hello!!", "09033262020"))


# # Practice Exercise 2
# # Given this class, identify the attributes and methods

# class BRTBus:
#     def __init__(self, route, bus_number):
       
#         self.route = route            
#         self.bus_number = bus_number    
#         self.current_stop = "Ikorodu"
#         self.passenger_count = 0
#         self.fare = 300
    
 
#     def announce_stop(self):
#         return f"Next stop: {self.current_stop}. Fare is ₦{self.fare}"
    
#     def board_passengers(self, count):
#         self.passenger_count += count
#         return f"{count} passengers boarded. Total: {self.passenger_count}"
# # Create an instance of BRTBus
# bus = BRTBus("Lagos-Ikorodu", "BRT124")
# # Test the methods
# print(bus.announce_stop())
# print(bus.board_passengers(10))


# # Practice Exercise 3
# # Given this class, identify the attributes and methods
# class MarketTrader:
#     def __init__(self, name, market_name, goods):
       
#         self.name = name                
#         self.market_name = market_name 
#         self.goods = goods             
#         self.daily_sales = 0
    
  
#     def advertise_goods(self):
#         return f"{self.name} at {self.market_name}: Fresh {', '.join(self.goods)} available!"
    
#     def make_sale(self, amount):
#         self.daily_sales += amount
#         return f"Sale made! Today's total: ₦{self.daily_sales:,}"

# # create an instance of MarketTrader
# trader = MarketTrader ("Wale", "Gbagi Market", ["yam", "tomatoes", "pepper"])
# # Test the methods
# print(trader.advertise_goods())
# print(trader.make_sale(400))
# print(trader.make_sale(200))
# print(f"Final daily sale: {trader.daily_sales}")


# ENCAPSULATION

# **What is Encapsulation?**

# Encapsulation is like putting related items in a box and controlling who can access them. It groups related data (attributes) and functions (methods) together in one class, and controls how they can be accessed from outside.

# - Real-World Analogy - Think of an ATM machine:

#    - Inside the ATM: Cash, card reader, computer system, cameras
# #    - What you can access: Keypad, screen, card slot, cash dispenser
# #    - What you cannot access: Internal cash storage, computer motherboard, security cameras

# # - The ATM encapsulates all its internal components and only gives you safe ways to interact with it.

# class NigerianBankAccount:
#     def __init__(self, owner, initial_balance=0):
#         self.owner = owner
#         self._balance = initial_balance        # Protected attribute
#         self.__pin = "1234"                   # Private attribute
#         self._transaction_history = []        # Protected attribute
    
#     # Public methods - anyone can use these
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             self._transaction_history.append(f"Deposited ₦{amount:,}")
#             return f"₦{amount:,} deposited successfully"
#         return "Invalid deposit amount"
    
#     def withdraw(self, amount, pin):
#         if self.__verify_pin(pin):  # Uses private method
#             if amount <= self._balance:
#                 self._balance -= amount
#                 self._transaction_history.append(f"Withdrew ₦{amount:,}")
#                 return f"₦{amount:,} withdrawn successfully"
#             return "Insufficient funds"
#         return "Invalid PIN"
    
#     def check_balance(self, pin):
#         if self.__verify_pin(pin):
#             return f"Current balance: ₦{self._balance:,}"
#         return "Invalid PIN"
    
#     # Private method - only the class can use this
#     def __verify_pin(self, entered_pin):
#         return entered_pin == self.__pin
    
#     # Protected method - subclasses can use this
#     def _get_transaction_history(self):
#         return self._transaction_history.copy()


# # Using the encapsulated account
# ibrahim_account = NigerianBankAccount("Ibrahim Orekunrin", 50000)

# # These work - public interface
# print(ibrahim_account.deposit(10000))      # ₦10,000 deposited successfully
# print(ibrahim_account.withdraw(5000, "1234"))  # ₦5,000 withdrawn successfully
# print(ibrahim_account.check_balance("1234"))   # Current balance: ₦55,000

# # Try this out...

# # But it won't  work - private/protected data

# # print(ibrahim_account.__pin)           # Error! Cannot access private attribute
# # ibrahim_account.__verify_pin("1234")   # Error! Cannot access private method


# # ABSTRACTION

# from abc import ABC, abstractmethod

# # Abstract base class - defines what a Nigerian student should do
# class NigerianStudent(ABC):
#     def __init__(self, name, course, level):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.fees_paid = False
    
#     # Concrete method - all students can do this
#     def pay_school_fees(self, amount):
#         self.fees_paid = True
#         return f"{self.name} paid ₦{amount:,} school fees"
    
#     # Abstract method - each type of student implements differently
#     @abstractmethod
#     def study_method(self):
#         pass
    
#     @abstractmethod
#     def take_exam(self):
#         pass

# # Concrete classes - specific implementations
# class MedicalStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} studies anatomy books and practices on cadavers"
    
#     def take_exam(self):
#         return f"{self.name} takes practical exam in the anatomy lab"

# class EngineeringStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} solves mathematical problems and builds prototypes"
    
#     def take_exam(self):
#         return f"{self.name} takes exam with calculations and technical drawings"

# class ComputerScienceStudent(NigerianStudent):
#     def study_method(self):
#         return f"{self.name} codes programs and debugs software"
    
#     def take_exam(self):
#         return f"{self.name} takes practical programming exam on computer"


# # Using abstraction
# students = [
#     MedicalStudent("Dr.Adeyinka Ogunsanya", "Medicine", 400),
#     EngineeringStudent("Dr. Ajala Gift", "Mechanical Engineering", 300),
#     ComputerScienceStudent("Fatima Hassan", "Computer Science", 200)
# ]

# # Same interface, different implementations
# for student in students:
#     print(student.pay_school_fees(150000))  # Same for all
#     print(student.study_method())           # Different for each
#     print(student.take_exam())              # Different for each
#     print("---")

#Simple abstraction for phone interface

class SimplePhone:
    def __init__(self, brand):
        self.brand = brand
        self._complex_internal_system = "Very complicated stuff"
    
    # Simple interface - user doesn't need to know internal complexity
    def make_call(self, number):
        self._establish_network_connection()
        self._encode_voice_signal()
        self._transmit_to_tower()
        return f"Calling {number} from {self.brand} phone..."
    
    def send_sms(self, message, number):
        self._connect_to_sms_center()
        self._format_message()
        self._send_through_network()
        return f"SMS sent to {number}: '{message}'"
    
    # Complex internal methods - hidden from user
    def _establish_network_connection(self):
        # Complex networking code here
        pass
    
    def _encode_voice_signal(self):
        # Complex audio processing here
        pass
    
    def _transmit_to_tower(self):
        # Complex radio transmission here
        pass
    def _connect_to_sms_center(self):
    # code to connect to sms center
       pass
    def _format_message(self):
        # code to format sms message
        pass
    def _send_through_network(self):
        #code to send through sms message
        pass

# User only needs to know the simple interface
my_phone = SimplePhone("Tecno")
print(my_phone.make_call("08012345678"))  # Simple to use
print(my_phone.send_sms("How far?", "08098765432"))  # Don't need to know internals

# **Benefits of Abstraction**

# - Simplicity: Complex systems become easy to use
# - Focus: Users focus on what matters, not how it works
# - Flexibility: Implementation can change without affecting users
# - Reusability: Same interface works for different implementations

# INHERITANCE - BUILDING ON WHAT ALREADY EXISTS

# **What is Inheritance?**

# Inheritance allows you to create new classes based on existing ones. The new class (child) inherits attributes and methods from the parent class, and can add its own features or modify existing ones.

# - Real-World Analogy
#    - Think of a Nigerian family

#        - Parent (Father): Adebayo Ogundimu - has surname, family traditions, property
#        - Child 1 (Son): Kemi Ogundimu - inherits surname, traditions, gets family property + adds his own career as doctor
#        - Child 2 (Daughter): Tunde Ogundimu - inherits surname, traditions, gets family property + adds her own career as engineer

# - The children inherit from their father but also have their own unique characteristics.

# Parent class - Base Nigerian Person
# class NigerianPerson:
#     def __init__(self, first_name, last_name, state_of_origin):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.state_of_origin = state_of_origin
#         self.can_speak_english = True
    
#     def introduce(self):
#         return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}"
    
#     def greet(self):
#         return "Good morning!"
    
#     def speak_local_language(self):
#         return "I speak my local language"

# # Child class 1 - Nigerian Student inherits from NigerianPerson
# class NigerianStudent(NigerianPerson):
#     def __init__(self, first_name, last_name, state_of_origin, course, level):
#         # Inherit parent's initialization
#         super().__init__(first_name, last_name, state_of_origin)
#         # Add student-specific attributes
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
    
#     # Override parent method with student-specific version
#     def introduce(self):
#         parent_intro = super().introduce()  # Get parent's introduction
#         return f"{parent_intro}. I'm a {self.level} level {self.course} student"
    
#     # Add student-specific methods
#     def study(self):
#         return f"{self.first_name} is studying {self.course}"
    
#     def take_exam(self):
#         return f"{self.first_name} is writing {self.course} exam"

# # Child class 2 - Nigerian Worker inherits from NigerianPerson
# class NigerianWorker(NigerianPerson):
#     def __init__(self, first_name, last_name, state_of_origin, job_title, company):
#         super().__init__(first_name, last_name, state_of_origin)
#         self.job_title = job_title
#         self.company = company
#         self.salary = 0
    
#     def introduce(self):
#         parent_intro = super().introduce()
#         return f"{parent_intro}. I work as a {self.job_title} at {self.company}"
    
#     def work(self):
#         return f"{self.first_name} is working as a {self.job_title}"
    
#     def receive_salary(self, amount):
#         self.salary += amount
#         return f"{self.first_name} received ₦{amount:,} salary"

# # Child class 3 - Nigerian Teacher (inherits from NigerianWorker)
# class NigerianTeacher(NigerianWorker):
#     def __init__(self, first_name, last_name, state_of_origin, subject, school):
#         # Teacher is a type of worker
#         super().__init__(first_name, last_name, state_of_origin, "Teacher", school)
#         self.subject = subject
#         self.students = []
    
#     def introduce(self):
#         return f"My name is {self.first_name} {self.last_name} from {self.state_of_origin}. I teach {self.subject} at {self.company}"
    
#     def teach(self):
#         return f"Teacher {self.first_name} is teaching {self.subject}"
    
#     def grade_students(self):
#         return f"Teacher {self.first_name} is grading {self.subject} assignments"

# # Using inheritance
# # Create different types of people
# student = NigerianStudent("Kemi", "Adebayo", "Lagos State", "Computer Science", 300)
# worker = NigerianWorker("Chinedu", "Okafor", "Anambra State", "Software Developer", "Sail Innovation Lab")
# teacher = NigerianTeacher("Chris", "Ekwugum", "Lagos State", "Data Science", "Sail Innovation Lab")


# # All inherit basic Nigerian person abilities
# print("=== Basic Inherited Methods ===")
# print(student.greet())                    # Good morning! (inherited)
# print(worker.speak_local_language())      # I speak my local language (inherited)
# print(teacher.greet())                    # Good morning! (inherited)

# print("\n=== Customized Introductions ===")
# print(student.introduce())    # Customized for students
# print(worker.introduce())     # Customized for workers  
# print(teacher.introduce())    # Customized for teachers

# print("\n=== Specific Abilities ===")
# print(student.study())        # Only students can do this
# print(worker.work())          # Only workers can do this
# print(teacher.teach())        # Only teachers can do this


# # **Inheritance Hierarchy Visualization**

# # NigerianPerson (Parent)
# # ├── Attributes: first_name, last_name, state_of_origin
# # ├── Methods: introduce(), greet(), speak_local_language()
# # │
# # ├── NigerianStudent (Child)
# # │   ├── Inherits: All parent attributes and methods
# # │   ├── Adds: course, level, cgpa
# # │   └── Adds: study(), take_exam()
# # │
# # ├── NigerianWorker (Child)
# # │   ├── Inherits: All parent attributes and methods
# # │   ├── Adds: job_title, company, salary
# # │   ├── Adds: work(), receive_salary()
# # │   │
# # │   └── NigerianTeacher (Grandchild)
# # │       ├── Inherits: Everything from NigerianWorker + NigerianPerson
# # │       ├── Adds: subject, students
# # │       └── Adds: teach(), grade_students()


# # TYPES OF INHERITANCE
# # 1. Single Inheritance - One parent
# class Parent:
#     pass

# class Child(Parent):  # Child inherits from Parent
#     pass

# # 2. Multiple Inheritance - Multiple parents
# class Father:
#     def father_trait(self):
#         return "Strong"

# class Mother:
#     def mother_trait(self):
#         return "Caring"

# class Child(Father, Mother):  # Inherits from both parents
#     pass

# child = Child()
# print(child.father_trait())  # Strong
# print(child.mother_trait())  # Caring

# # **Benefits of Inheritance**

# # - Code Reuse: Don't write the same code multiple times
# # - Organization: Related classes are grouped logically
# # - Maintenance: Fix bugs in parent class, all children benefit
# # - Extensibility: Easy to add new types without changing existing code

# # HOW ALL (ABSTRACTION,ENCAPSULATION,INHERITANCE) WORK TOGETHER

# # Nigerian School Management System

# # Abstraction - Define what all school members should do
# from abc import ABC, abstractmethod

# class SchoolMember(ABC):
#     def __init__(self, name, id_number):
#         self._name = name           # Encapsulation - protected attribute
#         self._id_number = id_number # Encapsulation - protected attribute
    
#     @abstractmethod
#     def daily_activity(self):       # Abstraction - must be implemented
#         pass
    
#     def get_info(self):            # Common method for all
#         return f"Name: {self._name}, ID: {self._id_number}"

# # Inheritance - Student inherits from SchoolMember
# class Student(SchoolMember):
#     def __init__(self, name, id_number, class_level):
#         super().__init__(name, id_number)  # Inheritance
#         self.__grades = []                 # Encapsulation - private
    
#     def daily_activity(self):              # Abstraction - implementation
#         return f"{self._name} attends classes and studies"
    
#     def add_grade(self, subject, score):   # Encapsulation - controlled access
#         if 0 <= score <= 100:
#             self.__grades.append({"subject": subject, "score": score})
#             return f"Grade added: {subject} = {score}"
#         return "Invalid grade"
    
#     def get_average(self):                 # Encapsulation - controlled access
#         if self.__grades:
#             total = sum(grade["score"] for grade in self.__grades)
#             return total / len(self.__grades)
#         return 0

# # Inheritance - Teacher inherits from SchoolMember
# class Teacher(SchoolMember):
#     def __init__(self, name, id_number, subject):
#         super().__init__(name, id_number)
#         self.__subject = subject           # Encapsulation - private
    
#     def daily_activity(self):              # Abstraction - implementation
#         return f"{self._name} teaches {self.__subject} and grades assignments"

# # Using all three principles together
# student = Student("Adunni Olaleye", "STU001", "SS2")
# teacher = Teacher("Mr. Emeka Nwosu", "TCH001", "Mathematics")

# # Polymorphism - same method, different behavior
# print(student.daily_activity())    # Student-specific activity
# print(teacher.daily_activity())    # Teacher-specific activity

# # Encapsulation - controlled access to data
# print(student.add_grade("Mathematics", 85))  # Grade added: Mathematics = 85
# print(student.add_grade("English", 78))      # Grade added: English = 78
# print(f"Average: {student.get_average()}")   # Average: 81.5

# # Can't access private data directly
# # print(student.__grades)  # This would cause an error