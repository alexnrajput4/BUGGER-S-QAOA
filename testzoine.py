import numpy as np
def make_problem(n: int = 8, seed: int = 7):
    rng = np.random.default_rng(seed)
    mu = rng.uniform(0.02, 0.20, n)
    a = rng.normal(size=(n, n)) * 0.1
    sigma = a @ a.T + np.diag(rng.uniform(0.01, 0.05, n))
    return mu, sigma
mu, sigma = make_problem(n=3, seed=42)

print("mu (Returns):\n", mu)
print("\nsigma (Covariance/Risk):\n", sigma)