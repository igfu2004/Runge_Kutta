def rk4(func, oper, state, h):
    """Implementacion del metodo Runge-Kutta de 4to orden.
        
    Examples:
        >>>sum(np.array([[0,1],[1,0]]), np.array([[1,0],[0,0]]))
        -1,0j*np.array([[0,-1],[1,0]])
        >>>rk4(dyn_generator,[[0 1],[1 0]],[[0.14078653+0.j         0.+0.34774213j],[0.-0.34774213j 0.85921347+0.j]],0.10101010101010101)
        [[0.0756005+0.j         0.       +0.26427933j],[0.       -0.26427933j 0.9243995+0.j]]

    Args:
        func (numpy array): First argument
        oper (numpy array): Second argument
        state (numpy array): Third  argument
        h (float): Fourth argument

    Returns:
        numpy array: Retorna una matriz con los datos evaluados por medio de la ecuacion de Runge-Kutta 4to orden.
    """
    k1 = h*func(oper,state)
    k2 = h* func(oper+ (h/2), state+ (k1/2))
    k3 = h* func(oper + (h/2), state + (k2/2))
    k4 = h*func(oper+h,state+k3)
    return state + (1/6)* (k1+2*k2+2*k3+k4)
