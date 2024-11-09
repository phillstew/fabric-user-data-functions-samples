# This is an example of using Fabric AI functions  within a user data function
# Complete these steps before publishing this function 
# 1. Select library managment and add openai==1.42 , synapseml_core= version libraries 

# Fetch the token for the AOAI endpoint.
from trident_token_library_wrapper import PyTridentTokenLibrary
kv_token = mssparkutils.credentials.getToken("keyvault")
aoai_key = PyTridentTokenLibrary.get_secret_with_token(
    "https://aifunc-kv.vault.azure.net/", "aoai-2", kv_token)


# Open the AOAI client.
import openai
client = openai.AzureOpenAI(
    api_key=aoai_key,
    api_version = "2024-02-01",
    azure_endpoint = "https://synapseml-openai-2.openai.azure.com/"
)

# Set the client.
import synapse.ml.aifunc as aifunc
aifunc.setup(client) 
import pandas as pd

from tqdm.auto import tqdm
tqdm.pandas()

# replace <function-name> with a new function name 
@app.function("translate_ai_function")
# replace <function-name> with a new function name 
def translate_ai_function() -> str:
    # use logging.info() to log any information
    logging.info('Python UDF trigger function processed a request.')

    # Translate text:
    df_translate = pd.DataFrame({"input": ["Where is the bus?", "The bus is on the beach."]})
    df_translate["as_greek"] = df_translate["input"].ai.translate("greek")
    df_translate["as_spanish"] = df_translate["input"].ai.translate("spanish")
    df_translate["spanish_via_greek"] = df_translate["as_greek"].ai.translate("spanish")
    display(df_translate)
 
    return f"Python UDF was executed successfully!"
