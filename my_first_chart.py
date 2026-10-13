import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic" #윈도우는 Malgun Gothic
prices = [1000, 2000, 1500, 3000, 3500]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
        xytext=(0, 8), ha="center")
ax.set_title("내 첫 그래프")
fig.savefig("my_first_chart.png")