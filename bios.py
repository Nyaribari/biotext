import pandas as pd
import spacy

def text_labels(path,model,your_output_name):

    nlp = spacy.load(model)
    df = pd.read_csv(path,usecols=['text','id'])

    tup = list(df.itertuples(index=False, name='meta'))

    entities = []
    for doc, context in list(nlp.pipe(tup, batch_size = 10, as_tuples=True)):
      for ent in doc.ents:
        entities.append(
            {
              
            "id":context, 
            "entity_id":ent.ent_id_,
            "entity_text":ent.text, 
            "entity_label":ent.label_, 
            "entity_start":ent.start_char, 
            "entity_end":ent.end_char,
            "entity_id_no":ent.ent_id 
            }
          )

    entities_df = pd.DataFrame.from_records(entities)
    data_frame = entities_df.to_csv("./"+ str(your_output_name) +".csv") # provide name of your file
    return data_frame




def info():
  print(
    'Biospacy is a package for biological data. The package is built on spaCy. The package version is 0.0.3.\
          Load package with: \
            import biospacy, biospacy.text_labels(), biospacy.info(), biospacy.version()'
  )

def version():
  print(
    'Version 0.0.3'
  )
