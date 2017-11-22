#4poznanski
import unittest
import kol1

class MyTest(unittest.TestCase):
    
    #def setUp(self):

    def test_Client(self):
        client_name = "Nowak"
        client = kol1.Client(client_name)
        self.assertIsNotNone(client)   

    def test_client_name(self):
        client_name = "Nowak"
        client = kol1.Client(client_name)
        self.assertEqual(client.name,"Nowak")

    def test_Bank(self):
        bank = kol1.Bank()
        self.assertIsNotNone(bank)
    
    def test_add_client(self):
        bank = kol1.Bank()
        client = kol1.Client("Nowak")
        bank.addClient(client)
        #assert len(bank.clients[client]) == 0, "not empty"


