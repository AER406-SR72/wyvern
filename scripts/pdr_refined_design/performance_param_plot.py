import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

from wyvern.data.propellers import PROP_8X8, PROP_9X6, PROP_10X5
from wyvern.performance.models import QuadraticLDModel
from wyvern.performance.plotting import plot_drag_polar, power_plot, thrust_plot

ld_model = QuadraticLDModel(
    c_d0=0.02959, e_inviscid=0.9131, K=0.45, aspect_ratio=5.106458
)
ws = 2.874 * 9.81

# plt.style.use("dark_background")

rcParams["text.usetex"] = True
# use computer modern serif font for all text
rcParams["font.family"] = "serif"

plt.figure(figsize=(4, 3))
power_plot(ld_model, ws, 0.56595, PROP_9X6)
plt.title("Power Performance for 9x6E APC Propeller")
plt.savefig("power_plot.pdf", bbox_inches="tight")

plt.figure(figsize=(4, 3))
thrust_plot(ld_model, ws, 0.56595, PROP_9X6)
plt.title("Thrust Performance for 9x6E APC Propeller")
plt.axvline(x=ld_model.v_ldmax(ws), color="C2", linestyle="--")
plt.axvline(x=10, color="C3", linestyle="--")
plt.text(
    ld_model.v_ldmax(ws) - 0.1,
    3,
    "v$_{LD, \mathrm{max}}$" + f" = {ld_model.v_ldmax(ws):.2f} m/s",
    ha="right",
    va="bottom",
    rotation=90,
    color="C2",
)
plt.text(
    10.1,
    3,
    "v$_{\mathrm{cruise}}$ = 10 m/s",
    ha="left",
    va="bottom",
    rotation=90,
    color="C3",
)

plt.savefig("thrust_plot.pdf", bbox_inches="tight")

plot_drag_polar(ld_model)
plt.savefig("drag_polar.pdf", bbox_inches="tight")

# plot L/D with CL, and L^1.5/D

cL_range = np.linspace(0, 1.2, 100)
cD_range = ld_model.c_D(cL_range)
ld = cL_range / cD_range
ld_15 = cL_range**1.5 / cD_range
plt.figure(figsize=(4, 3))
plt.plot(cL_range, ld, label="$$C_L/C_D$$")
plt.plot(cL_range, ld_15, label="$$C_L^{1.5}/C_D$$")

plt.xlabel("$C_L$")
plt.ylabel("Dimensionless")

plt.grid(linewidth=0.5, alpha=0.5)
plt.title("Performance parameters")
plt.legend()
plt.savefig("clcd15.pdf", bbox_inches="tight")
