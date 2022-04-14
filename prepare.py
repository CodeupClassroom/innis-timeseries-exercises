import pandas as pd

def prep_store_data(df):
    df.sale_date = df.sale_date.apply(lambda date: date[:-13])
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y')
    # make sure we sort by date/time before resampling or doing other time series manipulations
    df = df.set_index('sale_date').sort_index()
    df = df.rename(columns={'sale_amount': 'quantity'})
    df['month'] = df.index.month
    df['dow'] = df.index.day_name()
    df['sales_total'] = df.quantity * df.item_price
    return df

def prep_opsd_data(df):
    df.columns = [column.lower() for column in df]
    df = df.rename(columns={'wind+solar': 'wind_and_solar'})

    df.date = pd.to_datetime(df.date)
    df = df.set_index('date').sort_index()

    df['month'] = df.index.month
    df['year'] = df.index.year

    df = df.fillna(0)
    return df