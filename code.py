import random
import webbrowser
from colorama import Fore, Style

def generate_giftcode_link():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890-_"
    link = "https://t.me/giftcode/"
    for i in range(27):
        link += random.choice(characters)
    return link

class NumberGeneratorApp:
    def __init__(self):
        self.generated_links = []

    def generate(self):
        self.generated_links = [generate_giftcode_link() for _ in range(10)]
        print("Links generated!")

    def show_links(self):
        print(Fore.GREEN + "\n".join(self.generated_links) + Style.RESET_ALL)

    def open_link(self, link_number):
        if 0 < link_number <= len(self.generated_links):
            webbrowser.open(self.generated_links[link_number - 1])

    def open_all_links(self):
        for link in self.generated_links:
            webbrowser.open(link)
        print("All links opened in browser!")

if __name__ == "__main__":
    app = NumberGeneratorApp()
    while True:
        print("\nMain Menu:")
        print("1. Generate Links")
        print("2. Show Links")
        print("3. Open a Link")
        print("4. Open All Links")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            app.generate()
        elif choice == "2":
            app.show_links()
        elif choice == "3":
            link_number = int(input("Enter the number of the link to open: "))
            app.open_link(link_number)
        elif choice == "4":
            if app.generated_links:
                app.open_all_links()
            else:
                print("Please generate links first!")
        elif choice == "5":
            print("Exiting...")
            break
        elif choice == "6":
            print("developed by tymko on github. credits to Nureop. basic 0.1% working gui generator of tg premium.")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
