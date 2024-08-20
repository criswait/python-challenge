**Overview**
This project is a collection of Python challenges designed to analyze data and generate reports based on CSV files. The project is organized into two main challenges: PyPoll and PyBank. Each challenge is contained in its own directory, with separate folders for input data (Resources) and output reports (Analysis).


**Project Structure**
python-challenge/
│
├── PyPoll/
│   ├── Resources/
│   │   └── election_data.csv
│   │
│   ├── Analysis/
│   │   └── PyPoll_analysis.txt
│   │
│   └── main.py 
│
└── PyBank/
    ├── Resources/
    │   └── budget_data.csv
    │
    ├── Analysis/
    │   └── PyBank_analysis.txt
    │
    └── main.py

**PyPoll**
Input: election_data.csv located in the Resources folder.
Output: A summary of the election results saved as PyPoll_analysis.txt in the Analysis folder.
Script: The analysis is performed by main.py, which processes the CSV file and generates the report.

**PyBank**
Input: budget_data.csv located in the Resources folder.
Output: A summary of the financial analysis saved as PyBank_analysis.txt in the Analysis folder.
Script: The analysis is performed by main.py, which processes the CSV file and generates the report.

**How to Run the Scripts**
1. Navigate to the Challenge Directory:
For PyPoll: Navigate to the PyPoll directory.
For PyBank: Navigate to the PyBank directory.

2.Ensure Input Data is in the Correct Location:
The input CSV files should be located in the Resources folder for each challenge.

3. Execute the Script: python3 main.py
Run the main.py script using Python 3.

4. Check the Output:
The analysis results will be printed to the console and saved in the Analysis folder as a text file (PyPoll_analysis.txt or PyBank_analysis.txt).

**Notes**
- The project assumes that the working directory is set to the respective challenge directory (PyPoll or PyBank). If the script is run from a different directory, the paths may need to be adjusted.
- Ensure that Python 3 is installed on your system.

**Disclaimer**
This readme.txt file was generated with the assistance of ChatGPT. While the content has been customized to fit the project, the initial draft was created using AI.

