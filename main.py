import pandas as pd
import numpy as np
import random

# 定义一个函数来生成涨跌幅度
def generate_percentage_changes(n_periods, baseline=0.02, variability=0.01):
    return [baseline + random.uniform(-variability, variability) for _ in range(n_periods)]

# 定义主函数
def generate_business_metric(start_date, end_date):
    # 生成日期序列
    date_range = pd.date_range(start_date, end_date)
    
    # 生成月度涨跌幅度，考虑到日期范围的长度可能不能被 30 整除
    n_months = (len(date_range) + 29) // 30  # 使用加法和整除来向上取整
    monthly_changes = generate_percentage_changes(n_months)
    
    # 生成季度涨跌幅度，考虑到日期范围的长度可能不能被 90 整除
    n_quarters = (len(date_range) + 89) // 90  # 使用加法和整除来向上取整
    quarterly_changes = generate_percentage_changes(n_quarters)
    
    # 初始化业务指标
    business_metric = 100  # 可以设置为你希望的初始业务指标的值
    
    # 初始化业务指标列表
    business_metrics = [business_metric]
    
    # 生成业务指标数据
    for i, date in enumerate(date_range[1:], 1):
        # 计算当月和当季的涨跌幅度
        monthly_change = monthly_changes[i//30]
        quarterly_change = quarterly_changes[i//90]
        
        # 计算当日业务指标
        if date.month in [3, 6, 9, 12] and date.day == 30:  # 判断是否为季度末
            daily_change = monthly_change + quarterly_change  # 季度末的涨跌幅度为月度和季度的和
        else:
            daily_change = monthly_change  # 其他时间的涨跌幅度为月度涨跌幅度
            
        # 计算当日业务指标
        business_metric *= (1 + daily_change)
        
        # 将当日业务指标添加到列表中
        business_metrics.append(business_metric)
    
    # 创建 DataFrame
    df = pd.DataFrame({'date': date_range, 'business_metric': business_metrics})
    
    return df

# 使用函数生成业务指标数据
df = generate_business_metric('2020-01-01', '2022-12-31')
print(df)