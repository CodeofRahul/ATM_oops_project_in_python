class Atm:

  # constructor

  def __init__(self):

    self.pin = ''           # self.pin is an instance variable
    self.balance = 0        # self.balance is an instance variable
    self.menu()

  # create menu to choose from
  def menu(self):
    
    user_input = input("""
    Hi, How can I help you, Today!
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to deposit
    4. Press 4 to check balance
    5. Press 5 to withdraw
    6. Press 6 to exit
    """)

    # taking input from users
    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.deposit()
    elif user_input == '4':
      self.check_balance()
    elif user_input == '5':
      self.withdraw()
    elif user_input == '6':
      exit()

  # to create pin
  def create_pin(self):
    self.pin = input("Enter 4 digit to create pin :")
    print("Pin created Successfully!")
    self.menu()

  # to change pin
  def change_pin(self):
    old_pin = input("Enter old pin :")
    if self.pin == old_pin:
      new_pin = input("Enter new pin to change :")
      self.pin = new_pin
      print("Your new pin is :", self.pin)
      self.menu()
    else:
      print("invalid pin")
      self.menu()

  # to deposit money
  def deposit(self):
    temp = input("Enter your 4 digit pin :")
    if temp == self.pin:
      amount = int(input("Enter amount to deposit :"))
      self.balance += amount
      print("Your amount deposit successful")
      self.menu()
    else:
      print("invalid pin")
      self.menu()

  # to check balance
  def check_balance(self):
    temp = input("Enter your pin :")
    if temp == self.pin:
      print(f"Your current balance is :{self.balance}")
      self.menu()
    else:
      print("invalid pin")
      self.menu()
  
  # to withdraw money
  def withdraw(self):
    temp = input("Enter your pin :")
    if temp == self.pin:
      # allow to withdraw
      amount = int(input("Enter amount to withdraw :"))
      if amount <= self.balance:
        self.balance -= amount
        print("Amount withdraw successful")
        self.menu()
      else:
        print("Insufficient balance")
        self.menu()
    else:
      print("invalid pin")
      self.menu()


        

# creating the object to access class
# this will run only after accepting the card

card = input("Insert your debit card to proceed True/False:")
if card == 'True':
  atm = Atm()
else:
  exit()