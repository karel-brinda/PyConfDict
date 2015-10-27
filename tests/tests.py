#! /usr/bin/env python3

import unittest
import sys
import copy
import collections

sys.path.append("..")

from pyconfdict import PyConfDict

a=PyConfDict(collections.OrderedDict(
		[
			("a","A"),
			("b","B"),
		]
	))

b=PyConfDict(collections.OrderedDict(
		[
			("a","z"),
			("z","z"),
		]
	))

a_upd_b=PyConfDict(collections.OrderedDict(
		[
			("a","z"),
			("b","B"),
			("z","z"),
		]
	))

a_fill_b=PyConfDict(collections.OrderedDict(
		[
			("a","A"),
			("b","B"),
			("z","z"),
		]
	))


class TestStringMethods(unittest.TestCase):

	def test_update_exception(self):
		aa=copy.deepcopy(a)
		bb=copy.deepcopy(b)
		with self.assertRaises(ValueError):
			aa.update(bb)

	def test_update(self):
		aa=copy.deepcopy(a)
		bb=copy.deepcopy(b)
		aa.update(bb,allow_new_keys=True)
		self.assertEqual(aa, a_upd_b)

	def test_fill(self):
		aa=copy.deepcopy(a)
		bb=copy.deepcopy(b)
		aa.fill_missing(bb)
		self.assertEqual(aa, a_fill_b)

if __name__ == '__main__':
	unittest.main()

