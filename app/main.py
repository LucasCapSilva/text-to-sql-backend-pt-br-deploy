from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelWithLMHead, AutoTokenizer
from googletrans import Translator
translator = Translator()
tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-small-finetuned-wikiSQL")
model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-small-finetuned-wikiSQL")

def get_sql(query):
  input_text = "translate English to SQL: %s </s>" % query
  features = tokenizer([input_text], return_tensors='pt')

  output = model.generate(input_ids=features['input_ids'], 
               attention_mask=features['attention_mask'])

  return tokenizer.decode(output[0])

class Item(BaseModel):
    tabela:str
    pesquisa:str
    
    
app = FastAPI()

@app.post("/pesquisa")
async def create_item(item: Item):
    translations  = translator.translate(item.pesquisa, dest='en')
    textTranslator = translations.text
    query = textTranslator
    result = get_sql(query)
    result = result.replace("<pad>", "")
    result = result.replace("</s>", "")
    translations  = translator.translate(item.tabela, dest='en')
    textTranslator = translations.text
    result = result.replace("table",textTranslator)
    
    return {"resultado": result}