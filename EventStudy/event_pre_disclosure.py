#!/usr/bin/env python
#coding:utf-8
"""
  Author:  wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/7/26
"""

import os
import sys

root = os.path.abspath('d:\\quantlib2\\')
sys.path.append(root)
import outputtool.generate_log as gl
import eventstudy.event_study as es
import pandas as pd



gen_log = gl.GenLog('event_high_pre_disclosure', 'DEBUG')
mylog = gen_log.generate(1, 1)

dbinfo_cfg_path = 'dbinfo.cfg'

myes = es.EventStudy(dbinfo_cfg_path, mylog)

event_name = u'业绩预增'
event_table = 'event_data_earnings_forecast_disclosure'
test_start_date = '20100101'
test_end_date = '20160601'
event_start_mark = 'Date'
event_end_mark = 'null'
event_speical_variable = 'Change'
event_str = """
            Change>=100
            """
constituent_index = ['000001','399106']

myes.find_raw_event(event_table, event_speical_variable,
                    test_start_date, test_end_date,
                    event_start_mark, event_end_mark,
                    event_str, constituent_index)


result = myes.plot_event(event_name, 60, 60, 1, '000300')
result[0].plot()
result[0].to_csv('event_return.csv')
pd.DataFrame().to_csv('pre_disclosure.csv')