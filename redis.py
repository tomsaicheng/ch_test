# -*- coding: utf-8 -*-
# import redis
#
# r = redis.Redis(host='10.16.2.49', port=6379, db=0)
# print r.get('product_getProductVoById')

import redis, datetime


r = redis(host='10.16.2.49', port=6379, db=0)
print(r.get('product_getProductVoById'))

print 1
print datetim.datetime.now()







