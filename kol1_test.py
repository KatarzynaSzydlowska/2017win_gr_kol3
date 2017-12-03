# 4poznanski
import unittest
import kol1


class MyTest(unittest.TestCase):
    def setUp(self):
        self.client = kol1.Client('Nowak')
        self.client2 = kol1.Client('Kowal')
        self.client2.input(100)
        self.bank = kol1.Bank()
        self.bank.addClient(self.client)
        self.bank.addClient(self.client2)

    def test_bank_init(self):
        self.assertIsNotNone(self.bank)

    def test_client_name(self):
        self.assertEquals(self.client.name, 'Nowak')

    def test_client_default_cash(self):
        self.assertEquals(self.client.cash, 0)

    def test_add_client(self):
        self.assertTrue(self.client2 in self.bank.clients)

    def test_input(self):
        self.client.input(100)
        self.assertEqual(self.client.cash, 100)

    def test_withdraw(self):
        self.client2.withdraw(50)
        self.assertEqual(self.client2.cash, 50)

    def test_transfer(self):
        self.bank.transfer(self.client2, self.client, 10)
        self.assertEquals(self.client2.cash, 90)
        self.assertEquals(self.client.cash, 10)

    def test_input_wrong_value(self):
        self.client2.input(-100)
        self.assertNotEqual(self.client2.cash, 0)

    def test_withdraw_wrong_value(self):
        self.client2.withdraw(150)
        self.assertNotEqual(self.client2.cash, -50)

    def test_transfer_wrong_value(self):
        self.bank.addClient(self.client2)
        self.bank.transfer(self.client, self.client2, -10)
        self.assertNotEquals(self.client.cash, 110)
        self.assertNotEquals(self.client2.cash, -10)

    def test_transfer_more_than_in_account(self):
        self.bank.addClient(self.client2)
        self.bank.transfer(self.client, self.client2, 1000)
        self.assertNotEquals(self.client.cash, -900)
        self.assertNotEquals(self.client2.cash, 1000)

    def test_client_not_in_bank(self):
        self.client3 = kol1.Client('Kowalski')
        self.assertFalse(self.client3 in self.bank.clients)
