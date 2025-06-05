""" An example of the 'science' theme. """

import numpy as np
import matplotlib.pyplot as plt
import scienceplots  # Required for 'science' style

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))

x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['science', 'no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig1.pdf')
    fig.savefig('figures/fig1.jpg', dpi=300)

# import numpy as np
# import matplotlib.pyplot as plt
# print(plt.rcParams["text.usetex"])  # 检查是否启用 LaTeX
# import scienceplots  # Required for 'science' style
#
# # # 禁用 LaTeX，改用默认文本渲染
# # plt.rcParams.update({
# #     "text.usetex": False,  # 禁用 LaTeX
# #     "font.family": "serif",  # 使用衬线字体（类似 LaTeX）
# #     "font.serif": ["Times New Roman"],  # 指定字体
# # })
#
# def model(x, p):
#     return x ** (2 * p + 1) / (1 + x ** (2 * p))
#
#
# x = np.linspace(0.75, 1.25, 201)
#
# plt.style.use(['science', 'no-latex'])  # 使用 science 风格但不依赖 LaTeX  # Apply the style globally (alternative to context)
# # Or use context:
# # with plt.style.context(['science']):
# fig, ax = plt.subplots()
# for p in [10, 15, 20, 30, 50, 100]:
#     ax.plot(x, model(x, p), label=p)
# ax.legend(title='Order')
# ax.set(xlabel='Voltage (mV)')
# ax.set(ylabel='Current ($\mu$A)')
# ax.autoscale(tight=True)
#
# # Save (ensure 'figures' directory exists)
# import os
#
# os.makedirs('figures', exist_ok=True)
# fig.savefig('figures/fig1.pdf')
# fig.savefig('figures/fig1.jpg', dpi=300)
# plt.show()