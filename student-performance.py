import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("StudentsPerformance.csv")
math_scores = df["math score"]
fig = ff.create_distplot([math_scores.tolist()], ["Math Test Scores"], show_hist=False)
# fig.show()

mean = statistics.mean(math_scores)
median = statistics.median(math_scores)
mode = statistics.mode(math_scores)
std_dev = statistics.stdev(math_scores)

dev_strt, dev_end = mean - std_dev, mean + std_dev
dev_strt2, dev_end2 = mean - 2 * std_dev, mean + 2 * std_dev
dev_strt3, dev_end3 = mean - 3 * std_dev, mean + 3 * std_dev

stdev1 = [result for result in math_scores if result > dev_strt and result < dev_end]
stdev2 = [result for result in math_scores if result > dev_strt2 and result < dev_end2]
stdev3 = [result for result in math_scores if result > dev_strt3 and result < dev_end3]

print(f"The Mean of the math scores is: {mean:.2f}")
print(f"The Median of the math scores is: {median:.2f}")
print(f"The Mode of the math scores is: {mode:.2f}")

print(f"{len(stdev1)/len(math_scores)*100:.2f}% of data for math scores lies in 1 standard deviation")
print(f"{len(stdev2)/len(math_scores)*100:.2f}% of data for math scores lies in 2 standard deviations")
print(f"{len(stdev3)/len(math_scores)*100:.2f}% of data for math scores lies in 3 standard deviations")
