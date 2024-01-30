import pyfiglet

def generate_ascii(text, font="standard"):
    return pyfiglet.figlet_format(text, font=font)

def main():
    text = input("Enter the text you want to convert to ASCII art: ")
    font = input("Enter the font (optional, press enter for default): ")
    if not font.strip():
        font = "standard"  # default font
    ascii_art = generate_ascii(text, font)
    print(ascii_art)

if __name__ == "__main__":
    main()

