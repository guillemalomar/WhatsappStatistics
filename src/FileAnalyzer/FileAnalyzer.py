import re
import pylab as pl
import numpy as np
import math

_date_line = re.compile('[0-9]+/[0-9]+/[0-9]+?')
_message_line = re.compile('[0-9][0-9]:[0-9][0-9] - [\w0-9:+, ]+')


class FileAnalyzer:

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
        self.word = None

    def set_word(self, word):
        self.word = word

    def plot_messages_days(self):
        """
        This method plots the number of messages sent per day
        :return:
        """
        x = np.arange(len(self.messages_day))
        pl.bar(x, self.messages_day.values(), align='center', width=0.5)
        pl.xticks(x, self.messages_day.keys(), rotation=45)
        if max(self.messages_user.values()) > 10000:
            ymax = math.ceil(max(self.messages_day.values()) / 10000.0) * 10000
        elif max(self.messages_day.values()) > 1000:
            ymax = math.ceil(max(self.messages_day.values()) / 1000.0) * 1000
        elif max(self.messages_day.values()) > 100:
            ymax = math.ceil(max(self.messages_day.values()) / 100.0) * 100
        elif max(self.messages_day.values()) > 10:
            ymax = math.ceil(max(self.messages_day.values()) / 10.0) * 10
        else:
            max(self.messages_day.values()) + 1
        pl.ylim(0, ymax)
        pl.title('Messages for each day')
        pl.show()

    def plot_messages_hours(self):
        """
        This method plots the total number of messages sent per hour in any day
        :return:
        """
        lists = sorted(self.messages_hours.items())
        x, y = zip(*lists)
        pl.plot(x, y)
        pl.title('Messages classified by hour')
        pl.show()

    def plot_messages_user(self):
        """
        This method plots the number of messages sent per user
        :return:
        """
        x = np.arange(len(self.messages_user))
        pl.bar(x, self.messages_user.values(), align='center', width=0.5)
        pl.xticks(x, self.messages_user.keys(), rotation=45)
        if max(self.messages_user.values()) > 10000:
            ymax = math.ceil(max(self.messages_user.values()) / 10000.0) * 10000
        elif max(self.messages_user.values()) > 1000:
            ymax = math.ceil(max(self.messages_user.values()) / 1000.0) * 1000
        elif max(self.messages_user.values()) > 100:
            ymax = math.ceil(max(self.messages_user.values()) / 100.0) * 100
        elif max(self.messages_user.values()) > 10:
            ymax = math.ceil(max(self.messages_user.values()) / 10.0) * 10
        else:
            max(self.messages_user.values()) + 1
        pl.ylim(0, ymax)
        pl.title('Messages classified by user')
        pl.show()

    def plot_messages_user_chars(self):
        """
        This method plots the number of chars from all messages sent per user
        :return:
        """
        x = np.arange(len(self.messages_user_chars))
        pl.bar(x, self.messages_user_chars.values(), align='center', width=0.5)
        pl.xticks(x, self.messages_user_chars.keys(), rotation=45)
        if max(self.messages_user_chars.values()) > 100000:
            ymax = math.ceil(max(self.messages_user_chars.values()) / 100000.0) * 100000
        elif max(self.messages_user_chars.values()) > 10000:
            ymax = math.ceil(max(self.messages_user_chars.values()) / 10000.0) * 10000
        elif max(self.messages_user_chars.values()) > 1000:
            ymax = math.ceil(max(self.messages_user_chars.values()) / 1000.0) * 1000
        elif max(self.messages_user_chars.values()) > 100:
            ymax = math.ceil(max(self.messages_user_chars.values()) / 100.0) * 100
        elif max(self.messages_user_chars.values()) > 10:
            ymax = math.ceil(max(self.messages_user_chars.values()) / 10.0) * 10
        else:
            max(self.messages_user_chars.values()) + 1
        pl.ylim(0, ymax)
        pl.title('Characters classified by user')
        pl.show()

    def plot_messages_user_word(self):
        """
        This method plots the number of chars from all messages sent per user
        :return:
        """
        x = np.arange(len(self.messages_user_word))
        pl.bar(x, self.messages_user_word.values(), align='center', width=0.5)
        pl.xticks(x, self.messages_user_word.keys(), rotation=45)
        if max(self.messages_user_word.values()) > 100000:
            ymax = math.ceil(max(self.messages_user_word.values()) / 100000.0) * 100000
        elif max(self.messages_user_word.values()) > 10000:
            ymax = math.ceil(max(self.messages_user_word.values()) / 10000.0) * 10000
        elif max(self.messages_user_word.values()) > 1000:
            ymax = math.ceil(max(self.messages_user_word.values()) / 1000.0) * 1000
        elif max(self.messages_user_word.values()) > 100:
            ymax = math.ceil(max(self.messages_user_word.values()) / 100.0) * 100
        elif max(self.messages_user_word.values()) > 10:
            ymax = math.ceil(max(self.messages_user_word.values()) / 10.0) * 10
        else:
            max(self.messages_user_word.values()) + 1
        pl.ylim(0, ymax)
        pl.title('Times every user has said a given word')
        pl.show()

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
                    self.messages_day[line] = self.messages_day.get(line, 0) + 1
                else:
                    if 'El codi de seguretat de ' not in line and \
                       ' ha afegit ' not in line and \
                       ' marxa' not in line and \
                       'a aquest grup ara estan assegurats amb' not in line and \
                       'ha creat el grup' not in line and \
                       'Has canviat ' not in line and \
                       'ha canviat ' not in line and \
                       ' expulsat ' not in line and \
                       'aquest xat i trucades ara estan assegurats' not in line and \
                       ' t\'ha expulsat' not in line and \
                       ' t\'ha afegit' not in line:
                        n = _message_line.match(line)
                        if n is not None:
                            hour = line.split(':')[0]
                            self.messages_hours[hour] = self.messages_hours.get(hour, 0) + 1
                            user = line.split(':')[1].split(' - ')[1]
                            if '(' in user:
                                user = user.split('(')[0]
                            self.messages_user[user] = self.messages_user.get(user, 0) + 1
                            message = line.split(':')[-1]
                            self.messages_user_chars[user] = self.messages_user_chars.get(user, 0) + len(message)
                            self.messages_user_word[user] = self.messages_user_word.get(user, 0)
                            if str(self.word).lower() in message.lower():
                                self.messages_user_word[user] = self.messages_user_word[user] + 1
