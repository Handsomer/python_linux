#coding:utf-8

#unittest.mock.patch() 函数被用作一个上下文管理器，
#使用 StringIO 对象来代替 sys.stdout . fake_out 变量是在该进程中被创建的模拟对象。
#在with语句中使用它可以执行各种检查。当with语句结束时，patch 会将所有东西恢复到测试开始前的状态。
def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)

from io import StringIO
from unittest import TestCase
from unittest.mock import patch

class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            urlprint(protocol, host, domain)
            ret_value = self.assertEqual(fake_out.getvalue(), expected_url)

test_obj = TestURLPrint()
test_obj.test_url_gets_to_stdout()
