import unittest
from main import command_l, documents, directories

list_of_documents = [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}]
command_l_result = ['passport "2207 876234" "Василий Гупкин"']


class TestCommands(unittest.TestCase):

    def test_command_l(self):
        self.assertEqual(command_l_result, command_l(list_of_documents))

    def test_command_a_docs(self):
        self.assertIn({'type': 'passport', 'number': '1234', 'name': 'Tatiana'}, documents)
        self.assertEqual(['1234'], directories['3'])


if __name__ == '__main__':
    unittest.main()

