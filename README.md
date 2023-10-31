# Image Generator

To get started, fork this repository

Create a local installation of MindsDB following this [guide](https://docs.mindsdb.com/contribute/install#installing-mindsdb)

After, do `pip install mindsdb[openai]`

Run this command to configure openai

CREATE ML_ENGINE openai_engine
FROM openai
USING
    api_key = 'your-openai-api-key';

Then run the app using `python main.py`

Happy Image Generating!


