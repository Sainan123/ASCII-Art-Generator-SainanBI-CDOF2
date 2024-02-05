import pyfiglet

def generate_ascii(text, font="standard"):
    return pyfiglet.figlet_format(text, font=font)

def add_border(ascii_art, border_type="*"):
    """Adds a border around the ASCII art."""
    lines = ascii_art.split("\n")
    width = max(len(line) for line in lines)
    border_line = border_type * (width + 4)

    bordered_art = border_line + "\n"
    for line in lines:
        bordered_art += f"{border_type} {line.ljust(width)} {border_type}\n"
    bordered_art += border_line

    return bordered_art

def main():
    text = input("Enter the text you want to convert to ASCII art: ")
    font = input("Enter the font (optional, press enter for default): ")
    if not font.strip():
        font = "standard"  # default font

    ascii_art = generate_ascii(text, font)

    # Ask user if they want to add a border
    add_border_option = input("Do you want to add a border? (yes/no): ").lower()
    if add_border_option == "yes":
        border_type = input("Enter a single character for the border (e.g., *, #, @): ")
        ascii_art = add_border(ascii_art, border_type)

    print("\n" + ascii_art)

if __name__ == "__main__":
    main()

