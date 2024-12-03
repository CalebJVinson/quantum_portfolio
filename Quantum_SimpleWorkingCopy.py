import numpy as np
from qiskit_optimization import QuadraticProgram
from qiskit_algorithms.minimum_eigensolvers import NumPyMinimumEigensolver

def quantum_portfolio_optimization(returns, covariance, lambda_risk):
    """
    Perform portfolio optimization using a classical solver for testing.

    Parameters:
        returns (list): Expected returns for the assets.
        covariance (list of lists): Covariance matrix of the assets.
        lambda_risk (float): Risk aversion parameter.

    Returns:
        dict: Optimal portfolio decision and objective value.
    """
    qp = QuadraticProgram()

    num_assets = len(returns)
    for i in range(num_assets):
        qp.binary_var(f"x{i}")

    
    linear_coeffs = {f"x{i}": -returns[i] for i in range(num_assets)}  
    quadratic_coeffs = {
        (f"x{i}", f"x{j}"): lambda_risk * covariance[i][j]
        for i in range(num_assets) for j in range(num_assets)
    }
    qp.minimize(linear=linear_coeffs, quadratic=quadratic_coeffs)


    operator, offset = qp.to_ising()

    
    solver = NumPyMinimumEigensolver()
    result = solver.compute_minimum_eigenvalue(operator)
    
    
    statevector = result.eigenstate.data
    probabilities = np.abs(statevector) ** 2  
    max_prob_index = np.argmax(probabilities)  
    binary_decision = f"{max_prob_index:0{num_assets}b}"  

    selected_assets = [i for i, bit in enumerate(binary_decision) if bit == "1"]

    portfolio_return = sum(returns[i] for i in selected_assets)
    portfolio_risk = sum(
        covariance[i][j] for i in selected_assets for j in selected_assets
    )

    return {
        "selected_assets": selected_assets,
        "portfolio_return": portfolio_return,
        "portfolio_risk": portfolio_risk,
        "minimum_value": result.eigenvalue + offset,
    }

returns = [0.1, 0.2]
covariance = [[0.005, 0.002], [0.002, 0.006]]
lambda_risk = 0.5

result = quantum_portfolio_optimization(returns, covariance, lambda_risk)

print("Selected Assets:", result["selected_assets"])
print("Portfolio Return:", result["portfolio_return"])
print("Portfolio Risk:", result["portfolio_risk"])
print("Minimum Value:", result["minimum_value"])
print("Minimum Value:", result["minimum_value"])
