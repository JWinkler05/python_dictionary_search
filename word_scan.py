#!/usr/bin/python
import re

class word_search:
    goodList = []

    def __init__(self, fileName, wordSize, chars):
        self.fileName = fileName
        self.wordSize = wordSize
        self.charList = chars

    def search(self):
        regexStr = self._buildRegex(self.wordSize, self.charList)
        try:
            fo = self._openFile(self.fileName, "r")
            with fo as openfileobject:
                for content in openfileobject:
                    content = content.rstrip("\r\n")
                    if self._checkLength(self.wordSize, content) and self._checkRegex(regexStr, content):
                        # print "{0} is a match, adding to array".format(content)
                        self.goodList.append(content)
            if not fo.closed:
                self._closefile(fo)
            print "Process Complete"
            print self.goodList
        except IOError:
            print "Error: can\'t find file or read data"

    def writeList(self):
        fo = self._openFile('results.txt', "w+")
        for word in self.goodList:
            fo.write(word + "\n")
        if not fo.closed:
            self._closefile(fo)


    def _openFile(self, fn, options):
        fileObj = open(fn, options)
        return fileObj

    def _checkLength(self, size, word):
        if (len(word) == size):
            return True

        return False

    def _checkRegex(self, regex, word):
        if re.match(regex, word, re.I) is not None:
            return True

        return False

    def _buildRegex(self, size, cList):
        print "Building REGEX"
        rString = "^"
        for grouping in cList:
            rString += "[" + ",".join(grouping) + "]"
        rString += "$"
        return rString

    def _closefile(self, fileObj):
        fileObj.close()

print "Starting the process"
myList = []
dictionaryFile = 'alpha_dict.txt'

try:
    length = int(raw_input("What is the length of the words you would like to see?: "))
    print "I will now ask you to fill the possible characters for {0} position groups.".format(length)
    for i in range(0, length):
        myList.append(
            set(
                raw_input("Please provide the characters for position " + str(i+1) + " in the word (space delimited): ").split()
            )
        )
    print "The possible characters in their appropriate positions are as follows: "
    print myList

    ws = word_search(dictionaryFile, length, myList)
    ws.search()
    ws.writeList()
    exit()
except ValueError:
    print "The value cannot be null and must be of type integer"
else:
    print "Goodbye!"
    exit()
