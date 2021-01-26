import numpy as np
import matplotlib.pyplot as plt
import os.path
import pandas as pd
from get_dowJones_data import get_dowJones_data

# get dow jones data, using custom class
dfDowjones_returns = pd.read_csv("DowJones_Returns.csv")

### Question 2

# compute mean and variance/covariance matrix:
dfMu = dfDowjones_returns.mean()
dfCov = dfDowjones_returns.cov() 

# construct inverse covariance matrix
Sigma_inv = np.linalg.inv(dfCov)

def calc_param_frontier(Sigma_inv, dfMu):
    # get parameter n, and i (vector of 1s)
    N = len(dfMu.index) 
    i = np.ones(N)
        
    # Define A, B, C , D
    A = np.transpose(i) @ Sigma_inv @ dfMu     
    B = np.transpose(dfMu) @ Sigma_inv @ dfMu     
    C = np.transpose(i) @ Sigma_inv @ i  
    D = B*C - A**2

    return A, B, C , D

def calc_stdev_frontier(A, C, D, mu):
     return np.sqrt(1/C + C/D * (mu - A/C)**2)

A, B, C, D = calc_param_frontier(Sigma_inv, dfMu)

# generate some values for mu, these are target portfolio returns:
mu_p = np.linspace(-0.01,0.01,1000)
sigma_p = calc_stdev_frontier(A, C, D, mu_p)



# ### Question 3
mu_zp = 0.005
sigma_zp = calc_stdev_frontier(A,C,D, mu_zp)
mu_gmv = A/C


def slope_zp(mu_zp, sigma_zp, C, D, mu_gmv):

    top = D*sigma_zp
    diff = mu_zp - mu_gmv
    bottom = C * diff

    return top/bottom

# Define tangent line
def zp_line(sigma_p, mu_zp, sigma_zp, C, D, mu_gmv):
    slope_line = slope_zp(mu_zp, sigma_zp, C, D, mu_gmv)
    line = slope_line*(sigma_p - sigma_zp) + mu_zp
    return(line)


slope =  slope_zp(mu_zp, sigma_zp, C, D, mu_gmv)

# Define x data range for tangent line
sigma_range = np.linspace(sigma_zp-0.01, sigma_zp+0.01, 10)
tangent_zp = zp_line(sigma_range, mu_zp,sigma_zp, C, D, mu_gmv)

# plot efficient frontier and individual assets
plt.scatter(np.sqrt(np.diag(dfCov.loc[:, dfCov.columns != '^DJI'])),dfMu[1:],
              label='Stocks', color = 'red')
plt.scatter(np.sqrt(np.diag(dfCov.loc[:, dfCov.columns == '^DJI'])),dfMu[1],
              color='green', label='Dow Jones Index')
plt.plot(sigma_p, mu_p, color='black', label='Efficient Frontier')
plt.legend()
plt.plot(sigma_range, tangent_zp)
plt.xlabel(r'$\sigma_p$')
plt.ylabel(r'$\bar{\mu_p}}$',rotation=0)
plt.title('Efficient Frontier + Stocks in the Dow Jones Index')
plt.show()
