class chatbook:

    def __init__(self):
        self.user_name = ""
        self.__name = "hidden_name"
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
                            1. Press 1 to signup
                            2. Press 2 to signin
                            3. Press 3 to write a post
                            4. Press 4 to message a friend
                            5. Press any other key to exit
                             
                            -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.write_post()
        elif user_input == "4":
            self.message_friend()
        else:
            exit()

    def signup(self):
        self.user_name = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print(f"User {self.user_name} signed up successfully!")
        print()
        self.menu()
    
    def signin(self):
        if self.user_name == "" and self.password == "":
            print("No user found! Please signup first.")
            
        else:
            user_name = input("Enter your username: ")
            password = input("Enter your password: ")

            if self.user_name == user_name and self.password == password:
                print("Login successful!")
                self.loggedin = True
                
            else:
                print("Invalid credentials.")
        print("\n")
        self.menu()

    def write_post(self):
        if self.loggedin:
            post_content = input("Write your post: ")
            print("Post published!")
        else:
            print("Please signin to write a post.")
        print("\n")
        self.menu()
    
    def message_friend(self):
        if self.loggedin:
            friend_name = input("Enter your friend's name: ")
            message = input("Enter your message: ")
            print(f"Message sent to {friend_name}!")
        else:
            print("Please signin to message a friend.")
        print("\n")
        self.menu()
                
user = chatbook()

# Creating an instance (object) of chatbook