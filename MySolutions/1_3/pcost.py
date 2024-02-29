def calc_portfolio_cost():
    with open('../../Data/portfolio.dat', 'r') as file:
        total_cost = 0
        for line in file.readlines():
            ticker, shares, cost = line.split(' ')
            total_cost += float(shares) * float(cost)
        print(total_cost)

 
if __name__ == '__main__':
    calc_portfolio_cost()
    
