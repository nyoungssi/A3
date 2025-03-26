#Comp1020 A3
#by Nayoung Lim

from ChatBot import ChatBot

def main():
   # Create a ChatBot object
   # with specified files and default response
   bot = ChatBot("greetings.txt", "responses.txt", "Tell me more.")
   print(bot.greet())

   #Get user input
   while True:
       user_text = input("Talk to me something!: ")
       if user_text.lower() == "stop":
           print("Thanks for talking.")
           break
       response = bot.respond(user_text)

       print(f"Computer: {response}")

if __name__ == "__main__":

    main()
