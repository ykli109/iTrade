from sqlalchemy import DATE, NVARCHAR, FLOAT, BIGINT, SmallInteger
from sqlalchemy.dialects.mysql import BIT

TABLE_CN_STOCK_SELECTION = {
    'name': 'cn_stock_selection',
    'cn': '综合选股',
    'columns': {
        'date': {
            'type': DATE,
            'cn': '日期',
            'size': 0,
            'map': 'MAX_TRADE_DATE'
        },
        'code': {
            'type': NVARCHAR(length=6),
            'cn': '代码',
            'size': 60,
            'map': 'SECURITY_CODE'
        },
        'name': {
            'type': NVARCHAR(length=20),
            'cn': '名称',
            'size': 70,
            'map': 'SECURITY_NAME_ABBR'
        },
        'new_price': {
            'type': FLOAT,
            'cn': '最新价',
            'size': 70,
            'map': 'NEW_PRICE'
        },
        'change_rate': {
            'type': FLOAT,
            'cn': '涨跌幅',
            'size': 70,
            'map': 'CHANGE_RATE'
        },
        'volume_ratio': {
            'type': FLOAT,
            'cn': '量比',
            'size': 70,
            'map': 'VOLUME_RATIO'
        },
        'high_price': {
            'type': FLOAT,
            'cn': '最高价',
            'size': 70,
            'map': 'HIGH_PRICE'
        },
        'low_price': {
            'type': FLOAT,
            'cn': '最低价',
            'size': 70,
            'map': 'LOW_PRICE'
        },
        'pre_close_price': {
            'type': FLOAT,
            'cn': '昨收价',
            'size': 70,
            'map': 'PRE_CLOSE_PRICE'
        },
        'volume': {
            'type': BIGINT,
            'cn': '成交量',
            'size': 90,
            'map': 'VOLUME'
        },
        'deal_amount': {
            'type': BIGINT,
            'cn': '成交额',
            'size': 100,
            'map': 'DEAL_AMOUNT'
        },
        'turnoverrate': {
            'type': FLOAT,
            'cn': '换手率',
            'size': 70,
            'map': 'TURNOVERRATE'
        },
        'listing_date': {
            'type': DATE,
            'cn': '上市时间',
            'size': 110,
            'map': 'LISTING_DATE'
        },
        'industry': {
            'type': NVARCHAR(length=20),
            'cn': '行业',
            'size': 100,
            'map': 'INDUSTRY'
        },
        'area': {
            'type': NVARCHAR(length=20),
            'cn': '地区',
            'size': 70,
            'map': 'AREA'
        },
        'concept': {
            'type': NVARCHAR(length=255),
            'cn': '概念',
            'size': 150,
            'map': 'CONCEPT'
        },
        'style': {
            'type': NVARCHAR(length=255),
            'cn': '板块',
            'size': 150,
            'map': 'STYLE'
        },
        'is_hs300': {
            'type': NVARCHAR(length=2),
            'cn': '沪300',
            'size': 0,
            'map': 'IS_HS300'
        },
        'is_sz50': {
            'type': NVARCHAR(length=2),
            'cn': '上证50',
            'size': 0,
            'map': 'IS_SZ50'
        },
        'is_zz500': {
            'type': NVARCHAR(length=2),
            'cn': '中证500',
            'size': 0,
            'map': 'IS_ZZ500'
        },
        'is_zz1000': {
            'type': NVARCHAR(length=2),
            'cn': '中证1000',
            'size': 0,
            'map': 'IS_ZZ1000'
        },
        'is_cy50': {
            'type': NVARCHAR(length=2),
            'cn': '创业板50',
            'size': 0,
            'map': 'IS_CY50'
        },
        'pe9': {
            'type': FLOAT,
            'cn': '市盈率TTM',
            'size': 70,
            'map': 'PE9'
        },
        'pbnewmrq': {
            'type': FLOAT,
            'cn': '市净率MRQ',
            'size': 70,
            'map': 'PBNEWMRQ'
        },
        'pettmdeducted': {
            'type': FLOAT,
            'cn': '市盈率TTM扣非',
            'size': 70,
            'map': 'PETTMDEDUCTED'
        },
        'ps9': {
            'type': FLOAT,
            'cn': '市销率TTM',
            'size': 70,
            'map': 'PS9'
        },
        'pcfjyxjl9': {
            'type': FLOAT,
            'cn': '市现率TTM',
            'size': 70,
            'map': 'PCFJYXJL9'
        },
        'predict_pe_syear': {
            'type': FLOAT,
            'cn': '预测市盈率今年',
            'size': 70,
            'map': 'PREDICT_PE_SYEAR'
        },
        'predict_pe_nyear': {
            'type': FLOAT,
            'cn': '预测市盈率明年',
            'size': 70,
            'map': 'PREDICT_PE_NYEAR'
        },
        'total_market_cap': {
            'type': BIGINT,
            'cn': '总市值',
            'size': 120,
            'map': 'TOTAL_MARKET_CAP'
        },
        'free_cap': {
            'type': BIGINT,
            'cn': '流通市值',
            'size': 120,
            'map': 'FREE_CAP'
        },
        'dtsyl': {
            'type': FLOAT,
            'cn': '动态市盈率',
            'size': 70,
            'map': 'DTSYL'
        },
        'ycpeg': {
            'type': FLOAT,
            'cn': '预测PEG',
            'size': 70,
            'map': 'YCPEG'
        },
        'enterprise_value_multiple': {
            'type': FLOAT,
            'cn': '企业价值倍数',
            'size': 70,
            'map': 'ENTERPRISE_VALUE_MULTIPLE'
        },
        'basic_eps': {
            'type': FLOAT,
            'cn': '每股收益',
            'size': 70,
            'map': 'BASIC_EPS'
        },
        'bvps': {
            'type': FLOAT,
            'cn': '每股净资产',
            'size': 70,
            'map': 'BVPS'
        },
        'per_netcash_operate': {
            'type': FLOAT,
            'cn': '每股经营现金流',
            'size': 70,
            'map': 'PER_NETCASH_OPERATE'
        },
        'per_fcfe': {
            'type': FLOAT,
            'cn': '每股自由现金流',
            'size': 70,
            'map': 'PER_FCFE'
        },
        'per_capital_reserve': {
            'type': FLOAT,
            'cn': '每股资本公积',
            'size': 70,
            'map': 'PER_CAPITAL_RESERVE'
        },
        'per_unassign_profit': {
            'type': FLOAT,
            'cn': '每股未分配利润',
            'size': 70,
            'map': 'PER_UNASSIGN_PROFIT'
        },
        'per_surplus_reserve': {
            'type': FLOAT,
            'cn': '每股盈余公积',
            'size': 70,
            'map': 'PER_SURPLUS_RESERVE'
        },
        'per_retained_earning': {
            'type': FLOAT,
            'cn': '每股留存收益',
            'size': 70,
            'map': 'PER_RETAINED_EARNING'
        },
        'parent_netprofit': {
            'type': BIGINT,
            'cn': '归属净利润',
            'size': 110,
            'map': 'PARENT_NETPROFIT'
        },
        'deduct_netprofit': {
            'type': BIGINT,
            'cn': '扣非净利润',
            'size': 110,
            'map': 'DEDUCT_NETPROFIT'
        },
        'total_operate_income': {
            'type': BIGINT,
            'cn': '营业总收入',
            'size': 120,
            'map': 'TOTAL_OPERATE_INCOME'
        },
        'roe_weight': {
            'type': FLOAT,
            'cn': '净资产收益率ROE',
            'size': 70,
            'map': 'ROE_WEIGHT'
        },
        'jroa': {
            'type': FLOAT,
            'cn': '总资产净利率ROA',
            'size': 70,
            'map': 'JROA'
        },
        'roic': {
            'type': FLOAT,
            'cn': '投入资本回报率ROIC',
            'size': 70,
            'map': 'ROIC'
        },
        'zxgxl': {
            'type': FLOAT,
            'cn': '最新股息率',
            'size': 70,
            'map': 'ZXGXL'
        },
        'sale_gpr': {
            'type': FLOAT,
            'cn': '毛利率',
            'size': 70,
            'map': 'SALE_GPR'
        },
        'sale_npr': {
            'type': FLOAT,
            'cn': '净利率',
            'size': 70,
            'map': 'SALE_NPR'
        },
        'netprofit_yoy_ratio': {
            'type': FLOAT,
            'cn': '净利润增长率',
            'size': 70,
            'map': 'NETPROFIT_YOY_RATIO'
        },
        'deduct_netprofit_growthrate': {
            'type': FLOAT,
            'cn': '扣非净利润增长率',
            'size': 70,
            'map': 'DEDUCT_NETPROFIT_GROWTHRATE'
        },
        'toi_yoy_ratio': {
            'type': FLOAT,
            'cn': '营收增长率',
            'size': 70,
            'map': 'TOI_YOY_RATIO'
        },
        'netprofit_growthrate_3y': {
            'type': FLOAT,
            'cn': '净利润3年复合增长率',
            'size': 70,
            'map': 'NETPROFIT_GROWTHRATE_3Y'
        },
        'income_growthrate_3y': {
            'type': FLOAT,
            'cn': '营收3年复合增长率',
            'size': 70,
            'map': 'INCOME_GROWTHRATE_3Y'
        },
        'predict_netprofit_ratio': {
            'type': FLOAT,
            'cn': '预测净利润同比增长',
            'size': 70,
            'map': 'PREDICT_NETPROFIT_RATIO'
        },
        'predict_income_ratio': {
            'type': FLOAT,
            'cn': '预测营收同比增长',
            'size': 70,
            'map': 'PREDICT_INCOME_RATIO'
        },
        'basiceps_yoy_ratio': {
            'type': FLOAT,
            'cn': '每股收益同比增长率',
            'size': 70,
            'map': 'BASICEPS_YOY_RATIO'
        },
        'total_profit_growthrate': {
            'type': FLOAT,
            'cn': '利润总额同比增长率',
            'size': 70,
            'map': 'TOTAL_PROFIT_GROWTHRATE'
        },
        'operate_profit_growthrate': {
            'type': FLOAT,
            'cn': '营业利润同比增长率',
            'size': 70,
            'map': 'OPERATE_PROFIT_GROWTHRATE'
        },
        'debt_asset_ratio': {
            'type': FLOAT,
            'cn': '资产负债率',
            'size': 70,
            'map': 'DEBT_ASSET_RATIO'
        },
        'equity_ratio': {
            'type': FLOAT,
            'cn': '产权比率',
            'size': 70,
            'map': 'EQUITY_RATIO'
        },
        'equity_multiplier': {
            'type': FLOAT,
            'cn': '权益乘数',
            'size': 70,
            'map': 'EQUITY_MULTIPLIER'
        },
        'current_ratio': {
            'type': FLOAT,
            'cn': '流动比率',
            'size': 70,
            'map': 'CURRENT_RATIO'
        },
        'speed_ratio': {
            'type': FLOAT,
            'cn': '速动比率',
            'size': 70,
            'map': 'SPEED_RATIO'
        },
        'total_shares': {
            'type': BIGINT,
            'cn': '总股本',
            'size': 120,
            'map': 'TOTAL_SHARES'
        },
        'free_shares': {
            'type': BIGINT,
            'cn': '流通股本',
            'size': 120,
            'map': 'FREE_SHARES'
        },
        'holder_newest': {
            'type': BIGINT,
            'cn': '最新股东户数',
            'size': 80,
            'map': 'HOLDER_NEWEST'
        },
        'holder_ratio': {
            'type': FLOAT,
            'cn': '股东户数增长率',
            'size': 70,
            'map': 'HOLDER_RATIO'
        },
        'hold_amount': {
            'type': FLOAT,
            'cn': '户均持股金额',
            'size': 80,
            'map': 'HOLD_AMOUNT'
        },
        'avg_hold_num': {
            'type': FLOAT,
            'cn': '户均持股数量',
            'size': 70,
            'map': 'AVG_HOLD_NUM'
        },
        'holdnum_growthrate_3q': {
            'type': FLOAT,
            'cn': '户均持股数季度增长率',
            'size': 70,
            'map': 'HOLDNUM_GROWTHRATE_3Q'
        },
        'holdnum_growthrate_hy': {
            'type': FLOAT,
            'cn': '户均持股数半年增长率',
            'size': 70,
            'map': 'HOLDNUM_GROWTHRATE_HY'
        },
        'hold_ratio_count': {
            'type': FLOAT,
            'cn': '十大股东持股比例合计',
            'size': 70,
            'map': 'HOLD_RATIO_COUNT'
        },
        'free_hold_ratio': {
            'type': FLOAT,
            'cn': '十大流通股东比例合计',
            'size': 70,
            'map': 'FREE_HOLD_RATIO'
        },
        'macd_golden_fork': {
            'type': BIT,
            'cn': 'MACD金叉日线',
            'size': 70,
            'map': 'MACD_GOLDEN_FORK'
        },
        'macd_golden_forkz': {
            'type': BIT,
            'cn': 'MACD金叉周线',
            'size': 70,
            'map': 'MACD_GOLDEN_FORKZ'
        },
        'macd_golden_forky': {
            'type': BIT,
            'cn': 'MACD金叉月线',
            'size': 70,
            'map': 'MACD_GOLDEN_FORKY'
        },
        'kdj_golden_fork': {
            'type': BIT,
            'cn': 'KDJ金叉日线',
            'size': 70,
            'map': 'KDJ_GOLDEN_FORK'
        },
        'kdj_golden_forkz': {
            'type': BIT,
            'cn': 'KDJ金叉周线',
            'size': 70,
            'map': 'KDJ_GOLDEN_FORKZ'
        },
        'kdj_golden_forky': {
            'type': BIT,
            'cn': 'KDJ金叉月线',
            'size': 70,
            'map': 'KDJ_GOLDEN_FORKY'
        },
        'break_through': {
            'type': BIT,
            'cn': '放量突破',
            'size': 70,
            'map': 'BREAK_THROUGH'
        },
        'low_funds_inflow': {
            'type': BIT,
            'cn': '低位资金净流入',
            'size': 70,
            'map': 'LOW_FUNDS_INFLOW'
        },
        'high_funds_outflow': {
            'type': BIT,
            'cn': '高位资金净流出',
            'size': 70,
            'map': 'HIGH_FUNDS_OUTFLOW'
        },
        'breakup_ma_5days': {
            'type': BIT,
            'cn': '向上突破均线5日',
            'size': 70,
            'map': 'BREAKUP_MA_5DAYS'
        },
        'breakup_ma_10days': {
            'type': BIT,
            'cn': '向上突破均线10日',
            'size': 70,
            'map': 'BREAKUP_MA_10DAYS'
        },
        'breakup_ma_20days': {
            'type': BIT,
            'cn': '向上突破均线20日',
            'size': 70,
            'map': 'BREAKUP_MA_20DAYS'
        },
        'breakup_ma_30days': {
            'type': BIT,
            'cn': '向上突破均线30日',
            'size': 70,
            'map': 'BREAKUP_MA_30DAYS'
        },
        'breakup_ma_60days': {
            'type': BIT,
            'cn': '向上突破均线60日',
            'size': 70,
            'map': 'BREAKUP_MA_60DAYS'
        },
        'long_avg_array': {
            'type': BIT,
            'cn': '均线多头排列',
            'size': 70,
            'map': 'LONG_AVG_ARRAY'
        },
        'short_avg_array': {
            'type': BIT,
            'cn': '均线空头排列',
            'size': 70,
            'map': 'SHORT_AVG_ARRAY'
        },
        'upper_large_volume': {
            'type': BIT,
            'cn': '连涨放量',
            'size': 70,
            'map': 'UPPER_LARGE_VOLUME'
        },
        'down_narrow_volume': {
            'type': BIT,
            'cn': '下跌无量',
            'size': 70,
            'map': 'DOWN_NARROW_VOLUME'
        },
        'one_dayang_line': {
            'type': BIT,
            'cn': '一根大阳线',
            'size': 70,
            'map': 'ONE_DAYANG_LINE'
        },
        'two_dayang_lines': {
            'type': BIT,
            'cn': '两根大阳线',
            'size': 70,
            'map': 'TWO_DAYANG_LINES'
        },
        'rise_sun': {
            'type': BIT,
            'cn': '旭日东升',
            'size': 70,
            'map': 'RISE_SUN'
        },
        'power_fulgun': {
            'type': BIT,
            'cn': '强势多方炮',
            'size': 70,
            'map': 'POWER_FULGUN'
        },
        'restore_justice': {
            'type': BIT,
            'cn': '拨云见日',
            'size': 70,
            'map': 'RESTORE_JUSTICE'
        },
        'down_7days': {
            'type': BIT,
            'cn': '七仙女下凡(七连阴)',
            'size': 70,
            'map': 'DOWN_7DAYS'
        },
        'upper_8days': {
            'type': BIT,
            'cn': '八仙过海(八连阳)',
            'size': 70,
            'map': 'UPPER_8DAYS'
        },
        'upper_9days': {
            'type': BIT,
            'cn': '九阳神功(九连阳)',
            'size': 70,
            'map': 'UPPER_9DAYS'
        },
        'upper_4days': {
            'type': BIT,
            'cn': '四串阳',
            'size': 70,
            'map': 'UPPER_4DAYS'
        },
        'heaven_rule': {
            'type': BIT,
            'cn': '天量法则',
            'size': 70,
            'map': 'HEAVEN_RULE'
        },
        'upside_volume': {
            'type': BIT,
            'cn': '放量上攻',
            'size': 70,
            'map': 'UPSIDE_VOLUME'
        },
        'bearish_engulfing': {
            'type': BIT,
            'cn': '穿头破脚',
            'size': 70,
            'map': 'BEARISH_ENGULFING'
        },
        'reversing_hammer': {
            'type': BIT,
            'cn': '倒转锤头',
            'size': 70,
            'map': 'REVERSING_HAMMER'
        },
        'shooting_star': {
            'type': BIT,
            'cn': '射击之星',
            'size': 70,
            'map': 'SHOOTING_STAR'
        },
        'evening_star': {
            'type': BIT,
            'cn': '黄昏之星',
            'size': 70,
            'map': 'EVENING_STAR'
        },
        'first_dawn': {
            'type': BIT,
            'cn': '曙光初现',
            'size': 70,
            'map': 'FIRST_DAWN'
        },
        'pregnant': {
            'type': BIT,
            'cn': '身怀六甲',
            'size': 70,
            'map': 'PREGNANT'
        },
        'black_cloud_tops': {
            'type': BIT,
            'cn': '乌云盖顶',
            'size': 70,
            'map': 'BLACK_CLOUD_TOPS'
        },
        'morning_star': {
            'type': BIT,
            'cn': '早晨之星',
            'size': 70,
            'map': 'MORNING_STAR'
        },
        'narrow_finish': {
            'type': BIT,
            'cn': '窄幅整理',
            'size': 70,
            'map': 'NARROW_FINISH'
        },
        'limited_lift_f6m': {
            'type': BIT,
            'cn': '限售解禁未来半年',
            'size': 70,
            'map': 'LIMITED_LIFT_F6M'
        },
        'limited_lift_f1y': {
            'type': BIT,
            'cn': '限售解禁未来1年',
            'size': 70,
            'map': 'LIMITED_LIFT_F1Y'
        },
        'limited_lift_6m': {
            'type': BIT,
            'cn': '限售解禁近半年',
            'size': 70,
            'map': 'LIMITED_LIFT_6M'
        },
        'limited_lift_1y': {
            'type': BIT,
            'cn': '限售解禁近1年',
            'size': 70,
            'map': 'LIMITED_LIFT_1Y'
        },
        'directional_seo_1m': {
            'type': BIT,
            'cn': '定向增发近1个月',
            'size': 70,
            'map': 'DIRECTIONAL_SEO_1M'
        },
        'directional_seo_3m': {
            'type': BIT,
            'cn': '定向增发近3个月',
            'size': 70,
            'map': 'DIRECTIONAL_SEO_3M'
        },
        'directional_seo_6m': {
            'type': BIT,
            'cn': '定向增发近6个月',
            'size': 70,
            'map': 'DIRECTIONAL_SEO_6M'
        },
        'directional_seo_1y': {
            'type': BIT,
            'cn': '定向增发近1年',
            'size': 70,
            'map': 'DIRECTIONAL_SEO_1Y'
        },
        'recapitalize_1m': {
            'type': BIT,
            'cn': '资产重组近1个月',
            'size': 70,
            'map': 'RECAPITALIZE_1M'
        },
        'recapitalize_3m': {
            'type': BIT,
            'cn': '资产重组近3个月',
            'size': 70,
            'map': 'RECAPITALIZE_3M'
        },
        'recapitalize_6m': {
            'type': BIT,
            'cn': '资产重组近6个月',
            'size': 70,
            'map': 'RECAPITALIZE_6M'
        },
        'recapitalize_1y': {
            'type': BIT,
            'cn': '资产重组近1年',
            'size': 70,
            'map': 'RECAPITALIZE_1Y'
        },
        'equity_pledge_1m': {
            'type': BIT,
            'cn': '股权质押近1个月',
            'size': 70,
            'map': 'EQUITY_PLEDGE_1M'
        },
        'equity_pledge_3m': {
            'type': BIT,
            'cn': '股权质押近3个月',
            'size': 70,
            'map': 'EQUITY_PLEDGE_3M'
        },
        'equity_pledge_6m': {
            'type': BIT,
            'cn': '股权质押近6个月',
            'size': 70,
            'map': 'EQUITY_PLEDGE_6M'
        },
        'equity_pledge_1y': {
            'type': BIT,
            'cn': '股权质押近1年',
            'size': 70,
            'map': 'EQUITY_PLEDGE_1Y'
        },
        'pledge_ratio': {
            'type': FLOAT,
            'cn': '质押比例',
            'size': 70,
            'map': 'PLEDGE_RATIO'
        },
        'goodwill_scale': {
            'type': BIGINT,
            'cn': '商誉规模',
            'size': 110,
            'map': 'GOODWILL_SCALE'
        },
        'goodwill_assets_ratro': {
            'type': FLOAT,
            'cn': '商誉占净资产比例',
            'size': 70,
            'map': 'GOODWILL_ASSETS_RATRO'
        },
        'predict_type': {
            'type': NVARCHAR(length=10),
            'cn': '业绩预告',
            'size': 70,
            'map': 'PREDICT_TYPE'
        },
        'par_dividend_pretax': {
            'type': FLOAT,
            'cn': '每股股利税前',
            'size': 70,
            'map': 'PAR_DIVIDEND_PRETAX'
        },
        'par_dividend': {
            'type': FLOAT,
            'cn': '每股红股',
            'size': 70,
            'map': 'PAR_DIVIDEND'
        },
        'par_it_equity': {
            'type': FLOAT,
            'cn': '每股转增股本',
            'size': 70,
            'map': 'PAR_IT_EQUITY'
        },
        'holder_change_3m': {
            'type': FLOAT,
            'cn': '近3月股东增减比例',
            'size': 70,
            'map': 'HOLDER_CHANGE_3M'
        },
        'executive_change_3m': {
            'type': FLOAT,
            'cn': '近3月高管增减比例',
            'size': 70,
            'map': 'EXECUTIVE_CHANGE_3M'
        },
        'org_survey_3m': {
            'type': SmallInteger,
            'cn': '近3月机构调研',
            'size': 70,
            'map': 'ORG_SURVEY_3M'
        },
        'org_rating': {
            'type': NVARCHAR(length=10),
            'cn': '机构评级',
            'size': 70,
            'map': 'ORG_RATING'
        },
        'allcorp_num': {
            'type': SmallInteger,
            'cn': '机构持股家数合计',
            'size': 70,
            'map': 'ALLCORP_NUM'
        },
        'allcorp_fund_num': {
            'type': SmallInteger,
            'cn': '基金持股家数',
            'size': 70,
            'map': 'ALLCORP_FUND_NUM'
        },
        'allcorp_qs_num': {
            'type': SmallInteger,
            'cn': '券商持股家数',
            'size': 70,
            'map': 'ALLCORP_QS_NUM'
        },
        'allcorp_qfii_num': {
            'type': SmallInteger,
            'cn': 'QFII持股家数',
            'size': 70,
            'map': 'ALLCORP_QFII_NUM'
        },
        'allcorp_bx_num': {
            'type': SmallInteger,
            'cn': '保险公司持股家数',
            'size': 70,
            'map': 'ALLCORP_BX_NUM'
        },
        'allcorp_sb_num': {
            'type': SmallInteger,
            'cn': '社保持股家数',
            'size': 70,
            'map': 'ALLCORP_SB_NUM'
        },
        'allcorp_xt_num': {
            'type': SmallInteger,
            'cn': '信托公司持股家数',
            'size': 70,
            'map': 'ALLCORP_XT_NUM'
        },
        'allcorp_ratio': {
            'type': FLOAT,
            'cn': '机构持股比例合计',
            'size': 70,
            'map': 'ALLCORP_RATIO'
        },
        'allcorp_fund_ratio': {
            'type': FLOAT,
            'cn': '基金持股比例',
            'size': 70,
            'map': 'ALLCORP_FUND_RATIO'
        },
        'allcorp_qs_ratio': {
            'type': FLOAT,
            'cn': '券商持股比例',
            'size': 70,
            'map': 'ALLCORP_QS_RATIO'
        },
        'allcorp_qfii_ratio': {
            'type': FLOAT,
            'cn': 'QFII持股比例',
            'size': 70,
            'map': 'ALLCORP_QFII_RATIO'
        },
        'allcorp_bx_ratio': {
            'type': FLOAT,
            'cn': '保险公司持股比例',
            'size': 70,
            'map': 'ALLCORP_BX_RATIO'
        },
        'allcorp_sb_ratio': {
            'type': FLOAT,
            'cn': '社保持股比例',
            'size': 70,
            'map': 'ALLCORP_SB_RATIO'
        },
        'allcorp_xt_ratio': {
            'type': FLOAT,
            'cn': '信托公司持股比例',
            'size': 70,
            'map': 'ALLCORP_XT_RATIO'
        },
        'popularity_rank': {
            'type': SmallInteger,
            'cn': '股吧人气排名',
            'size': 70,
            'map': 'POPULARITY_RANK'
        },
        'rank_change': {
            'type': SmallInteger,
            'cn': '人气排名变化',
            'size': 70,
            'map': 'RANK_CHANGE'
        },
        'upp_days': {
            'type': SmallInteger,
            'cn': '人气排名连涨',
            'size': 70,
            'map': 'UPP_DAYS'
        },
        'down_days': {
            'type': SmallInteger,
            'cn': '人气排名连跌',
            'size': 70,
            'map': 'DOWN_DAYS'
        },
        'new_high': {
            'type': SmallInteger,
            'cn': '人气排名创新高',
            'size': 70,
            'map': 'NEW_HIGH'
        },
        'new_down': {
            'type': SmallInteger,
            'cn': '人气排名创新低',
            'size': 70,
            'map': 'NEW_DOWN'
        },
        'newfans_ratio': {
            'type': FLOAT,
            'cn': '新晋粉丝占比',
            'size': 70,
            'map': 'NEWFANS_RATIO'
        },
        'bigfans_ratio': {
            'type': FLOAT,
            'cn': '铁杆粉丝占比',
            'size': 70,
            'map': 'BIGFANS_RATIO'
        },
        'concern_rank_7days': {
            'type': SmallInteger,
            'cn': '7日关注排名',
            'size': 70,
            'map': 'CONCERN_RANK_7DAYS'
        },
        'browse_rank': {
            'type': SmallInteger,
            'cn': '今日浏览排名',
            'size': 70,
            'map': 'BROWSE_RANK'
        },
        'amplitude': {
            'type': FLOAT,
            'cn': '振幅',
            'size': 70,
            'map': 'AMPLITUDE'
        },
        'is_issue_break': {
            'type': BIT,
            'cn': '破发股票',
            'size': 70,
            'map': 'IS_ISSUE_BREAK'
        },
        'is_bps_break': {
            'type': BIT,
            'cn': '破净股票',
            'size': 70,
            'map': 'IS_BPS_BREAK'
        },
        'now_newhigh': {
            'type': BIT,
            'cn': '今日创历史新高',
            'size': 70,
            'map': 'NOW_NEWHIGH'
        },
        'now_newlow': {
            'type': BIT,
            'cn': '今日创历史新低',
            'size': 70,
            'map': 'NOW_NEWLOW'
        },
        'high_recent_3days': {
            'type': BIT,
            'cn': '近期创历史新高近3日',
            'size': 70,
            'map': 'HIGH_RECENT_3DAYS'
        },
        'high_recent_5days': {
            'type': BIT,
            'cn': '近期创历史新高近5日',
            'size': 70,
            'map': 'HIGH_RECENT_5DAYS'
        },
        'high_recent_10days': {
            'type': BIT,
            'cn': '近期创历史新高近10日',
            'size': 70,
            'map': 'HIGH_RECENT_10DAYS'
        },
        'high_recent_20days': {
            'type': BIT,
            'cn': '近期创历史新高近20日',
            'size': 70,
            'map': 'HIGH_RECENT_20DAYS'
        },
        'high_recent_30days': {
            'type': BIT,
            'cn': '近期创历史新高近30日',
            'size': 70,
            'map': 'HIGH_RECENT_30DAYS'
        },
        'low_recent_3days': {
            'type': BIT,
            'cn': '近期创历史新低近3日',
            'size': 70,
            'map': 'LOW_RECENT_3DAYS'
        },
        'low_recent_5days': {
            'type': BIT,
            'cn': '近期创历史新低近5日',
            'size': 70,
            'map': 'LOW_RECENT_5DAYS'
        },
        'low_recent_10days': {
            'type': BIT,
            'cn': '近期创历史新低近10日',
            'size': 70,
            'map': 'LOW_RECENT_10DAYS'
        },
        'low_recent_20days': {
            'type': BIT,
            'cn': '近期创历史新低近20日',
            'size': 70,
            'map': 'LOW_RECENT_20DAYS'
        },
        'low_recent_30days': {
            'type': BIT,
            'cn': '近期创历史新低近30日',
            'size': 70,
            'map': 'LOW_RECENT_30DAYS'
        },
        'win_market_3days': {
            'type': BIT,
            'cn': '近期跑赢大盘近3日',
            'size': 70,
            'map': 'WIN_MARKET_3DAYS'
        },
        'win_market_5days': {
            'type': BIT,
            'cn': '近期跑赢大盘近5日',
            'size': 70,
            'map': 'WIN_MARKET_5DAYS'
        },
        'win_market_10days': {
            'type': BIT,
            'cn': '近期跑赢大盘近10日',
            'size': 70,
            'map': 'WIN_MARKET_10DAYS'
        },
        'win_market_20days': {
            'type': BIT,
            'cn': '近期跑赢大盘近20日',
            'size': 70,
            'map': 'WIN_MARKET_20DAYS'
        },
        'win_market_30days': {
            'type': BIT,
            'cn': '近期跑赢大盘近30日',
            'size': 70,
            'map': 'WIN_MARKET_30DAYS'
        },
        'net_inflow': {
            'type': FLOAT,
            'cn': '当日净流入额',
            'size': 110,
            'map': 'NET_INFLOW'
        },
        'netinflow_3days': {
            'type': BIGINT,
            'cn': '3日主力净流入',
            'size': 110,
            'map': 'NETINFLOW_3DAYS'
        },
        'netinflow_5days': {
            'type': BIGINT,
            'cn': '5日主力净流入',
            'size': 110,
            'map': 'NETINFLOW_5DAYS'
        },
        'nowinterst_ratio': {
            'type': BIGINT,
            'cn': '当日增仓占比',
            'size': 70,
            'map': 'NOWINTERST_RATIO'
        },
        'nowinterst_ratio_3d': {
            'type': FLOAT,
            'cn': '3日增仓占比',
            'size': 70,
            'map': 'NOWINTERST_RATIO_3D'
        },
        'nowinterst_ratio_5d': {
            'type': FLOAT,
            'cn': '5日增仓占比',
            'size': 70,
            'map': 'NOWINTERST_RATIO_5D'
        },
        'ddx': {
            'type': FLOAT,
            'cn': '当日DDX',
            'size': 70,
            'map': 'DDX'
        },
        'ddx_3d': {
            'type': FLOAT,
            'cn': '3日DDX',
            'size': 70,
            'map': 'DDX_3D'
        },
        'ddx_5d': {
            'type': FLOAT,
            'cn': '5日DDX',
            'size': 70,
            'map': 'DDX_5D'
        },
        'ddx_red_10d': {
            'type': SmallInteger,
            'cn': '10日内DDX飘红天数',
            'size': 70,
            'map': 'DDX_RED_10D'
        },
        'changerate_3days': {
            'type': FLOAT,
            'cn': '3日涨跌幅',
            'size': 70,
            'map': 'CHANGERATE_3DAYS'
        },
        'changerate_5days': {
            'type': FLOAT,
            'cn': '5日涨跌幅',
            'size': 70,
            'map': 'CHANGERATE_5DAYS'
        },
        'changerate_10days': {
            'type': FLOAT,
            'cn': '10日涨跌幅',
            'size': 70,
            'map': 'CHANGERATE_10DAYS'
        },
        'changerate_ty': {
            'type': FLOAT,
            'cn': '今年以来涨跌幅',
            'size': 70,
            'map': 'CHANGERATE_TY'
        },
        'upnday': {
            'type': SmallInteger,
            'cn': '连涨天数',
            'size': 70,
            'map': 'UPNDAY'
        },
        'downnday': {
            'type': SmallInteger,
            'cn': '连跌天数',
            'size': 70,
            'map': 'DOWNNDAY'
        },
        'listing_yield_year': {
            'type': FLOAT,
            'cn': '上市以来年化收益率',
            'size': 70,
            'map': 'LISTING_YIELD_YEAR'
        },
        'listing_volatility_year': {
            'type': FLOAT,
            'cn': '上市以来年化波动率',
            'size': 70,
            'map': 'LISTING_VOLATILITY_YEAR'
        },
        'mutual_netbuy_amt': {
            'type': BIGINT,
            'cn': '沪深股通净买入金额',
            'size': 90,
            'map': 'MUTUAL_NETBUY_AMT'
        },
        'hold_ratio': {
            'type': FLOAT,
            'cn': '沪深股通持股比例',
            'size': 70,
            'map': 'HOLD_RATIO'
        },
        'secucode': {
            'type': NVARCHAR(length=10),
            'cn': '全代码',
            'size': 0,
            'map': 'SECUCODE'
        }
    }
}