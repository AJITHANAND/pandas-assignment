import pandas as pd

df = pd.read_csv('data.csv')

def total_impression(df:pd.DataFrame):
    temp = df[(df['age']=='30-34') | ((df['age'] >= '30') & (df['age'] <= '34')) ]
    total = temp['impressions'].sum()
    print("Total impression of the age group 30-34 :{}".format(total))
def get_ids(df:pd.DataFrame):
    ids = df.groupby('campaign_id')['ad_id'].apply(list)
    print('Ad IDs by campaign ID: {}'.format(ids))
def get_total_click(df:pd.DataFrame):
    df['reporting_start'] = pd.to_datetime(df['reporting_start'], format='%d/%m/%Y')
    df['reporting_end'] = pd.to_datetime(df['reporting_end'], format='%d/%m/%Y')
    temp = df[(df['reporting_start'] >= '2017-08-19') & (df['reporting_end'] <= '2017-08-22')]
    total = temp['clicks'].sum()
    print("Total Click in between 2017-08-19 & 2017-08-22 :{}".format(total))
total_impression(df)
get_ids(df)
get_total_click(df)
