#!/user/bin/env python3
"""
Documentación de la API de ejemplo

Author: Fortinux
info@fortinux.com
Date: 2023
"""

import asyncio
import ejemploAsyncioAPI


async def enviar_datos(a: str):
    """
    Ejemplo de creación de una API en python.

    Esta API se conecta a ejemploAsyncioAPI
    para obtener datos mediante la función `datos`.

    Parametros
    ----------
    `print` : Imprime una cadena
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
    'Datos:'
    """
    print(f'Enviar datos a {a}...')
    await asyncio.sleep(3)
    print(f'Datos enviados a {a}')


async def main():
    datos = await ejemploAsyncioAPI.datos()
    print('Datos: ', datos)
    # await enviar_datos('Fortinux')
    await asyncio.gather(enviar_datos('Marcelo'), enviar_datos('Fortinux'))


if __name__ == '__main__':
    asyncio.run(main())
