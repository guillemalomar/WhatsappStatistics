import sys
from FileAnalyzer.FileAnalyzer import FileAnalyzer


# Method called to do a 'clear', just for application visualization purposes
def clean_screen():
    print(chr(27) + "[2J")


def message_header():
    """
    Print method for the header of the application
    :return:
    """
    print "-------------------------- Welcome to the Whatsapp Conversation analyzer app --------------------------\n" \
          "The default path to the data file is this one:\n" \
          "       data/input.txt\n" \
          "If you would like to use another data file, insert the path to it as a parameter of the application.\n"


def process_input(input_file_path):
    """
    # Method used to read the input_data
    :param input_file_path: path to the input file
    :return:
    """
    with open(input_file_path, 'r') as f:
        read_data = f.read()
    return read_data.split(', ')


def message_output():
    """
    Print method for all the available modes
    :return:
    """
    show_modes()
    print " HELP     - Show the initial application message\n" + \
          " MODES    - Show the available modes\n" + \
          " EXIT     - Quit application"


def show_modes():
    """
    Print method for the available data processing modes
    :return:
    """
    print "Available modes:"
    print " 1 - Get Pages by Score Ranking\n" + \
          " 2 - Get Pages by Comment Ranking\n" + \
          " 3 - Get Users by Submissions Score Ranking\n" + \
          " 4 - Get Users by Submissions Quantity"


def check_input(input_var):
    """
    Method to check if the selected method is correct, and to exit if wanted
    :param input_var: user mode selected
    :return: True (Mode to execute) / False (Mode executed or incorrect)
    """
    if input_var.lower() == 'exit':
        print "The application will now end."
        clean_screen()
        raise SystemExit
    elif input_var.lower() == 'modes':
        show_modes()
        return False
    elif input_var.lower() == 'help':
        message_output()
        return False
    elif input_var not in ['1', '2', '3', '4']:
        print "Please enter a valid mode."
        return False
    return True

if __name__ == '__main__':

    clean_screen()
    message_output()

    if len(sys.argv) == 1:
        input_path = 'data/input.txt'
    else:
        input_path = sys.argv[1]
    input_data = process_input(input_path)

    my_file_analyzer = FileAnalyzer(input_data)
    my_file_analyzer.process_input()

    message_header()
    message_output()

    while True:
        correct_input = False
        while not correct_input:
            print "***************************"
            var = raw_input("Please, enter a new mode: ")
            correct_input = check_input(var)
        if var == '1':
            my_file_analyzer.plot_messages_days()
        elif var == '2':
            my_file_analyzer.plot_messages_hours()
        elif var == '3':
            my_file_analyzer.plot_messages_user()
        elif var == '4':
            my_file_analyzer.plot_messages_user_chars()
