from queue import Queue
from common.enum import enum
from client import Client


class CommandProcessor():

    def process(self, rawRequest, client):        
        commandRequest = CommandRequest(rawRequest, client = client)
        return commandRequest;


class CommandQueue():
    """
      Holds the raw commands in a queue for later processing.
    """
    commandQueue = None
    _commandProcessor = None

    def __init__(self, commandProcessor=CommandProcessor()):
        self.commandQueue = Queue()
        self._commandProcessor = commandProcessor;

    def addCommand(self, client, commandString):
        """
          Adds the next command to the command queue for latter processing. We add 
          the client and commandString instead of wrapping them because
          the commandString has not been evaluated in any way.
        """
        self.commandQueue.put((client, commandString))

    def nextCommand(self):
        client, rawCommand = self.commandQueue.get(True)
        while client.isLinkdead() :  
            client, rawCommand = self.commandQueue.get(True)
            
        return self._commandProcessor.process(rawCommand, client)

class CommandRequest():
    """
      An object that holds the raw request string and other basic information about the request.
    """
    rawCommand = None
    _name = None
    client = None
    _timestamp = None

    def __init__(self, rawCommand, client=None):
        self.rawCommand = rawCommand
        self.client = client
        import time
        self._timestamp = time.time()
    
    @property
    def name(self):
        if self._name is None:
            self._name = self.rawCommand.split(" ", 1)[0]
        return self._name






