# -*- coding:utf-8 -*-

import pymssql

ms = MSSQL(host="127.0.0.1",user="sa",pwd="kj222",db="BW_CONTRACT")

conn = pymssql.connect(server='.', user='', password='', database='', timeout=0, login_timeout=60, charset='UTF-8', as_dict=False, host='', appname=None, port='1433', conn_properties, autocommit=False, tds_version='7.1')
print(conn)
