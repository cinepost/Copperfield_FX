import os, sys, logging, re
import code

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

from copper import hou
from .base_panel import BasePanel

from .python_syntax_highlighter import PythonHighlighter

logger = logging.getLogger(__name__)


class PythonShellPanel(BasePanel):
    def __init__(self):
        BasePanel.__init__(self)
        self.python_shell_widget = PythonShellWidget(self)
        self.syntax = PythonHighlighter(self.python_shell_widget.document())

        self.addWidget(self.python_shell_widget)

    @classmethod
    def panelTypeName(cls):
        return "Python Shell"

    @classmethod
    def hasNetworkControls(cls):
        return False


class PythonShellWidget(QtWidgets.QTextEdit):

    class InteractiveInterpreter(code.InteractiveInterpreter):
        def __init__(self, locals):
            code.InteractiveInterpreter.__init__(self, locals)
        def runIt(self, command):
            logger.debug("run cmd: %s" % command)
            code.InteractiveInterpreter.runsource(self, command)

    def __init__(self,  parent):
        QtWidgets.QTextEdit.__init__(self, parent)
        self.setObjectName("PythonShellWidget")

        sys.stdout              = self
        sys.stderr              = self
        self.refreshMarker      = False # to change back to >>> from ...
        self.multiLine          = False # code spans more than one line
        self.command            = ''    # command to be ran
        self.printBanner()              # print sys info
        self.marker()                   # make the >>> or ... marker        
        self.history            = []    # list of commands entered
        self.historyIndex       = -1
        self.interpreterLocals  = {"hou": hou}

        # initilize interpreter with self locals
        self.initInterpreter(locals())
    
    def printBanner(self):
        self.write(sys.version)
        self.write(' on ' + sys.platform + '\n')
        self.write('CopperFX python interpreter on PyQt ' + QtCore.PYQT_VERSION_STR + '\n')
        msg = 'Type !hist for a history view and !hist(n) history index recall'
        self.write(msg + '\n')

    def marker(self):
        if self.multiLine:
            self.insertPlainText('... ')
        else:
            self.insertPlainText('>>> ')

    def initInterpreter(self, interpreterLocals=None, parent=None):
        if interpreterLocals:
            # when we pass in locals, we don't want it to be named "self"
            # so we rename it with the name of the class that did the passing
            # and reinsert the locals back into the interpreter dictionary
            selfName = interpreterLocals['self'].__class__.__name__
            interpreterLocalVars = interpreterLocals.pop('self')
            self.interpreterLocals[selfName] = interpreterLocalVars
        else:
            self.interpreterLocals = interpreterLocals
        self.interpreter = self.InteractiveInterpreter(self.interpreterLocals)

    def updateInterpreterLocals(self, newLocals):
        className = newLocals.__class__.__name__
        self.interpreterLocals[className] = newLocals

    def write(self, line):
        self.insertPlainText(line)
        self.ensureCursorVisible()

    def clearCurrentBlock(self):
        # block being current row
        length = len(self.document().lastBlock().text()[4:])
        if length == 0:
            return None
        else:
            # should have a better way of doing this but I can't find it
            [self.textCursor().deletePreviousChar() for x in xrange(length)]
        return True

    def recallHistory(self):
        # used when using the arrow keys to scroll through history
        self.clearCurrentBlock()
        if self.historyIndex > -1 or self.historyIndex < -1:
            self.insertPlainText(self.history[self.historyIndex])
        return True

    def customCommands(self, command):

        if command == '!hist': # display history
            self.append('') # move down one line
            # vars that are in the command are prefixed with ____CC and deleted
            # once the command is done so they don't show up in dir()
            backup = self.interpreterLocals.copy()
            history = self.history[:]
            history.reverse()
            for i, x in enumerate(history):
                iSize = len(str(i))
                delta = len(str(len(history))) - iSize
                line = line  = ' ' * delta + '%i: %s' % (i, x) + '\n'
                self.write(line)
            self.updateInterpreterLocals(backup)
            self.marker()
            return True

        if re.match('!hist\(\d+\)', command): # recall command from history
            backup = self.interpreterLocals.copy()
            history = self.history[:]
            history.reverse()
            index = int(command[6:-1])
            self.clearCurrentBlock()
            command = history[index]
            if command[-1] == ':':
                self.multiLine = True
            self.write(command)
            self.updateInterpreterLocals(backup)
            return True

        return False

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            # proper exit
            self.interpreter.runIt('exit()')

        if event.key() == Qt.Key_Down:
            if self.historyIndex == len(self.history):
                self.historyIndex -= 1
            try:
                if self.historyIndex > -1:
                    self.historyIndex -= 1
                    self.recallHistory()
                else:
                    self.clearCurrentBlock()
            except:
                pass
            return None

        if event.key() == Qt.Key_Up:
            try:
                if len(self.history) - 1 > self.historyIndex:
                    self.historyIndex += 1
                    self.recallHistory()
                else:
                    self.historyIndex = len(self.history)
            except:
                pass
            return None

        if event.key() == Qt.Key_Home:
            # set cursor to position 4 in current block. 4 because that's where
            # the marker stops
            blockLength = len(self.document().lastBlock().text()[4:])
            lineLength  = len(self.document().toPlainText())
            position = lineLength - blockLength
            textCursor  = self.textCursor()
            textCursor.setPosition(position)
            self.setTextCursor(textCursor)
            return None

        if event.key() in [Qt.Key_Left, Qt.Key_Backspace]:
            # don't allow deletion of marker
            if self.textCursor().positionInBlock() == 4:
                return None

        if event.key() in [Qt.Key_Return, Qt.Key_Enter]:
            # set cursor to end of line to avoid line splitting
            textCursor = self.textCursor()
            position   = len(self.document().toPlainText())
            textCursor.setPosition(position)
            self.setTextCursor(textCursor)

            line = str(self.document().lastBlock().text())[4:] # remove marker
            line.rstrip()
            self.historyIndex = -1

            if self.customCommands(line):
                return None
            else:
                try:
                    line[-1]
                    self.haveLine = True
                    if line[-1] == ':':
                        self.multiLine = True
                    self.history.insert(0, line)
                except:
                    self.haveLine = False

                if self.haveLine and self.multiLine: # multi line command
                    self.command += line + '\n' # + command and line
                    self.append('') # move down one line
                    self.marker() # handle marker style
                    return None

                if self.haveLine and not self.multiLine: # one line command
                    self.command = line # line is the command
                    self.append('') # move down one line
                    self.interpreter.runIt(self.command)
                    self.command = '' # clear command
                    self.marker() # handle marker style
                    return None

                if self.multiLine and not self.haveLine: #  multi line done
                    self.append('') # move down one line
                    self.interpreter.runIt(self.command)
                    self.command = '' # clear command
                    self.multiLine = False # back to single line
                    self.marker() # handle marker style
                    return None

                if not self.haveLine and not self.multiLine: # just enter
                    self.append('')
                    self.marker()
                    return None
                return None

        # allow all other key events
        super(PythonShellWidget, self).keyPressEvent(event)