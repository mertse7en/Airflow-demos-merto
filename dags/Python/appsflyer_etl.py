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
    api_token = 
    

    today = datetime.datetime.now()
    from_day = today - datetime.timedelta(20)

    start_date = str(from_day).split(' ')[0]
    end_date = str(today).split(' ')[0]

    params = {'api_token':'',
                'from': start_date,
                'to': end_date}

    request_url = 
    
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

