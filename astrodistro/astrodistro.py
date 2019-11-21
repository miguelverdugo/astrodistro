import numpy as np


def randomvariate(pdf, n, xmin, xmax):
    """
    Create random numbers according to an arbitrary PDF

    Uses the rejection method for generating random numbers derived from an arbitrary   
    probability distribution. For reference, see Bevington's book, page 84. Based on  
    rejection*.py.

    Usage:  
    >>> randomvariate(P,N,xmin,xmax)  
    where  
    P : probability distribution function from which you want to generate random numbers  
    N : desired number of random values  
    xmin,xmax : range of random numbers desired  
    
    Returns:   
    the sequence (ran,ntrials) where  
    ran : array of shape N with the random variates that follow the input P  
    ntrials : number of trials the code needed to achieve N  
   
    Here is the algorithm:  
    - generate x' in the desired range  
    - generate y' between Pmin and Pmax (Pmax is the maximal value of your pdf)  
    - if y'<P(x') accept x', otherwise reject  
    - repeat until desired number is achieved  
   
    Rodrigo Nemmen  
    Nov. 2011  

    """
      x = np.linspace(xmin, xmax, 10000)
      y = pdf(x)
      pmin = y.min()
      pmax = y.max()
      naccept = 0
      ntrial = 0
      ran = []
      while naccept < n:
            x = np.random.uniform(xmin, xmax)
            y = np.random.uniform(pmin, pmax)
            if y <= pdf(x):
                  ran.append(x)
                  naccept = naccept+1
                #  print pdf(x)
            ntrial = ntrial + 1

      ran = np.asarray(ran)
      return ran, ntrial


def schechter_lf(mags, phi=200, Mstar=18., alpha=1):
    return (phi * (10.**(0.4*(1+alpha)*(Mstar-mags)))*np.exp(-10.**(0.4*(Mstar-mags))))

    