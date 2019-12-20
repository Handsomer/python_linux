from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import mymodule

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol, host, domain = 'http', 'www', 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)
        with patch('sys.stdout',  new = StringIO()) as fake_out:
            mymodule.urlPrint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)

if __name__ == "__main__":
    test_obj = TestURLPrint()
    test_obj.test_url_gets_to_stdout()
