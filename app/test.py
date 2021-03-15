import unittest

from app import app 

class TestAPI(unittest.TestCase):

	
	def setUp(self):
		self.app = app.test_client()
		

	def test_welcomepage(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code,200)

	def test_ressource(self):
		response_ressource = self.app.get("/Ressource/")
		self.assertEqual(response_ressource.status_code,200)
	def test_ressource_post(self):
		pass
		

	

if __name__ == "__main__":
	unittest.main()