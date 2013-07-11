import unittest
from command import CommandRequest
from command import CommandQueue
from command import CommandProcessor
from unittest.mock import MagicMock

class CommandRequestTest(unittest.TestCase):
    commandString = "look at me"

    def setUp(self):
        self.commandRequest = CommandRequest(self.commandString, MagicMock())
        

    def testConstructor(self):
        self.assertEqual(self.commandRequest.rawCommand, self.commandString)
        self.assertEqual(self.commandRequest.name, "look")

    def testTimeStamp(self):
        import time
        minTime = time.time()
        commandRequest = CommandRequest(self.commandString, MagicMock())
        myTime = commandRequest._timestamp
        maxTime = time.time()
        self.assertTrue(myTime > minTime)
        self.assertTrue(myTime < maxTime)


class CommandQueueTest(unittest.TestCase):

    def testConstructor(self):
        commandQueue = CommandQueue();
        self.assertIsNotNone(commandQueue.commandQueue)

class CommandProcessorTest(unittest.TestCase):
    commandProcessor = None
    rawRequest = "look at me"

    def setUp(self):
        self.commandProcessor = CommandProcessor()

    def testProcess(self):
        self.assertIsInstance(self.commandProcessor.process("rawRequest", MagicMock()), CommandRequest)
