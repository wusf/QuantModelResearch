import os
import sys

root = os.path.abspath('d:\\pyquantlib2\\')
sys.path.append(root)
import outputtool.generate_log as gl
import histdatastats.get_distribution as getdist
import fetchdatatool.fetch_hist_eqty_data as fh

gen_log = gl.GenLog('sync_analyst_data', 'DEBUG')
mylog = gen_log.generate(1, 1)

dbinfo_cfg_path = 'dbinfo.cfg'
gd = getdist.GetHistReturnDist(dbinfo_cfg_path, mylog)

stkcode_list = '000300'
start_date = '20050601'
end_date = '20160601'
security_type = 'index'
is_adj = 1
return_type = 'log'

gd.get_dist(stkcode_list, security_type, 1,
            return_type, start_date, end_date,100)
gd.compare2norm()



