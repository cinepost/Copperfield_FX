#!/bin/bash

function check_sip {
    python -c "exec(\"import sip\")"  &> /dev/null
    [ $? -eq 0 ]
}

function check_pyqt4 {
    python -c "exec(\"import PyQt4\")"  &> /dev/null
    [ $? -eq 0 ]
}

if check_sip; then
    echo "SIP already installed. All good!"
else
    read -p "No SIP inatalled!"
fi  

if check_pyqt4; then
    echo "PyQt4 already installed. All good!"
else
    read -p "No PyQt4 inatalled!"
fi