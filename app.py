import os
import openai
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy import text
from helpers.helpers import combine_prompts, prompt_input


openai.api_key = os.getenv('OPENAI_API_KEY')


df = pd.read_csv("sales_data_sample.csv")
# print(df.groupby("QTR_ID").sum()['SALES'])


# temporary db in ram, pushing df into the temp db
temp_db = create_engine('sqlite://', echo=False)
data = df.to_sql(name = 'Sales', con=temp_db)


# with temp_db.connect() as conn:
#     result = conn.execute((text("SELECT * FROM Sales")))
#     rows = result.fetchall()
#     print(rows)

nlp_text = prompt_input()


response = openai.Completion.create(
    model='text-davinci-002',
    prompt=combine_prompts(df, nlp_text),
    temperature=0,
    max_tokens=150,
    frequency_penalty=0,
    presence_penalty=0,
    stop=['#', ';']
)

print(response)