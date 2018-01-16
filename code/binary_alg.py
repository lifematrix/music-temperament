

import os
import logging

class DigitOp:
	# _table = [ 
	# 	['1', '1', ['2']],
	# 	['1', '2', ['3']],
	# 	['1', '3', ['4']],
	# 	['1', '4', ['5']],
	# 	['1', '5', ['6']],
	# 	['1', '6', ['7']],
	# 	['1', '7', ['8']],
	# 	['1', '8', ['9']],
	# 	['1', '9', ['1', '0']],
	# 	['2', '2', ['4']],
	# 	['2', '3', ['5']],
	# 	['2', '4', ['6']],
	# 	['2', '5', ['7']],
	# 	['2', '6', ['8']],
	# 	['2', '7', ['9']],
	# 	['2', '8', ['1', '0']],
	# 	['2', '9', ['1', '1']],
	# 	['3', '3', ['6']],
	# 	['3', '4', ['7']],
	# 	['3', '5', ['8']],
	# 	['3', '6', ['9']],
	# 	['3', '7', ['1', '0']],
	# 	['3', '8', ['1', '1']],
	# 	['3', '9', ['1', '2']],
	# 	['4', '4', ['8']],
	# 	['4', '5', ['9']],
	# 	['4', '6', ['1', '0']],
	# 	['4', '7', ['1', '1']],
	# 	['4', '8', ['1', '2']],
	# 	['4', '9', ['1', '3']],
	# 	['5', '5', ['1', '0']],
	# 	['5', '6', ['1', '1']],
	# 	['5', '7', ['1', '2']],
	# 	['5', '8', ['1', '3']],
	# 	['5', '9', ['1', '4']],
	# 	['6', '6', ['1', '2']],
	# 	['6', '7', ['1', '3']],
	# 	['6', '8', ['1', '4']],
	# 	['6', '9', ['1', '5']],
	# 	['7', '7', ['1', '4']],
	# 	['7', '8', ['1', '5']],
	# 	['7', '9', ['1', '6']],
	# 	['8', '8', ['1', '6']],
	# 	['8', '9', ['1', '7']],
	# 	['9', '9', ['1', '8']],
	# ]

	# _tabdict = dict([['%s_%s' % (x[0],x[1]), x[2]] for x in _table] +
	# 				[['%s_%s' % (x[1],x[0]), x[2]] for x in _table if x[0] != x[1]])

	_tabdict = {
		'1_1': ['2'],
		'1_2': ['3'],
		'1_3': ['4'],
		'1_4': ['5'],
		'1_5': ['6'],
		'1_6': ['7'],
		'1_7': ['8'],
		'1_8': ['9'],
		'1_9': ['1', '0'],
		'2_1': ['3'],
		'2_2': ['4'],
		'2_3': ['5'],
		'2_4': ['6'],
		'2_5': ['7'],
		'2_6': ['8'],
		'2_7': ['9'],
		'2_8': ['1', '0'],
		'2_9': ['1', '1'],
		'3_1': ['4'],
		'3_2': ['5'],
		'3_3': ['6'],
		'3_4': ['7'],
		'3_5': ['8'],
		'3_6': ['9'],
		'3_7': ['1', '0'],
		'3_8': ['1', '1'],
		'3_9': ['1', '2'],
		'4_1': ['5'],
		'4_2': ['6'],
		'4_3': ['7'],
		'4_4': ['8'],
		'4_5': ['9'],
		'4_6': ['1', '0'],
		'4_7': ['1', '1'],
		'4_8': ['1', '2'],
		'4_9': ['1', '3'],
		'5_1': ['6'],
		'5_2': ['7'],
		'5_3': ['8'],
		'5_4': ['9'],
		'5_5': ['1', '0'],
		'5_6': ['1', '1'],
		'5_7': ['1', '2'],
		'5_8': ['1', '3'],
		'5_9': ['1', '4'],
		'6_1': ['7'],
		'6_2': ['8'],
		'6_3': ['9'],
		'6_4': ['1', '0'],
		'6_5': ['1', '1'],
		'6_6': ['1', '2'],
		'6_7': ['1', '3'],
		'6_8': ['1', '4'],
		'6_9': ['1', '5'],
		'7_1': ['8'],
		'7_2': ['9'],
		'7_3': ['1', '0'],
		'7_4': ['1', '1'],
		'7_5': ['1', '2'],
		'7_6': ['1', '3'],
		'7_7': ['1', '4'],
		'7_8': ['1', '5'],
		'7_9': ['1', '6'],
		'8_1': ['9'],
		'8_2': ['1', '0'],
		'8_3': ['1', '1'],
		'8_4': ['1', '2'],
		'8_5': ['1', '3'],
		'8_6': ['1', '4'],
		'8_7': ['1', '5'],
		'8_8': ['1', '6'],
		'8_9': ['1', '7'],
		'9_1': ['1', '0'],
		'9_2': ['1', '1'],
		'9_3': ['1', '2'],
		'9_4': ['1', '3'],
		'9_5': ['1', '4'],
		'9_6': ['1', '5'],
		'9_7': ['1', '6'],
		'9_8': ['1', '7'],
		'9_9': ['1', '8']}
	@classmethod
	def add(cls, c1, c2):
		if isinstance(c1, str) and len(c1) != 1  and isinstance(c2, str) and len(c2) != 1:
		   raise TypeError("Input should be digit")

		if c1 == '0':
			return c2
		if c2 == '0':
			return c1

		key = '%s_%s' % (c1, c2)
		logging.debug(sorted(cls._tabdict.items()))
		return cls._tabdict[key]

	@classmethod
	def inc(cls, c):
		if isinstance(c, str) and len(c) != 1: 
		   raise TypeError("Input should be digit")

		return cls.add(c, '1')


class StrInteger:
	"""
	A class for long string integer operation: add, multiply.
	"""

	# _vstr = '' 

	def __init__(self, val):
		self._vstr = str(val)

	def __add__(self, obj):
		if not isinstance(obj, StrInteger):
			raise TypeError("Object type must be StrInteger")

		s1, s2 = self._vstr, obj._vstr
		if len(s1) > len(s2):
			s2 = '0'*(len(s1)-len(s2)) + s2
		else:
			s1 = '0'*(len(s2)-len(s1)) + s1

		r = []; rr = False;
		logging.debug("s1: %s, s2: %s", s1, s2)
		for i, (c1, c2) in enumerate(zip(s1[::-1], s2[::-1])):
			d = DigitOp.add(c1, c2)
			logging.debug("d: %s, c1: %s, c2: %s" % (d, c1, c2))
			if rr and len(d) == 1:
				d = DigitOp.inc(d[0])
			elif rr and len(d) == 2:
				d[1] = DigitOp.inc(d[1])[0]

			r.append(d[-1])
			if len(d) > 1:
				rr = True
			else:
				rr = False
			logging.debug("rr: %s, r: %s" % (rr, r))

		if rr:
			r.append('1')

		return StrInteger(''.join(r[::-1]))


	def __str__(self):
		return self._vstr

	def __repr__(self):
		return "StrInteger(%s)" % self._vstr


if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	# a1 = StrInteger("123456789")
	# a2 = StrInteger("370370367")
	# print("%s" % (a1+a2))
	s1 = StrInteger("123456789")
	ss = StrInteger("0")
	for i in range(10):
		ss = ss + s1
		print("%d, %s" % (i, ss))

		