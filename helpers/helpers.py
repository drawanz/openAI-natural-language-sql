def create_table_definition(df):
    prompt = """### sqlite SQL table, with this properties:
    #
    # Sales({})
    """.format(",".join(str(col for col in df.columns)))
    return prompt


def prompt_input():
    nlp_text = input("Enter the info you want: ")
    print(nlp_text)
    return nlp_text


def combine_prompts(df, query_prompt):
    definition = create_table_definition(df)
    query_init_string = f"### A query to answer: {query_prompt}\nSELECT"
    return definition+query_init_string
