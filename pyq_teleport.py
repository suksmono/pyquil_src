# -*- coding: utf-8 -*-
"""
Quantum Teleportation
Created on Sun May 27 09:54:57 2018
@author: Suksmono

 **** TELEPORTATION CIRCUIT ****

0:       |y> -- o --|H|--|M|==========
                |                    ||  
1:       |0> --(+)-------|M|==       ||
                             ||      ||
2:       |0> --------------|X^M2|--|Z^M1|-----> |y>

"""

import pyquil.quil as pq
from pyquil.gates import H, CNOT, Z, X
import pyquil.api as api

qvm=api.QVMConnection()

qprog = pq.Program()

'''
prepare entangled qubits
1:|0> --|H|--o----- |q0>
             |
2:|0> ------(+)---- |q1>

'''
qprog.inst(H(1), CNOT(1,2))

'''
creating |psi>: teleported qubit
|psi> = 1/sqrt(2)* [|0> - |1>]

circuit:    
0: |0> --|H|--|Z|--> |psi>
'''
qprog.inst(H(0), Z(0), CNOT(0,1),H(0))
#          ^^^   ^^^
#          |psi>     
'''
>> COMPLETE CIRCUIT :
0: |0> --|H|--|Z|-->> |y> -- o --|H|--|M|=======
                             |                 ||  
1: |0> ---------------------(+)-------|M|==    ||
                                          ||   ||
2: |0> -----------------------------------|X|--|Z|-->> |y>

'''
qprog.measure(0,0).measure(1,1).if_then(1,X(2)).if_then(0,Z(2))

print("\nReceived qubit:")
print(qvm.wavefunction(qprog,[0,1]))
'''
RESULT: (0.7071067812+0j)|011> + (-0.7071067812+0j)|111>
                          ^                         ^
                 -> 1/(sqrt(2))[ |0> - |1> ]
'''


