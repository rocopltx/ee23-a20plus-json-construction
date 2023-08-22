# ee23-a20plus-json-construction
One-off Python script to prepare the DDR A20PLUS songlist for the Eclipse (nee Eclipse East) 2023 tournament. It takes the `a20plus.json` file as input and iterates through all charts in each song to initialize an "mtgColor" attribute to "uncolored", and outputs the changed file as `ee23_a20plus.json`.

# Setup and Execution
1. Clone the repo
2. Create a Python 3.10.6 (near-zero dependencies, so latest version should be ok) virtual environment.
3. Run `python main.py` to execute the script.