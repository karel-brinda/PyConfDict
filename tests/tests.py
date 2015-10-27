#! /usr/bin/env python3

import unittest
import sys

sys.path.append("..")

from pyconfdict import PyConfDict

a=PyConfDict({
		"a":"A",
		"b":"B",
	})

b=PyConfDict({
		"a":"z",
		"z":"z",
	})

a_upd_b=PyConfDict({
		"a":"z",
		"b":"B",
		"z":"z",
	})

a_fill_b=PyConfDict({
		"a":"A",
		"b":"B",
		"z":"z",
	})


class TestStringMethods(unittest.TestCase):

	def test_update_exception(self):
		aa=a
		bb=b
		print(aa)
		print(bb)
		with self.assertRaises(ValueError):
			aa.update(bb)

	def test_update(self):
		aa=a
		bb=b
		print(aa)
		print(bb)
		aa.update(bb,allow_new_keys=True)
		self.assertEqual(aa, a_upd_b)

	def test_fill(self):
		aa=a
		bb=b
		print(aa)
		print(bb)
		aa.fill_missing(bb)
		self.assertEqual(aa, a_fill_b)

if __name__ == '__main__':
	unittest.main()

