#!/usr/bin/env python
#coding:utf-8
"""
  Author:  wusf --<wushifan221@gmail>
  Purpose: 
  Created: 2016/7/20
"""

import os
import sys

root = os.path.abspath('d:\\pyquantlib2\\')
sys.path.append(root)
import outputtool.generate_log as gl
import eventstudy.event_study as es

gen_log = gl.GenLog('event_high_div_stk_shr_trans', 'DEBUG')
mylog = gen_log.generate(1, 1)

dbinfo_cfg_path = 'dbinfo.cfg'

myes = es.EventStudy(dbinfo_cfg_path, mylog)

event_name = u'高送转实施公告日股价影响'
event_table = 'event_data_dividend'
test_start_date = '20100101'
test_end_date = '20160601'
event_start_mark = 'DateShrHldMeetingAnnouncement'
event_start_mark = 'DateShrHldMeetingAnnouncement'
event_start_mark = 'DateEventAnnoucement'
event_end_mark = 'null'
event_speical_variable = '(ifnull(NumeStockDividend,0)+ifnull(NumeTransfer2Share,0))'
event_str = """
            (ifnull(NumeStockDividend,0)+ifnull(NumeTransfer2Share,0))>=10
            and Prog1Code in (2,3)
            """
constituent_index = ['000001','399106']

myes.find_raw_event(event_table, event_speical_variable,
                    test_start_date, test_end_date,
                    event_start_mark, event_end_mark,
                    event_str, constituent_index)

import matplotlib.pyplot as plt

result = myes.plot_event(event_name, 60, 60, 0, '000300')
result[0].plot()
result[0].to_csv('event_return.csv')
