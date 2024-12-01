import yfinance as yf
#import alphavantage as av
import numpy as np
import matplotlib.pyplot as plt
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit_algorithms.minimum_eigensolvers import NumPyMinimumEigensolver

def quantum_portfolio_optimization(num_assets, lambda_risk, initial_capital=1, max_assets=3):
    """
    Perform portfolio optimization with a budget constraint and visualize allocation.

    Parameters:
        num_assets (int): Number of assets in the portfolio.
        lambda_risk (float): Risk aversion parameter.
        initial_capital (float): Total capital to allocate.
        max_assets (int): Maximum number of assets allowed in the portfolio.

    Returns:
        dict: Results including selected portfolio, expected return, and risk.
    """

    
    np.random.seed(128) 
    
    returns = np.random.uniform(0.05, 0.2, num_assets)
    cov_matrix = np.random.uniform(0.001, 0.01, (num_assets, num_assets))
    cov_matrix = (cov_matrix + cov_matrix.T) / 2  
    np.fill_diagonal(cov_matrix, np.random.uniform(0.005, 0.02, num_assets))

    qp = QuadraticProgram()

    
    for i in range(num_assets):
        qp.binary_var(f"x{i}")

    
    linear_coeffs = {f"x{i}": -returns[i] for i in range(num_assets)}  
    quadratic_coeffs = {
        (f"x{i}", f"x{j}"): lambda_risk * cov_matrix[i][j]
        for i in range(num_assets) for j in range(num_assets)
    }
    qp.minimize(linear=linear_coeffs, quadratic=quadratic_coeffs)


    qp.linear_constraint(

        linear={f"x{i}": 1 for i in range(num_assets)},  
        sense="==", 
	rhs=max_assets,
        name="budget_constraint"
    )

    qubo_converter = QuadraticProgramToQubo()
    qp_qubo = qubo_converter.convert(qp)
    
    operator, offset = qp_qubo.to_ising()

    solver = NumPyMinimumEigensolver()
    result = solver.compute_minimum_eigenvalue(operator)
    
    statevector = result.eigenstate.data
    probabilities = np.abs(statevector) ** 2  
    max_prob_index = np.argmax(probabilities) 
    binary_decision = f"{max_prob_index:0{num_assets}b}"      
    
    selected_assets = [i for i, bit in enumerate(binary_decision) if bit == "1"]
    allocation = [initial_capital / len(selected_assets) if i in selected_assets else 0 for i in range(num_assets)]
    

    portfolio_return = sum(returns[i] * allocation[i] for i in range(num_assets))
    portfolio_risk = sum(
        allocation[i] * allocation[j] * cov_matrix[i][j]
        for i in range(num_assets) for j in range(num_assets)
    )
    risk_free_rate = 0.03
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_risk

    
    
    plt.figure(figsize=(10, 6))
    plt.bar(range(num_assets), allocation, color="blue", alpha=0.7)
    plt.xlabel("Asset Index")
    plt.ylabel("Capital Allocation")
    plt.title("Portfolio Allocation")
    plt.xticks(range(num_assets), [f"Asset {i}" for i in range(num_assets)])
    plt.show()

    return {
        "selected_assets": selected_assets,
        "allocation": allocation,
        "portfolio_return": format(portfolio_return*100,".3f"),
        "portfolio_risk": format(portfolio_risk*100,".3f"),
        "sharpe_ratio": format(sharpe_ratio,".2f")
    }

# Example
result = quantum_portfolio_optimization(num_assets=10, lambda_risk=0.5)

# Print the results
print("Selected Assets:", result["selected_assets"])
print("Capital Allocation:", result["allocation"])
print("Portfolio Return:", result["portfolio_return"])
print("Portfolio Risk:", result["portfolio_risk"])
print("Sharpe Ratio:", result["sharpe_ratio"])

lambdas = np.linspace(0.1, 2.0, 20)  # Range of lambda_risk values
frontier = []
for lam in lambdas:
    result = quantum_portfolio_optimization(num_assets=10, lambda_risk=lam)
    frontier.append((result["portfolio_risk"], result["portfolio_return"]))

# Plot Efficient Frontier
risks, returns = zip(*frontier)
plt.plot(risks, returns, marker="o")
plt.xlabel("Portfolio Risk")
plt.ylabel("Portfolio Return")
plt.title("Efficient Frontier")
plt.show()
