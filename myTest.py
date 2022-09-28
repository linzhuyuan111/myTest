# -*- coding: utf-8 -*-

import time
import json
from base64 import b64decode, b64encode


if __name__ == '__main__':
	stamp = time.mktime(time.strptime('2022-9-24 01:00:00', '%Y-%m-%d %H:%M:%S'))
	print int(stamp)

	print int(stamp) - 1663950637

	print (int(stamp) - 1663950637) / (3600 * 24)

	print 'great'