import pysher
from decouple import config

# Env
API_KEY = config('PUSHER_API_KEY')
SECRET = config('PUSHER_SECRET')
USER_ID = config('PUSHER_USER_ID')
CHANNEL = config('PUSHER_CHANNEL')

class Pusher():

	def __init__(self):

		print("Pusher Init")
		self.pusher = pysher.Pusher(API_KEY, secret=SECRET, cluster="eu", user_data={'user_id': USER_ID})
		self.pusher.connection.bind('pusher:connection_established', self.connect_handler)

	def connect(self):
		
		self.pusher.connect()

	def disconnect(self):
		self.pusher.disconnect()

	def connect_handler(self, data):
		print(data)

		try:
			print ("Connecting...")
			self.channel = self.pusher.subscribe(CHANNEL)
			self.channel.bind('client_set_pixel', client_set_pixel_callback)
			print("Connected")
		except:
			print("Something went wrong...")

	def client_set_pixel_callback(self):
		print("Set pixel")

pusher = Pusher()