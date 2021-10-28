# unit test
# TDD Test Driven Development

# actually, you should just read https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936

# SERIOUSLY BRO JUST READ https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936

from mydict import Dict

d = Dict(a=1,b=2)
d['a']
class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d,a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty



# setUp and tearDown

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

# SERIOUSLY BRO JUST READ https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936

