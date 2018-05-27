#
# classical-quantum interaction
# Bell state: ( |00> + |11> )
#
from pyquil.gates import H, CNOT
from pyquil.quil import Program
from pyquil.api import QVMConnection

#define classical register
creg=0

# repeat simulate coin
pbell=Program(H(0),CNOT(0,1))
# define virtual quantum machine (remote)
qsim=QVMConnection()

#
wf=qsim.wavefunction(pbell)

# before measurement
print("Before measurement H|0>= ", qsim.wavefunction(pbell))

# after measurement
pbell.measure(0,creg)
for x in range(5):
    print("After measurement: ", qsim.wavefunction(pbell))
    print("Prob = ", wf.get_outcome_probs())
