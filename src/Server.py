__author__ = 'M. C. Skinner'
import threading
from MessageSender import MessageSender
from command import CommandQueue
from client import Client
import logging
import sys

class Server:
    messageSender = None

    def __init__(self):
        self.messageSender = MessageSender()

    def start(self):
        self.__initalizeServer()
        pass

    def stop(self):
        pass

    def restart(self):
        pass



    def __initalizeServer(self):
        self.__initalizeLogging()
        commandHandler = CommandQueue()
        sendMessageThread = messageSenderThread(self.messageSender)
        sendMessageThread.start()
        readMessageThread = messageReaderThread(commandHandler, MessageSource())
        readMessageThread.start()
        processMessagethread = messageProcessingThread(commandHandler)
        processMessagethread.start()


    def __initalizeLogging(self):
        logger = logging.getLogger('mud')
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler('debug.log')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)


class messageSenderThread(threading.Thread):
    """
    A thread that send messages to the client. Typically this will be a remote client through
    a network connection.
    """

    def __init__(self, messageSender):
        super(messageSenderThread, self).__init__()
        self.messageSender = messageSender

    def run(self):
        logging.getLogger("mud.messageSenderThread").info("Starting message sender thread")
        while True:
            self.messageSender.sendMessages()


class messageReaderThread(threading.Thread):
    """
    A thread the reads messages from the client that could change the state of the server.
    """
    commandHandler = None
    messageSource = None
    logger = None

    def __init__(self, commandHandler=None, messageSource=None):
        super(messageReaderThread, self).__init__()
        self.commandHandler = commandHandler
        self.messageSource = messageSource
        self.logger = logging.getLogger("mud.messageReadeThread")

    def run(self):
        self.logger.info("Ready to accept input")
        while True:
            client, inputString = self.messageSource.nextMessage()
            self.logger.info("Got input...")
            self.commandHandler.addCommand(client, inputString)

class messageProcessingThread(threading.Thread):
    """
    A thread that checks to see whether there is any input sitting around that must
    be processed that could mutate state.
    """
    def __init__(self, commandHandler=None):
        super(messageProcessingThread, self).__init__()
        self.commandHandler = commandHandler
        self.logger = logging.getLogger("mud.messageProcessingThread")

    def run(self):
        while True:
            commandRequest = self.commandHandler.nextCommand()
            self.logger.info("Processing command: "+commandRequest.rawCommand.rstrip())
            commandRequest.client.sendMessage("I got your message")


class MessageSource:
    def nextMessage(self):
        line = sys.stdin.readline()
        return commandLineClient, line

server = Server()
commandLineClient = Client(messageSender = server.messageSender)

server.start()

