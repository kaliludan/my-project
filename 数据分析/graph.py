import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import tushare as ts
df = ts.realtime_boxoffice()
xx = (df)

xx.to_csv('/Users/kaliludan1/my-project/my-project/数据分析/box.csv')