import pandas as pd
import requests
from data.cn_stock_selection import TABLE_CN_STOCK_SELECTION
from data.utils import get_field_type_name


def stock_selection() -> pd.DataFrame:
    """
    东方财富网-个股-选股器
    https://data.eastmoney.com/xuangu/
    :return: 选股器
    :rtype: pandas.DataFrame
    """
    cols = TABLE_CN_STOCK_SELECTION['columns']
    sty = ""  # 初始值 "SECUCODE,SECURITY_CODE,SECURITY_NAME_ABBR,CHANGE_RATE"
    for k in cols:
        sty = f"{sty},{cols[k]['map']}"
    url = "https://data.eastmoney.com/dataapi/xuangu/list"
    params = {
        "sty": sty[1:],
        # "上交所主板","深交所主板","深交所创业板","上交所科创板","上交所风险警示板","深交所风险警示板","北京证券交易所","上交所主板","上交所风险警示板","上交所科创板"
        "filter": "(MARKET+in+(\"上交所主板\",\"深交所主板\",\"深交所创业板\"))(NEW_PRICE>0)",
        "p": 1,
        "ps": 10000,
        "source": "SELECT_SECURITIES",
        "client": "WEB"
    }

    r = requests.get(url, params=params)
    data_json = r.json()
    data = data_json["result"]["data"]
    if not data:
        return pd.DataFrame()
    temp_df = pd.DataFrame(data)

    mask = ~temp_df['CONCEPT'].isna()
    temp_df.loc[mask, 'CONCEPT'] = temp_df.loc[mask, 'CONCEPT'].apply(lambda x: ', '.join(x))
    mask = ~temp_df['STYLE'].isna()
    temp_df.loc[mask, 'STYLE'] = temp_df.loc[mask, 'STYLE'].apply(lambda x: ', '.join(x))

    for k in cols:
        t = get_field_type_name(cols[k]["type"])
        if t == 'numeric':
            temp_df[cols[k]["map"]] = pd.to_numeric(temp_df[cols[k]["map"]], errors="coerce")
        elif t == 'datetime':
            temp_df[cols[k]["map"]] = pd.to_datetime(temp_df[cols[k]["map"]], errors="coerce").dt.date

    return temp_df

