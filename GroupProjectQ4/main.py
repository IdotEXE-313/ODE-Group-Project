import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def bn(n):
    f1 = lambda x: (np.sin(2*x)**2 - 1) * np.cos(n*x)
    bn, _ = quad(f1,0,2*np.pi)
    return bn / np.pi

def yn(n):
    f2 = lambda x: (np.sin(2*x)**2 - 1) * np.sin(n*x)
    yn, _ = quad(f2, 0, 2*np.pi)
    return yn / np.pi

def model(alpha, theta, r=1.5, R=10): #set r to 1, R to 2 by default (they can be anything as long as 0 < r < R). N is also 20 by default

    n=4
    init_val = bn(0) / 2
    r_plus = (alpha + np.sqrt(alpha**2 + 4*n**2)) / 2
    r_minus = (alpha - np.sqrt(alpha**2 + 4*n**2)) / 2

    init_val += ((bn(n) * np.cos(n*theta) + yn(n) * np.sin(n*theta)) * (r**(r_minus) - r**(r_plus))/R**n)
    return init_val

theta_vals = np.linspace(0, 2*np.pi, 200)
r_vals = np.linspace(1, 2, 100)  
alpha_vals = [0,0.5,1,1.5,2]

fig, axes = plt.subplots(1, len(alpha_vals), figsize=(15,5), subplot_kw={'projection':'polar'})
theta, r = np.meshgrid(theta_vals, r_vals)

for i, alpha in enumerate(alpha_vals):
    Z = np.zeros_like(r)
    
    # Fill Z(r, theta)
    for j in range(len(r_vals)):
        for k in range(len(theta_vals)):
            Z[j, k] = model(alpha, theta_vals[k], r=r_vals[j])

    ax = axes[i]
    c = ax.contourf(theta, r, Z, levels=50)
    ax.set_title(f"alpha = {alpha}")

plt.show()









    
    

