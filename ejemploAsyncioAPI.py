#!/user/bin/env python3
"""
Documentación de la API

Author: Fortinux
info@fortinux.com
Date: 2023
"""


import asyncio


async def datos() -> str:
    """
    Esta función sirve como ejemplo de API en python.

    Esta función es llamada por ejemploAsyncioAPImain
    para obtener datos de la función `datos`.

    Parametros
    ----------
    `print` : imprime
        Imprime la cadena: Obteniendo datos...

    Returns
    -------
    print
        Explicación del valor de retorno de tipo ``print``.

    Notas
    -----
    Notas si son necesarias.
    En este caso no son necesarias.

    Referencias
    ----------
    Ejemplo de cita: [1]_. Se pueden incluir las citas
    también en la sección notas.

    .. [1] Fortino, Marcelo Horacio, et al. Theoretical framework for Risk
        management monitoring, review and improvement process of FLOSS
        applications using key risk indicators - KRI at a public agency.
        http://47jaiio.sadio.org.ar/sites/default/files/SIE-01.PDF, 2018.

    Ejemplos
    --------
    Escritos en formato doctest, deben explicar como usar la función.    

    >>> print(datos)
    
    """  
    print('Obteniendo datos...')
    await asyncio.sleep(3)
    print('Datos obtenidos!')

    return 'Datos API'
