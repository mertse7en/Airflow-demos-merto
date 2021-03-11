import io
import os
import requests
import urllib
import json
import pandas as pd
import datetime
import logging


def etl_function(**kwargs):
    ti = kwargs['ti']

    logging.info('Hello')
    api_token = '398605a1-1356-4b82-ab0d-1c5485028ad1'
    

    today = datetime.datetime.now()
    from_day = today - datetime.timedelta(20)

    start_date = str(from_day).split(' ')[0]
    end_date = str(today).split(' ')[0]

    params = {'api_token':'398605a1-1356-4b82-ab0d-1c5485028ad1',
                'from': start_date,
                'to': end_date}

    request_url = 'https://hq.appsflyer.com/export/id1489293379/installs_report/v5?api_token=398605a1-1356-4b82-ab0d-1c5485028ad1&from=2021-02-02&to=2021-02-25&timezone=Europe%2fIstanbul'
    
    res = requests.request('GET', request_url)
    if res.status_code != 200:
            if res.status_code == 404:
                print('There is a problem with the request URL. Make sure that it is correct')
            else:
                print('There was a problem retrieving data: ', res.text)

        
    res_df = pd.read_csv(io.StringIO(res.text))

    # First way of pushing data is return ------ # But it needs to be in key-value format ??? // df is no acceptable
    # Specific bi task'a pushlamıyorum isteyen herkes alabilir tabi downstream olmak zorunda <<<<
    res_df = res_df.to_dict()
    return res_df

    # Second way of pushing ----- 
        # ti.xcom_push(key='res_df', value=res_df)

