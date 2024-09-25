#!/usr/bin/env python3

def dyn_generator(oper,state):
    """Generador dinamico.

    Examples:
        >>>sum(np.array([[0,1],[1,0]]), np.array([[1,0],[0,0]]))
        -1,0j*np.array([[0,-1],[1,0]])

    Args:
        oper (numpy array): First argument
        state (numpy array): Second argument

    Returns:
        numpy array: Retorna la resta entre la multiplicacion de 'oper' y 'state' y la multiplicacion de 'state' y 'oper' en ese orden exactamente multiplicado por -i.
    """
    return -1.0j*(np.dot(oper,state)-np.dot(state,oper))
