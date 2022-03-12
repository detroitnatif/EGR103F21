# %% Import modules
from tri_calc import triangles
import matplotlib.pyplot as plt
import numpy as np

# %% Open file for diary
fo = open("tri_diary.txt", "w")


# %% Command to print to screen and save to file
def scrsave(string):
    print(string, end="")
    fo.write(string)


# %% Seed based on NetID
NetID = input("NetID: ")
seed = 0
for code in map(ord, NetID):
    seed = seed + code

np.random.seed(seed)

# %% Run and print results of test
n_test = 4

scrsave("Running tests for user {}\n".format(NetID))
for k in range(n_test):
    scrsave("Test {}: ".format(k + 1))
    try:
        a = np.random.randint(1, 11)
        b = np.random.randint(1, 11)
        c = np.random.randint(abs(a - b) + 1, a + b)
        out = triangles(a, b, c, True, k + 1)
        fig = plt.figure(k + 1)
        ax = fig.axes[0]
        ax.set_title("Test {} for {}".format((k + 1), NetID))
        fig.tight_layout()
        fig.savefig("TriPlotTest{}.png".format(k + 1))
        scrsave(
            "runs: triangles({:2}, {:2}, {:2})".format(a, b, c)
            + " returns ({:0.3e}, {:0.3e}, {:0.3e})".format(*out)
        )
    except Exception as ex:
        scrsave("failed: {}".format(ex))
    scrsave("\n")

# %% Close diary file
fo.close()
