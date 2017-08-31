



class FileAnalyzer:

    def __init__(self, input_data):
        self.data = input_data

    def process_input(self): 
        for row in self.data:
            lines = row.split('\n')
            for line in lines:
                print "line:", line
