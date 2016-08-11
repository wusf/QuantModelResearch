import os
import sys

root = os.path.abspath('d:\\pyquantlib2\\')
sys.path.append(root)
import outputtool.generate_log as gl
import datetool.get_trade_day as gtr

gen_log = gl.GenLog('get_trade_date', 'DEBUG')
mylog = gen_log.generate(1, 1)

dbinfo_cfg_path = 'dbinfo.cfg'

trdday = gtr.GetTradeDay(dbinfo_cfg_path, mylog)
trd_status = trdday.check_stock_trade_status('600837', '20160405',1)
print trd_status



import fetchdatatool.fetch_hist_eqty_data as fetchdata


fdata = fetchdata.FetchHistData(dbinfo_cfg_path, mylog)
stockcode = ['300435']
security_type = 'a_stock'
start_date = '20150228'
end_date = '20150508'
is_adj = 1

df = fdata.fetch_close_price(stockcode, security_type, start_date, end_date, is_adj)

#ret = fdata.fetch_return(stockcode, security_type, start_date, end_date, 1, 'log')

ret = fdata.fetch_hedged_return(stockcode, security_type, start_date, end_date, 1, 'log', '000300')

