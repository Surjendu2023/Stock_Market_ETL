import requests
import os
import json


def main():


    def data_fetch():
        api_key=os.getenv(my_api_key)
        URL=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey={api_key}'
        responce=requests.get(URL)
        if responce.status_code==200:
            print('We have connected......')
            data=responce.json()   
            database=[]     
            for date in data(['Time Series (Daily)']):
                new_date=date
                opening_bal=data['Time Series (Daily)'][date]['1. open']
                closing_bal=data['Time Series (Daily)'][date]['4. close']
                Today_High=data['Time Series (Daily)'][date]['2. high']
                Today_Low=data['Time Series (Daily)'][date]['3. low']
                Volume=data['Time Series (Daily)'][date]['5. volume']
                element={"date":new_date,"opening_bal":opening_bal,"closing_bal":closing_bal,"Today_High":Today_High,"Today_Low":Today_Low,"Volume":Volume}
                database.append(element)

    def data_load():
        import psycopg2
        from sqlalchemy import create_engine
        import pandas as pd
        engine=create_engine('postgresql+psycopg2://postgres:admin@localhost/surjendu')
        df=pd.DataFrame(database)
        df.to_sql('Stock_Market_data',engine,if_exists='replace') 
        

    def notify():
        info=dict(token='6653752665:AAGeGEqnSaraeY1dHNGjGLY-GEyyhDfCxgU',
                chat_id='1702937489',
                message='Data Loaded')
        trigger=f"https://api.telegram.org/bot{info['token']}/sendMessage?chat_id={info['chat_id']}&text={info['message']}"
        print(requests.get(trigger))

    data_fetch()
    data_load()
    notify()


if __name__=='__main__':
    main()