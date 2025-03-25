from ChatBot import ChatBot


def main():
   # Create a ChatBot object with specified files and default response
   bot = ChatBot("greetings.txt", "responses.txt", "Tell me more.")
   print(bot.greet())

   #Get user input

   while True:
       user_input = input("Talk to me: ")
       if user_input.lower() == "stop":
           print("Thanks for talking.")
           break
       response = bot.respond(user_input)


       print(f"Computer: {response}")


if __name__ == "__main__":


   main()
