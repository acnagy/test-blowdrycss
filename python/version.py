""" Defines the version of the project. Use ``method 3`` described in this reference for single sourcing the version.
    Reference: https://packaging.python.org/en/latest/single_source_version/#single-sourcing-the-version

    Only set the __version__ global variable in this module.

    How to access __version__ externally from settings.py, conf.py, and so on.

    >>> current_version = {}
    >>> with open('version.py') as file:
    >>>     exec(file.read(), current_version)
    >>> current_version['__version__']
    'x.x.x'

    | Uses a modified version of the pre-release version format defined in PEP 440.
    | Reference: https://www.python.org/dev/peps/pep-0440/#pre-releases

    **__version__ format:**

    ``X.Y.Z``

    **__release__ formats:**

    +------------+-------------------+
    | ``0.0.Za`` | Alpha release     |
    +------------+-------------------+
    | ``0.Y.Zb`` | Beta release      |
    +------------+-------------------+
    | ``X.Y.Zrc``| Release Candidate |
    +------------+-------------------+
    | ``X.Y.Z``  | Final release     |
    +------------+-------------------+

    **Incrementing Rules:**

    - When X and Y are both 0 the project is Alpha
    - When only X is 0 the project is Beta

    - The numbers are only incremented never decremented.

    - Z may not be greater than 9
    - Y may not be greater than 9
    - X may grow into infinity.

    - When Z increments beyond 9 Y is incremented by 1 and Z is reset to 0.
    - When Y increments beyond 9 X is incremented by 1 and both Y and Z is reset to 0.
    - When X increments both Y and Z is reset to 0.

"""
__author__ = 'chad nelson'

__project__ = 'blow dry css'

__version__ = '0.0.4'

__release__ = __version__ + 'a'