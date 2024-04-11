# easy-sample-creator-app
A simple Python data sample creation app for generating data samples from excel flatfiles.
This app can be used for an easy and fast sample creation.
Possible use cases:
- sample creation when conducting audits / compliance checks of a subset of cases from a larger base dataset or similar


## Features

- **User Authentication:** Users are required to login with their role ('poweruser' or 'defaultuser').
- **File Selection:** Users can browse their system to select an Excel file containing data.
- **Create Sample Data:** Users can create sample data from the selected Excel file by clicking the "Create Sample Data" button.
- **Limited Runs:** Users with the 'defaultuser' role have a limited number of runs (3) for creating sample data.

## Installation

1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Install the required dependencies:
   - pip install Pillow
4. Run the application
   - python main.py


