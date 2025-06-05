""" An example of the 'science' theme. """

import numpy as np
import matplotlib.pyplot as plt
import scienceplots  # Required for 'science' style

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))

x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['science', 'ieee', 'no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 20, 50]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.set(xlabel='Voltage (mV)')
    ax.set(ylabel='Current ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig2.pdf')
    fig.savefig('figures/fig2.jpg', dpi=300)