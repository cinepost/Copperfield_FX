from PyQt5 import QtGui
import moderngl


class ContextManager:
    ctx = None
    qt_ctx = None

    @staticmethod
    def get_default_context(allow_fallback_standalone_context=True) -> moderngl.Context:
        '''
        Default context
        '''

        if ContextManager.ctx is None:
            try:
                ContextManager.ctx = moderngl.create_context()
            except moderngl.Error:
                if allow_fallback_standalone_context:
                    ContextManager.ctx = moderngl.create_standalone_context()
                else:
                    raise

        return ContextManager.ctx

    @staticmethod
    def get_qt_context(window=None):
        if ContextManager.qt_ctx is None and window:
            try:
                ContextManager.qt_ctx = QtGui.QOpenGLContext(window)
            except:
                raise

        return ContextManager.qt_ctx

