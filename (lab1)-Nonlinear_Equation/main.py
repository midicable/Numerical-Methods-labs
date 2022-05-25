from methods import*
from convergenceMonitoring import*

root = 1.4776700622632
rootD, itD = dichotomyMethod(1, 2, 10**(-7))
rootS, itS = simpleIteration(2, 10**(-7))
rootN, itN = newtonMethod(2, 10**(-7))
rootC, itC = chebyshevMethod(2, 10**(-7))

print(f'resisualD = {func(rootD)} , itersD = {itD}')
print(f'resisualSI = {func(rootS)} , itersD = {itS}')
print(f'resisualN = {func(rootN)} , itersN = {itN}')
print(f'resisualC = {func(rootC)} , itersC = {itC}')

MSIConvergence(2, 10**(-7), root)
NewtonConvergence(2, 10**(-7), root)
ChebyshevConvergence(2, 10**(-7), root)