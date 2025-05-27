## Usage

- Install TWS API (tested for >= version 10.30.01) in a fresh environment (and activate)
- In RTD-Translator\ directory, run `python app.py`
- Enter contract identifier when prompted (or 'exit' to end the program)
- Enter Topic string if desired (default = Last)
- The RTD formula will be printed to stdout
- It will loop around, asking for contract identifier, until you type 'exit'

Security types implemented: "STK", "FUND", "IND", "BOND", "CFD", "CMDTY", "CASH", "FUT", "OPT", "FOP", "WAR"