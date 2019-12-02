scores = [5, 9.8, 10, 1.2, 6.5, 8.5, 5.5, 7.5, 6, 9.5]
scores.sort()
scores.pop(0)
scores.pop(-1)
average = sum(scores) / len(scores)
print(round(average, 1))
