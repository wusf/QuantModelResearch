import os
import sys
import time
import pandas 
print pandas.__version__

root = os.path.abspath('d:\\quantlib2\\')
sys.path.append(root)
import outputtool.generate_log as gl
import procfindata.process_financial_data_by_sql as pf

gen_log = gl.GenLog('process_financial_data', 'DEBUG')
mylog = gen_log.generate(1, 1)

dbinfo_cfg_path = 'dbinfo.cfg'


start_date = '20070101'
procfin = pf.ProcFinancialData(start_date, dbinfo_cfg_path, mylog)
procfin.load_local_db_into_memory()
procfin._get_financial_item_algos('financial_item_algos.cfg')
print procfin.fin_item_names

qts = procfin._get_past_fin_quarters('20151231', 8)
print qts

procfin.find_all_stock_codes()

tm1 = time.time()
procfin.find_days_when_data_change()
tm2 = time.time()
print tm2-tm1


#procfin.process_concurrent()
procfin.process()
import sqlite3 

sqlite3.Cache