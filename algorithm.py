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


def generate_numbers_with_peaks(n=1000, growth_rate=1.0, peaks_valleys=2):
    # 生成一组正弦波作为基础波动模式
    x = np.linspace(0, peaks_valleys * np.pi, n)
    y = np.sin(x)

    # 为每个值添加随机扰动
    y = [value + random.uniform(-growth_rate, growth_rate) for value in y]
    
    # 将波动模式进行缩放以达到整体增长的幅度
    y = [value * growth_rate for value in y]

    # 生成一个增长的序列，使得整体趋势是增长的
    growth = np.linspace(0, n * growth_rate, n)

    # 将增长的序列和波动模式相加得到最终的序列
    result = y + growth

    return result


def generate_series(length=1000, overall_growth=10.0, num_peaks=3):
    # 初始化一个数组来存储数据
    data = [1.0]

    # 计算每个步骤的平均增长率
    avg_growth_rate = (overall_growth - 1) / length

    # 计算每个波峰或波谷之间的距离
    peak_distance = length // num_peaks

    # 初始化一个变量来跟踪当前的增长率
    current_growth_rate = avg_growth_rate

    for i in range(1, length):
        # 如果当前位置接近波峰或波谷，我们将反转增长率
        if i % peak_distance == 0:
            current_growth_rate *= -1

        # 添加随机波动
        random_factor = np.random.uniform(0.5, 1.5)
        growth_rate = current_growth_rate * random_factor

        # 计算新的值，并添加到数据中
        new_value = data[-1] * (1 + growth_rate)
        data.append(new_value)

    return data

if __name__ == "__main__":
    #print(generate_numbers2(6))
    #print(np.random.uniform(0, 2))
    # 生成一组包含两个以上波峰或波谷，整体增长幅度为1.0的数字
    #numbers = generate_numbers_with_peaks(n=100, growth_rate=2.0, peaks_valleys=4)
    # 生成数据
    data = generate_series(100, 4.0, 2)

    print(data)