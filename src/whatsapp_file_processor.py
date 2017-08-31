import sys
from FileAnalyzer.FileAnalyzer import FileAnalyzer


# Method called to do a 'clear', just for application visualization purposes
def clean_screen():
    print(chr(27) + "[2J")



# Print method for the first message
def presentation():
    print "-------------------------- Welcome to the Whatsapp Conversation analyzer app --------------------------\n" \
          "The default path to the data file is this one:\n" \
          "       data/input.txt\n" \
          "If you would like to use another data file, insert the path to it as a parameter of the application.\n"


# Method used to read the input_data
def process_input(input_path):
    with open(input_path, 'r') as f:
        read_data = f.read()
    return read_data.split(', ')


if __name__ == '__main__':

    clean_screen()
    presentation()

    if len(sys.argv) == 1:
        input_path = 'data/input.txt'
    else:
        input_path = sys.argv[1]
    input_data = process_input(input_path)

    my_file_analyzer = FileAnalyzer(input_data)
    my_file_analyzer.process_input()
