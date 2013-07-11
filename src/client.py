class Client:

    commandQueue = None
    messageSender = None

    def __init__(self, messageSender = None, commandQueue = None):
        self.commandQueue = commandQueue
        self.messageSender = messageSender

    def onMessageReceived(self, message):
        """
        The client has received a message from some source that could change
        the game state. This message could have come from some client at the end 
        of some network connection.
        """
        self.commandQueue.addCommand(message)

    def onMessageSent(self, message):
        """
        The system has a message that needs to be sent to a source to notify it of state change.
        This could some remote client connected via a network connection.
        """
        pass

    def sendMessage(self, message):
        self.messageSender.addMessage(self, message)

    def isLinkdead(self):
        return False;
    
    
