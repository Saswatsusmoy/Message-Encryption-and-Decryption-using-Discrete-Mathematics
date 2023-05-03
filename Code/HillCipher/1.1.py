import numpy as np
import scipy.optimize as sco

# Define a function to calculate the portfolio return
def portfolio_return(weights, expected_returns):
    return np.sum(weights * expected_returns)

# Define a function to calculate the portfolio volatility
def portfolio_volatility(weights, expected_returns, covariance_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))

# Define a function to calculate the negative Sharpe ratio
def negative_sharpe_ratio(weights, expected_returns, covariance_matrix, risk_free_rate):
    return - (portfolio_return(weights, expected_returns) - risk_free_rate) / portfolio_volatility(weights, expected_returns, covariance_matrix)

# Define the constraints
def constraints(weights):
    return np.sum(weights) - 1

# Get the expected returns and covariance matrix from the user
expected_returns = np.array(input("Enter the expected returns for each stock, separated by a space: ").split(), dtype=float)
covariance_matrix = np.array(input("Enter the covariance matrix for each stock, separated by a space: ").split(), dtype=float).reshape(len(expected_returns), len(expected_returns))
risk_free_rate = float(input("Enter the risk-free rate: "))
risk_tolerance = float(input("Enter your risk tolerance (a number between 0 and 1): "))

# Optimize the portfolio using the Sharpe ratio as the objective function
weights_bounds = [(0, 1) for i in range(len(expected_returns))]
constraints = ({'type': 'eq', 'fun': constraints})
initial_weights = [1/len(expected_returns) for i in range(len(expected_returns))]
optimized_weights = sco.minimize(fun=negative_sharpe_ratio, x0=initial_weights, args=(expected_returns, covariance_matrix, risk_free_rate), bounds=weights_bounds, constraints=constraints, method='SLSQP')

# Calculate the optimized portfolio return and volatility
optimized_return = portfolio_return(optimized_weights.x, expected_returns)
optimized_volatility = portfolio_volatility(optimized_weights.x, expected_returns, covariance_matrix)

# Print the results
print("Optimized weights:", optimized_weights.x)
print("Optimized return:", optimized_return)
print("Optimized volatility:", optimized_volatility)
print("Optimized Sharpe ratio:", (optimized_return - risk_free_rate) / optimized_volatility)
