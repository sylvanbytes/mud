from Queue import Queue

class MessageSender:

	messageQueue = None

	def __init__(self):
		self.messageQueue = Queue()

	def addMessage(self, client, message):
		"""
		  Adds the next command to the command queue for latter processing.
		"""
		self.messageQueue.put((client, message))

	def sendMessages(self):
		"""
		Sends some messages that are on the queu.
		"""
		messageTuple = self.messageQueue.get(True)
		client = messageTuple[0]
		message = messageTuple[1]

		client.sendMessage(message)