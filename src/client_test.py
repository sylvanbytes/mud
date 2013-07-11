import unittest
from unittest.mock import Mock
from command import CommandQueue
from client import Client

class ClientTest(unittest.TestCase):
	client = None
	commandQueue = None
	def setUp(self):
		self.commandQueue = Mock()
		self.client = Client(commandQueue = self.commandQueue)

	def testConstructor(self):		
		self.assertEqual(self.client.commandQueue, self.commandQueue)

	def testIsLinkdead(self):
		self.assertFalse(self.client.isLinkdead())

