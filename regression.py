from matplotlib import pyplot
#y = 2x + 3
x = [1,2,3,4,5]
y = [5, 7, 8, 11 , 14]

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)
x_minus_mean_x_2 = [(item - mean_x)**2 for item in x]
y_minus_mean_y_multiplied_x_minus_mean_x= [(a - mean_x)*(b - mean_y) for (a,b) in zip(x,y)]

# y = mx + c
# m = sum(x_minus_mean_x) * sum(y_minus_mean_y) / sum(x_minus_mean_x_2)
# c = y - mx (mean_y - m* mean_x)

m = sum(y_minus_mean_y_multiplied_x_minus_mean_x) / sum(x_minus_mean_x_2)
c = mean_y - m* mean_x

line_plotted_y = [m*x_iter + c for x_iter in x]
pyplot.scatter(x, y)
pyplot.plot(x, line_plotted_y, '-r')
pyplot.scatter(mean_x, mean_y)
pyplot.show()