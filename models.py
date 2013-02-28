from django.db import models

# Create your models here.

# This database is to store the messages from the sender client when the
# receiver client is not ready to receive the messages.
# Use TextProperty instead of StringProperty for msg because
# the session description can be more than 500 characters.
class Message(models.Model):
  client_id = models.CharField(max_length=30)
  msg = models.CharField(max_length=50)

class Room(models.Model):
  """All the data we store for a room"""
  user1 = models.CharField(max_length=30)
  user2 = models.CharField(max_length=30)
  user1_connected = models.BooleanField()
  user2_connected = models.BooleanField()

