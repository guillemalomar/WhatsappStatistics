import sys
from FileAnalyzer.FileAnalyzer import FileAnalyzer
import argparse


def clean_screen():
    """
    Method called to do a 'clear', just for application visualization purposes
    :return:
    """
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
    print " 1 - Plot messages send per day\n" + \
          " 2 - Plot messages send per hour for all days\n" + \
          " 3 - Plot messages sent by each user\n" + \
          " 4 - Plot characters sent by each user\n" + \
          " 5 - Plot times each user said a specific word\n" + \
          " 6 - Show expulsions history"


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
    elif input_var not in ['1', '2', '3', '4', '5', '6']:
        print "Please enter a valid mode."
        return False
    return input_var

if __name__ == '__main__':

    clean_screen()

    # Arguments are taken from command line
    parser = argparse.ArgumentParser(description='Whatsapp Statistics',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--input-file', action="store", dest="input_file",
                        help="Path to the input file",
                        default="data/input.txt", type=str)
    args = parser.parse_args()
    input_path = args.input_file

    message_output()

    input_data = process_input(input_path)

    message_header()
    message_output()

    while True:
        correct_input = False
        while not correct_input:
            print "***************************"
            var = raw_input("Please, enter a new mode: ")
            correct_input = check_input(var)

        my_file_analyzer = FileAnalyzer(input_data)
        if var == '1':
            if my_file_analyzer.messages_day == {}:
                my_file_analyzer.process_input()
            my_file_analyzer.plot_messages_days()
        elif var == '2':
            if my_file_analyzer.messages_hours == {}:
                my_file_analyzer.process_input()
            my_file_analyzer.plot_messages_hours()
        elif var == '3':
            if my_file_analyzer.messages_user == {}:
                my_file_analyzer.process_input()
            my_file_analyzer.plot_messages_user()
        elif var == '4':
            if my_file_analyzer.messages_user_chars == {}:
                my_file_analyzer.process_input()
            my_file_analyzer.plot_messages_user_chars()
        elif var == '5':
            word_to_search = raw_input("Please, enter a word to be searched: ")
            my_file_analyzer.set_word(word_to_search)
            my_file_analyzer.process_input()
            my_file_analyzer.plot_messages_user_word()
        elif var == '6':
            if my_file_analyzer.expulsions == {}:
                my_file_analyzer.process_input()
            my_file_analyzer.show_expulsions()
