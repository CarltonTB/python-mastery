def calc_portfolio_cost(path):
    with open(path, 'r') as file:
        total_cost = 0
        for line in file.readlines():
            split = line.split()
            ticker = split[0]
            shares = split[1]
            cost = split[2]
            try:
                total_cost += int(shares) * float(cost)
            except ValueError as e:
                print('Could not parse:', line.strip())
                print('Reason:', e)
        print(total_cost)

 
if __name__ == '__main__':
    calc_portfolio_cost('../../Data/portfolio3.dat')
    
