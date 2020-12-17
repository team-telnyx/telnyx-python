if [[ $PYTHON_VERSION == '2.7' ]]; then make lint; fi
if [[ $PYTHON_VERSION == '3.7' ]]; then make fmtcheck; fi
