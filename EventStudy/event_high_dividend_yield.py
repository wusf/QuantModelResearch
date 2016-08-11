#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/7/20
"""

import os
import sys

root = os.path.abspath('d:\\pyquantlib2\\')
sys.path.append(root)
import outputtool.generate_log as gl
import eventstudy.event_study as es
import pandas as pd

########################################################################
class EventHighDividendYield(es.EventStudy):
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self, dbinfocfgpath, log):
        super(EventHighDividendYield, self).__init__(dbinfocfgpath, log)
        self.div_yields = []
        

    #----------------------------------------------------------------------
    def _event_filter(self, event):
        stockcode = event[0]
        event_day = event[1]
        cash_div = event[-1]
        _status = self.trdday.check_stock_trade_status(stockcode, event_day, 1) 
        _price = self.trdday.get_latest_close_price(stockcode , event_day)
        div_yield = cash_div/(_price*10)
        self.div_yields.append([stockcode,div_yield])
        if div_yield>=0.1 and _status==-1:
            val = 1
        else:
            val = 0
        return val



gen_log = gl.GenLog('event_high_div_yield', 'DEBUG')
mylog = gen_log.generate(1, 1)

dbinfo_cfg_path = 'dbinfo.cfg'

myes = EventHighDividendYield(dbinfo_cfg_path, mylog)

event_name = u'现金分红实施公告日股价影响'
event_table = 'event_data_dividend'
test_start_date = '20100101'
test_end_date = '20160601'
event_start_mark = 'DateShrHldMeetingAnnouncement'
event_end_mark = 'null'
event_speical_variable = 'NumeCashDividend'
event_str = """
            NumeCashDividend>=0
            and Prog1Code in (2,3)
            """
constituent_index = ['000001','399106']

myes.find_raw_event(event_table, event_speical_variable,
                    test_start_date, test_end_date,
                    event_start_mark, event_end_mark,
                    event_str, constituent_index)


result = myes.plot_event(event_name, 60, 60, 1, '000300')
result[0].plot()
result[0].to_csv('event_return.csv')
pd.DataFrame(myes.div_yields).to_csv('div_yields.csv')