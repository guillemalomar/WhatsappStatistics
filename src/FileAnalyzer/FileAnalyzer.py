import re
import pylab as pl
import numpy as np
import math

_date_line = re.compile('[0-9]+/[0-9]+/[0-9]+?')
_message_line = re.compile('[0-9][0-9]:[0-9][0-9] - [\w+,.!?()"#\[\] ]+:[\w+,.!?()"#\[\] ]+')
_message_line2 = re.compile('[\w.?!\-()"#\[\] ]+')


class FileAnalyzer:

    _reserved_messages = ['El codi de seguretat de ',
                          ' ha afegit ',
                          ' marxa',
                          'ha creat el grup',
                          'Has canviat ',
                          'ha canviat ',
                          'a aquest grup ara estan assegurats amb',
                          'aquest xat i trucades ara estan assegurats',
                          ' t\'ha expulsat',
                          ' expulsat ',
                          ' t\'ha afegit']

    def __init__(self, input_data):
        """
        File Analyzer initializer
        :param input_data: data in input file
        """
        self.data = input_data
        self.messages_day = {}
        self.messages_hours = {}
        self.messages_user = {}
        self.messages_user_chars = {}
        self.messages_user_word = {}
        self.expulsions = {}
        self.expulsions_by_user = {}
        self.word = None

    def set_word(self, word):
        """
        Assigns a given word to the FileAnalyzer
        :param word: specified word by the user
        :return:
        """
        self.word = word

    def plot_messages_days(self):
        """
        This method plots the number of messages sent per day
        :return:
        """
        sorted_keys = []
        sorted_values = []
        values = self.messages_day.values()
        for key in sorted(self.messages_day.keys()):
            for value in self.messages_day.values():
                if self.messages_day[key] == value and value in values:
                    sorted_keys.append(key)
                    sorted_values.append(value)
                    values.remove(value)
        x = np.arange(len(self.messages_day))
        pl.bar(x, sorted_values, align='center', width=0.5)
        pl.xticks(x, sorted_keys, rotation=45)
        y_max = FileAnalyzer.calculate_max(self.messages_day)
        pl.ylim(0, y_max)
        pl.axis('auto')
        pl.title('Messages for each day')
        pl.show()

    def plot_messages_hours(self):
        """
        This method plots the total number of messages sent per hour in any day
        :return:
        """
        lists = sorted(self.messages_hours.items())
        x, y = zip(*lists)
        pl.plot(x, y, marker='o')
        pl.title('Messages classified by hour')
        pl.show()

    def plot_messages_user(self):
        """
        This method plots the number of messages sent per user
        :return:
        """
        sorted_values = []
        keys = self.messages_user.keys()
        for value in sorted(self.messages_user.values(), reverse=True):
            for key in self.messages_user.keys():
                if self.messages_user[key] == value and key in keys:
                    sorted_values.append(key)
                    keys.remove(key)
        x = np.arange(len(self.messages_user))
        pl.bar(x, sorted(self.messages_user.values(), reverse=True), align='center', width=0.5)
        pl.xticks(x, sorted_values, rotation=45)
        y_max = FileAnalyzer.calculate_max(self.messages_user)
        pl.ylim(0, y_max)
        pl.axis('auto')
        pl.title('Messages classified by user')
        pl.show()

    def plot_messages_user_chars(self):
        """
        This method plots the number of chars from all messages sent per user
        :return:
        """
        sorted_values = []
        keys = self.messages_user_chars.keys()
        for value in sorted(self.messages_user_chars.values(), reverse=True):
            for key in self.messages_user_chars.keys():
                if self.messages_user_chars[key] == value and key in keys:
                    sorted_values.append(key)
                    keys.remove(key)
        x = np.arange(len(self.messages_user_chars))
        pl.bar(x, sorted(self.messages_user_chars.values(), reverse=True), align='center', width=0.5)
        pl.xticks(x, sorted_values, rotation=45)
        y_max = FileAnalyzer.calculate_max(self.messages_user_chars)
        pl.ylim(0, y_max)
        pl.axis('auto')
        pl.title('Characters classified by user')
        pl.show()

    def plot_messages_user_word(self):
        """
        This method plots the number of chars from all messages sent per user
        :return:
        """
        sorted_values = []
        keys = self.messages_user_word.keys()
        for value in sorted(self.messages_user_word.values(), reverse=True):
            for key in self.messages_user_word.keys():
                if self.messages_user_word[key] == value and key in keys:
                    sorted_values.append(key)
                    keys.remove(key)
        x = np.arange(len(self.messages_user_word))
        pl.bar(x, sorted(self.messages_user_word.values(), reverse=True), align='center', width=0.5)
        pl.xticks(x, sorted_values, rotation=45)
        y_max = FileAnalyzer.calculate_max(self.messages_user_word)
        pl.ylim(0, y_max)
        pl.axis('auto')
        pl.title('Times every user has said ' + str(self.word))
        pl.show()

    @staticmethod
    def calculate_max(dictionary):
        """
        Method to calculate the plot height from a given dictionary
        :param dictionary: obtained from processed data
        :return:
        """
        max_val = max(dictionary.values())
        if max_val > 100000:
            y_max = math.ceil(max_val / 100000.0) * 100000
        elif max_val > 10000:
            y_max = math.ceil(max_val / 10000.0) * 10000
        elif max_val > 1000:
            y_max = math.ceil(max_val / 1000.0) * 1000
        elif max_val > 100:
            y_max = math.ceil(max_val / 100.0) * 100
        elif max_val > 10:
            y_max = math.ceil(max_val / 10.0) * 10
        else:
            y_max = max_val + 1
        return y_max

    @staticmethod
    def increase_statistic(dictionary, key, to_increase=1):
        """
        Method to simplify process_input method
        :param dictionary: dictionary to be increased
        :param key: position in the dictionary to be increased
        :param to_increase: value to increase
        :return:
        """
        dictionary[key] = dictionary.get(key, 0) + to_increase

    def show_expulsions(self):
        """
        Method to show expulsions history
        :return:
        """
        if len(self.expulsions) == 0:
            print "Nobody has been expulsed"
        else:
            print "Expulser - Expulsed - Times expulsed ############"
            for key, value in self.expulsions.iteritems():
                print str(key[0]) + ' - ' + str(key[1]) + ' - ' + str(value)
            print "Most prolific expulsers #########################"
            for key, value in self.expulsions_by_user.iteritems():
                print str(key) + " - " + str(value) + " expulsions"

    @staticmethod
    def process_date(date):
        """
        Method that processes a date in order to be able to
        order them in method plot_messages_days
        :param date: a message date
        :return:
        """
        if int(date[0]) < 10 or int(date[1]) < 10:
            final_line = ''
            final_line += date[2]
            if int(date[1]) < 10:
                final_line += '0'
            final_line += date[1]
            if int(date[0]) < 10:
                final_line += '0'
            final_line += date[0]
        else:
            final_line = date[2] + date[1] + date[0]
        return final_line


    def process_input(self):
        """
        This method processes the input data and accumulates all interesting
        information in order to be able to plot it afterwards
        :return:
        """
        for row in self.data:
            lines = row.split('\n')
            for line in lines:
                m = _date_line.match(line)
                if m is not None and ']' not in line:
                    split_line = line.split('/')
                    final_line = FileAnalyzer.process_date(split_line)
                    FileAnalyzer.increase_statistic(self.messages_day, int(final_line))
                else:
                    if True not in [x in line for x in FileAnalyzer._reserved_messages]:
                        user = ''
                        n = _message_line.match(line)
                        if n is not None:
                            hour = line.split(':')[0]
                            FileAnalyzer.increase_statistic(self.messages_hours, int(hour))

                            user = line.split(':')[1].split(' - ')[1]
                            if '(' in user:
                                user = user.split('(')[0]
                            FileAnalyzer.increase_statistic(self.messages_user, user)

                            message = line.split(':')[-1]
                            FileAnalyzer.increase_statistic(self.messages_user_chars, user, len(message))

                            print message
                            if message == '\<Mitjans omesos\>':
                                print "message:", message

                            if str(self.word).lower() in message.lower():
                                FileAnalyzer.increase_statistic(self.messages_user_word, user)
                        else:
                            o = _message_line2.match(line)
                            if o is not None:
                                if user != '':
                                    FileAnalyzer.increase_statistic(self.messages_user, user)

                                    FileAnalyzer.increase_statistic(self.messages_user_chars, len(line))

                                    if str(self.word).lower() in message.lower():
                                        FileAnalyzer.increase_statistic(self.messages_user_word, user)
                    else:
                        if ' expulsat' in line:
                            line = line.split(' - ')[1]
                            if 't\'ha expulsat' in line:
                                expulser = line.split(' t\'ha expulsat')[0]
                                expulsed = 'me'
                                FileAnalyzer.increase_statistic(self.expulsions_by_user, expulser)
                                FileAnalyzer.increase_statistic(self.expulsions, (expulser, expulsed))
                            elif  ' ha expulsat a ' in line:
                                expulser = line.split(' ha expulsat a ')[0]
                                expulsed = line.split(' ha expulsat a ')[-1]
                                FileAnalyzer.increase_statistic(self.expulsions_by_user, expulser)
                                FileAnalyzer.increase_statistic(self.expulsions, (expulser, expulsed))
