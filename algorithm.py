import numpy as np
import random

def generate_numbers(total_growth_rate, num_numbers=100, base=1.0):
    # 计算平均增长率
    mean_growth_rate = total_growth_rate / num_numbers

    # 使用正态分布生成增长率
    growth_rates = np.random.normal(mean_growth_rate, mean_growth_rate / 2.0, num_numbers)

    # 初始化数字列表
    numbers = [base]

    # 生成数字
    for growth_rate in growth_rates:
        numbers.append(numbers[-1] * (1 + growth_rate))

    return numbers

def generate_numbers_random(start=1, number=1000, growth_mean=0.003, growth_range=0.05):
    numbers = [start]
    for _ in range(1, number):
        growth = random.uniform(growth_mean - growth_range, growth_mean + growth_range)
        next_number = numbers[-1] * (1 + growth)
        numbers.append(next_number)
    return numbers


if __name__ == "__main__":
    #print(generate_numbers2(6))
    #print(np.random.uniform(0, 2))
    # 生成一组包含两个以上波峰或波谷，整体增长幅度为1.0的数字
    #numbers = generate_numbers_with_peaks(n=100, growth_rate=2.0, peaks_valleys=4)
    # 生成数据
    # 生成数据
    data = generate_numbers2()


    print(data)