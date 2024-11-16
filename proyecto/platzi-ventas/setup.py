from setuptools import setup



setup(
        name='pv', #se llama pv
        version='0.1', # version de prueba 0.1
        py_modules=['pv'],# se llamara al modulo pv 
        install_requires=[ # necesitamos como requisitos el modulo o lb click
            'Click',
        ], #punto de entrada
        entry_points=''' 
            [console_scripts]
            pv=pv:cli  
        ''',
)
