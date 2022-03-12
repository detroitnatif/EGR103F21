import numpy as np
import matplotlib.pyplot as plt


def singularity(x, a, n):
    return (x > a) * ((x - a) ** n)


if __name__ == "__main__":
    x = np.linspace(-2, 5, 500)
    fig = plt.figure(num=1, clear=True)
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(
        x, singularity(x, -1, 0), "k-",
        x, singularity(x, 0, 1), "r--",
        x, singularity(x, 1, 1), "g-.",
        x, singularity(x, 3, 2), "b:",
    )
    ax.legend(labels=["$<x+1>^0$", "$<x>^1$", "$<x-1>^1$", "$<x-3>^2$"], loc="best")
    ax.set(title="Four Different Values of $y=<x-a>^n$ (NetID)", xlabel="x", ylabel="y")
    ax.grid(True)
    fig.tight_layout()
    fig.savefig("SingPlots.png")
