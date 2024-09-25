#!/usr/bin/env python3

def dyn_generator(oper,state):
    """Generador dinamico.

    Examples:
        >>>sum(np.array(terminar.....................
        (Resultado)

    Args:
        oper (numpy array): First argument
        state (numpy array): Second argument

    Returns:
        numpy array: Retorna la resta entre la multiplicacion de 'oper' y 'state' y la multiplicacion de 'state' y 'oper'.
    """
    return -1.0j*(np.dot(oper,state)-np.dot(state,oper))
