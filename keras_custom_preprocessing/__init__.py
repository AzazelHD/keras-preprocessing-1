"""Enables dynamic setting of underlying Keras module.
"""

_KERAS_BACKEND = None
_KERAS_UTILS = None


def set_keras_submodules(backend, utils):
    # Deprecated, will be removed in the future.
    global _KERAS_BACKEND
    global _KERAS_UTILS
    _KERAS_BACKEND = backend
    _KERAS_UTILS = utils


def get_keras_submodule(name):
    # Deprecated, will be removed in the future.
    if name not in {'backend', 'utils'}:
        raise ImportError(
            'Can only retrieve "backend" and "utils". '
            'Requested: %s' % name)
    if _KERAS_BACKEND is None:
        raise ImportError('You need to first `import keras` '
                          'in order to use `keras_custom_preprocessing`. '
                          'For instance, you can do:\n\n'
                          '```\n'
                          'import keras\n'
                          'from keras_custom_preprocessing import image\n'
                          '```\n')
    if name == 'backend':
        return _KERAS_BACKEND
    elif name == 'utils':
        return _KERAS_UTILS


__version__ = '1.1.2'
