from PyQt4 import QtGui

class BasePanel(object):    
    def __init__(self, engine=None):
        self.engine = engine

    def copyPanel(self):
        '''
        This method is used for copying panels and maintain all the setting and variables.
        Should be reimplemented by inhereted panel type
        '''
        return self.__class__(None, engine=self.engine)

    @classmethod
    def panelTypeName(cls):
        '''
        This method is used to get panel type name and display it as window title or tab title
        '''
        raise NotImplementedError

    @classmethod
    def hasNetworkControls(cls):
        '''
        This method is used to determine particular panel type implements network navigation control aka path bar
        '''
        raise NotImplementedError