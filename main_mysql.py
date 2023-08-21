from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import mysql.connector
from datetime import timedelta, date


# 载入 .env 文件中的环境变量
load_dotenv()

# 通过 os.getenv 访问环境变量
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_ssl_pem = os.getenv('DB_SSL_PEM')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

# 创建数据库引擎
engine = create_engine(f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?ssl_ca={db_ssl_pem}", echo=False)

# 业务指标相关信息
indices = [['IND_00000001','交易金额'], ['IND_00000002','交易笔数'], ['IND_00000003','交易笔均'], ['IND_00000004','发卡量'], ['IND_00000005','卡均交易笔数'], ['IND_00000006','卡均交易金额']]
dimensions_a = ['T0', 'T1', 'T2', 'T3'] # 卡等级
dimensions_b = ['北方银行', '南方银行', '东部商业银行', '西部投资银行', '滨江区银行']
dimensions_c = ['Wechat', 'Alipay', 'JDPay','ATM','POS','OB']

start_date = date(2020, 1, 1)
end_date = date(2023, 6, 30)

# 生成业务指标数据
data = []
for index in indices:
    for dimension_a in dimensions_a:
        for dimension_b in dimensions_b:
            for dimension_c in dimensions_c:
                d = start_date
                measure_value = 1000
                while d <= end_date:
                    measure_value *= 1 + np.random.uniform(-0.02, 0.05)  # 涨幅随机
                    data.append([
                        index[0],
                        index[1],
                        dimension_a,
                        dimension_b,
                        dimension_c,
                        '',
                        '',
                        '',
                        '',
                        measure_value,
                        'Daily',
                        d
                    ])
                    d += timedelta(days=1)

# 将数据转换为 DataFrame
df = pd.DataFrame(data, columns=[
    'index_id',
    'index_name',
    'dimension_a',
    'dimension_b',
    'dimension_c',
    'dimension_d',
    'dimension_e',
    'dimension_f',
    'dimension_g',
    'measure_value',
    'update_frequency',
    'rpt_dte'
])

# 将数据插入到 MySQL 数据库中
df.to_sql('ads_kronos_mul_index', con=engine, if_exists='append', index=False)
#print(df)