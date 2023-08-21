from datetime import timedelta, date
import os, time
from influxdb_client_3 import InfluxDBClient3, Point, WritePrecision
import numpy as np

# 业务指标相关信息
indices = [['IND_00000001','交易金额'], ['IND_00000002','交易笔数'], ['IND_00000003','交易笔均'], ['IND_00000004','发卡量'], ['IND_00000005','卡均交易笔数'], ['IND_00000006','卡均交易金额']]
dimensions_a = ['T0', 'T1', 'T2', 'T3'] # 卡等级
dimensions_b = ['北方银行', '南方银行', '东部商业银行', '西部投资银行', '滨江区银行']
dimensions_c = ['Wechat', 'Alipay', 'JDPay','ATM','POS','OB']

start_date = date(2023, 1, 1)
end_date = date(2023, 3, 1)

token = os.getenv('INFLUXDB_TOKEN')
org = "Xiaowen Deployed"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org, verify_ssl=False)

database="Metric"

# 生成业务指标数据
data_points = []

for index in indices:
    for dimension_a in dimensions_a:
        for dimension_b in dimensions_b:
            for dimension_c in dimensions_c:
                d = start_date
                measure_value = 1000
                while d <= end_date:
                    measure_value *= 1 + np.random.uniform(-0.02, 0.05)  # 涨幅随机
                    point = Point(index[1]) \
                        .tag("卡等级", dimension_a) \
                        .tag("发卡银行", dimension_b) \
                        .tag("交易渠道", dimension_c) \
                        .field("值", measure_value) \
                        .time(d.strftime("%Y-%m-%dT%H:%M:%SZ"), WritePrecision.NS)
                    data_points.append(point)
                    d += timedelta(days=1)


client.write(database=database, record=data_points)