from sys import stdin

def bestItem(weights, values):
    maxAverage = 0
    bestItem = 0
    
    for i in range (len(values)):
        if weights[i] > 0 and (values[i]/weights[i]) > maxAverage:
            maxAverage = values[i]/weights[i]
            bestItem = i
    return bestItem

def optimal_value(n, capacity, weights, values):
    totalValue = 0
    for _ in range (n):
        if capacity == 0:
            return totalValue
        i = bestItem(weights,values)
        a = min (weights[i],capacity)
        totalValue += a * (values[i]/weights[i])
        weights[i] -=a
        capacity -=a
    return totalValue

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(n, capacity, weights, values)
    print("{:.3f}".format(opt_value))