#!/usr/bin/env python
#coding:utf-8
"""
  Author:  wusf --<wushifan221@gmail.com>
  Purpose: 
  Created: 2016/7/7
"""

import os
import sys
import logging

root = os.path.abspath('d:\\quantlib2\\')
sys.path.append(root)
import syncdata.sync_mssql as sync1
import syncdata.sync_oracle as sync2

import outputtool.generate_log as gl
BUFFER_SIZE = 100000
DATE_SEGMENT = 'month'

#----------------------------------------------------------------------
def sync_analyst_data(startdate, method='update'):
    """"""
    gen_log = gl.GenLog('sync_analyst_data', 'DEBUG')
    mylog = gen_log.generate(1, 1)
    dbname = 'dbsuntime_cicc'
    dbinfo_cfg_path = 'cfg//dbinfo.cfg'
    table_info_cfg = 'cfg//analyst_data_table.cfg'
    start_date = startdate
    srd = sync1.SyncRawDataFromMssql(dbname, dbinfo_cfg_path, table_info_cfg,
                           start_date, mylog)
    srd.conn_remote_db()
    srd.conn_local_db()
    srd.run(DATE_SEGMENT, BUFFER_SIZE, method)


#----------------------------------------------------------------------
def sync_financial_data(startdate, method='update'):
    """"""
    gen_log = gl.GenLog('sync_financial_data', 'DEBUG')
    mylog = gen_log.generate(1, 1)
    dbname = 'dbwind_cicc'
    dbinfo_cfg_path = 'cfg//dbinfo.cfg'
    table_info_cfg = 'cfg//financial_data_table.cfg'
    start_date = startdate
    srd = sync2.SyncRawDataFromOracle(dbname, dbinfo_cfg_path, table_info_cfg,
                           start_date, mylog)
    srd.conn_remote_db()
    srd.conn_local_db()
    srd.run(DATE_SEGMENT, BUFFER_SIZE, method)


#----------------------------------------------------------------------
def sync_market_data(startdate, method='update'):
    """"""
    gen_log = gl.GenLog('sync_market_data', 'DEBUG')
    mylog = gen_log.generate(1, 1)
    dbname = 'dbwind_cicc'
    dbinfo_cfg_path = 'cfg//dbinfo.cfg'
    table_info_cfg = 'cfg//market_data_table.cfg'
    start_date = startdate
    srd = sync2.SyncRawDataFromOracle(dbname, dbinfo_cfg_path, table_info_cfg,
                           start_date, mylog)
    srd.conn_remote_db()
    srd.conn_local_db()
    srd.run(DATE_SEGMENT, BUFFER_SIZE, method)


#----------------------------------------------------------------------
def sync_event_data(startdate, method='update'):
    """"""
    gen_log = gl.GenLog('sync_event_data', 'DEBUG')
    mylog = gen_log.generate(1, 1)
    dbname = 'dbwind_cicc'
    dbinfo_cfg_path = 'cfg//dbinfo.cfg'
    table_info_cfg = 'cfg//event_data_table.cfg'
    start_date = startdate
    srd = sync2.SyncRawDataFromOracle(dbname, dbinfo_cfg_path, table_info_cfg,
                           start_date, mylog)
    srd.conn_remote_db()
    srd.conn_local_db()
    srd.run(DATE_SEGMENT, BUFFER_SIZE, method)


#----------------------------------------------------------------------
def sync_event_data(startdate, method='update'):
    """"""
    gen_log = gl.GenLog('sync_event_data', 'DEBUG')
    mylog = gen_log.generate(1, 1)
    dbname = 'dbwind_cicc'
    dbinfo_cfg_path = 'cfg//dbinfo.cfg'
    table_info_cfg = 'cfg//event_data_table.cfg'
    start_date = startdate
    srd = sync2.SyncRawDataFromOracle(dbname, dbinfo_cfg_path, table_info_cfg,
                           start_date, mylog)
    srd.conn_remote_db()
    srd.conn_local_db()
    srd.run(DATE_SEGMENT, BUFFER_SIZE, method)
    
    
#----------------------------------------------------------------------
def sync_info_data(startdate, method='update'):
    """"""
    gen_log = gl.GenLog('sync_info_data', 'DEBUG')
    mylog = gen_log.generate(1, 1)
    dbname = 'dbwind_cicc'
    dbinfo_cfg_path = 'cfg//dbinfo.cfg'
    table_info_cfg = 'cfg//info_data_table.cfg'
    start_date = startdate
    srd = sync2.SyncRawDataFromOracle(dbname, dbinfo_cfg_path, table_info_cfg,
                           start_date, mylog)
    srd.conn_remote_db()
    srd.conn_local_db()
    srd.run(DATE_SEGMENT, BUFFER_SIZE, method)