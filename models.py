from django.db import models

# Create your models here.

# This database is to store the messages from the sender client when the
# receiver client is not ready to receive the messages.
# Use TextProperty instead of StringProperty for msg because
# the session description can be more than 500 characters.
class Message(models.Model):
    client_id = models.CharField(max_length=30)
    msg = models.TextField()

class Room(models.Model):
    """All the data we store for a room"""
    user1 = models.CharField(max_length=30)
    user2 = models.CharField(max_length=30)
    user1_connected = models.BooleanField()
    user2_connected = models.BooleanField()

    def __unicode__(self):
        str = '['
        if self.user1:
            str += "%s-%r" % (self.user1, self.user1_connected)
        if self.user2:
            str += ", %s-%r" % (self.user2, self.user2_connected)
        str += ']'
        return str

    def get_occupancy(self):
        occupancy = 0
        if self.user1:
            occupancy += 1
        if self.user2:
            occupancy += 1
        return occupancy

    def get_other_user(self, user):
        if user == self.user1:
            return self.user2
        elif user == self.user2:
            return self.user1
        else:
            return None

    def has_user(self, user):
        return (user and (user == self.user1 or user == self.user2))

    def add_user(self, user):
        if not self.user1:
            self.user1 = user
        elif not self.user2:
            self.user2 = user
        else:
            raise RuntimeError('room is full')
        self.put()

    def remove_user(self, user):
        delete_saved_messages(make_client_id(self, user))
        if user == self.user2:
            self.user2 = None
            self.user2_connected = False
        if user == self.user1:
            if self.user2:
                self.user1 = self.user2
                self.user1_connected = self.user2_connected
                self.user2 = None
                self.user2_connected = False
            else:
                self.user1 = None
                self.user1_connected = False
        if self.get_occupancy() > 0:
            self.put()
        else:
            self.delete()

    def set_connected(self, user):
        if user == self.user1:
            self.user1_connected = True
        if user == self.user2:
            self.user2_connected = True
        self.put()

    def is_connected(self, user):
        if user == self.user1:
            return self.user1_connected
        if user == self.user2:
            return self.user2_connected

