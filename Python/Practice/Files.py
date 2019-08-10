import os
import re
import sys
import argparse


class TextSearch:
    def __init__(self, string2, path1, i=None):
        self.path1 = path1
        self.string1 = string2
        self.i = i
        if self.i:
            string2 = string2.lower()
            self.string2 = re.compile(string2)

    def txt_search(self):
        file_number = 0
        files = [f for f in os.listdir(self.path1) if os.path.isfile(self.path1 + "\\" + f)]
        for file in files:
            file_t = open(self.path1 + "\\" + file)
            file_text = file_t.read()
            if self.i:
                file_text = file_text.lower()
            file_t.close()
            if re.search(self.string2, file_text):
                print("The text " + self.string1 + " found in ", file)
            file_number = file_number + 1

        print("total files are ", file_number)

ts = TextSearch("procedure", "D:\\Projects\\content-feeds\\unittest\\EDD\\MetricsDashboard\\MeaningfulVerificationContacts", 1)

ts.txt_search()