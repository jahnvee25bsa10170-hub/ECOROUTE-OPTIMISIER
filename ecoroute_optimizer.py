# I was trying to see how emissions change when you mess with distance/speed etc.

import random
import math
import os

try:
    import matplotlib.pyplot as plt
    _plot_ok = True
except:
    _plot_ok = False
    plt = None


def dist(pt1, pt2):
    # just straight distance, nothing fancy
    x = pt2[0] - pt1[0]
    y = pt2[1] - pt1[1]
    return (x*x + y*y) ** 0.5


def make_routes(a, b, count=5):
    base = dist(a, b)
    out = []
    for i in range(count):
        # I wanted randomness so the plots aren't boring
        f = random.uniform(0.72, 1.58)
        d = round(base * f, 2)

        # I don’t really know how many stops real routes have
        s_lo = int(d * 0.3)
        s_hi = int(d * 1.7)
        if s_lo < 0: s_lo = 0
        if s_hi <= s_lo: s_hi = s_lo + 3

        stops = random.randint(s_lo, s_hi)
        spd = round(random.uniform(9, 102), 2)

        out.append({
            "id": f"R{i+1}",
            "d": d,
            "st": stops,
            "v": spd,
            "co2": None
        })
    return out


def co2_calc(r):
    # very rough CO2 logic I hacked together
    base = 0.21
    per_stop = 0.04

    t = r["d"] * base + r["st"] * per_stop

    # punish slow crawling a bit more
    v = r["v"]
    if v < 25:
        t *= 1.19
    elif v > 92:
        t *= 1.07

    return round(t, 2)


def pick_best(rs):
    # quickest way I remember
    best = rs[0]
    for r in rs[1:]:
        if r["co2"] < best["co2"]:
            best = r
    return best


def plot_routes(rs):
    if not _plot_ok:
        print("No matplotlib. Skipping plot.")
        return

    names = [r["id"] for r in rs]
    cvals = [r["co2"] for r in rs]
    dvals = [r["d"] for r in rs]

    fig, ax = plt.subplots(1, 2, figsize=(11, 5))

    # bar colors
    mn = min(cvals)
    mx = max(cvals)
    cols = []
    for c in cvals:
        if c == mn:
            cols.append("green")
        elif c == mx:
            cols.append("red")
        else:
            cols.append("#7da7c4")

    ax[0].bar(names, cvals, color=cols)
    ax[0].set_title("CO2")

    ax[1].scatter(dvals, cvals, s=70)
    for d, c, n in zip(dvals, cvals, names):
        ax[1].annotate(n, (d, c), xytext=(4, 4), textcoords="offset points")

    os.makedirs("screenshots", exist_ok=True)
    fig.savefig("screenshots/out.png", dpi=180)
    plt.close(fig)


def show(rs):
    print("\n--- route dump ---")
    for r in rs:
        c = r["co2"]
        if c < 3:
            tag = "nice"
        elif c < 4:
            tag = "ok"
        elif c < 5:
            tag = "meh"
        else:
            tag = "bad"

        print(f"{r['id']}: dist={r['d']}km  stops={r['st']}  v={r['v']}  co2={c} ({tag})")


def main():
    a = (0, 0)
    b = (12, 9)

    rs = make_routes(a, b)

    # fill emissions
    for r in rs:
        r["co2"] = co2_calc(r)

    # sort but keep original separate
    ordered = sorted(rs, key=lambda x: x["co2"])

    show(ordered)

    best = pick_best(ordered)
    print("\nbest route:", best["id"], "with", best["co2"], "kg")

    plot_routes(ordered)


if __name__ == "__main__":
    main()
