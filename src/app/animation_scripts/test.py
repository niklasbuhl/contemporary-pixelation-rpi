from multiprocessing import Process
import time




class TestAnimation(Process):
	def __init__(self, conn, matrix):
		super(TestAnimation, self).__init__()
		self.conn = conn
		self.target_fps = 1
		self.matrix = matrix
		print("TestAnimation __init__")
	
	def setup():
		pass
	
	def run(self):
		print("TestAnimation run")
		# Loop
		while True:
			# Receive any messages

			while self.conn.poll():

				msg = self.conn.recv()
				print(msg)
				if msg == "stop":
					self.conn.close()
					print("exited gracefully")
					return

			start = time.time()
			print(f"start: {start}")
			self.draw()
			end = time.time()
			print(f"end: {end}")

			# Calculate fps
			remaining_frame_time = (1/self.target_fps) - (end - start)
			print(remaining_frame_time)

			# Wait the rest of the fps
			if remaining_frame_time:
				time.sleep(remaining_frame_time)

	def draw(self):
		print("draw")



