"""
server/message.py

Implementation of the "Message" class, a backend way of connecting a user's
message to relevant metadata.
"""

class Message:
    def __init__(self, user, text, timestamp=None):
        self.user = user
        self.text = text
        self.timestamp = timestamp

    def to_str(self):
        return '[{user}] {msg}'.format(user=self.user, msg=self.text)
