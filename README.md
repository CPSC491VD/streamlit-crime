# streamlit-crime

## Hosted application: [Chicago Crime Analysis](https://chicagocrimeanalytics.streamlit.app/)

**Please note:** Running this app locally requires that the user have a secrets.toml file in their .streamlit/ directory. This file is ignored in the ```.gitignore``` for security reasons due to the fact that it contains credentials for a hosted database.

If you wish to run this application on your local machine, you must reach out to the authors to securely get access to this file in order to run it using Python.

## How to run the application locally:
1. Have Python installed. If not installed, follow the installation steps for your OS. [Python Install](https://www.python.org/downloads/)
2. Create a .venv by running `python -m venv .venv`
3. Activate the .venv
    ```
    .venv\Scripts\activate
    ```
4. Install the requirements.txt `pip install -r requirements.txt`
5. Run the streamlit app at localhost:8501 `streamlit run Home.py`