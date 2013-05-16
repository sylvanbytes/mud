from Queue import Queue
from common.enum import enum

class CommandQueue():
    commandQueue = None

    def __init__(self):
        self.commandQueue = Queue()

    def addCommand(self, client, commandString):
        """
            Adds the next command to the command queue for latter processing.
          """
        self.commandQueue.put((client, commandString))

    def nextCommand(self):
        return self.commandQueue.get(True)


Tokens = enum('NUMBER', 'COMMAND', 'PREPOSITION', 'ARTICLE', 'ORDINAL')

class CommandProcessor():
    def processCommand(self, client, commandString):
        tokens = self.__tokenizeCommand(commandString)
        command = self.__findCommand(tokens)

    def __tokenizeCommand(self, commandString):
        parts = commandString.split(" ", 1)


    def __findCommand(self, tokens):
        pass
