# this adds the names of arctic indigenous peoples as an entity ruler to a medium sized
# model that already recognises the entities that we want such as taxa etc. 

import spacy

#nlp = spacy.load('./models/biospacy_en_md_LOC_int')
# note, using the medium model does not overwrite the ents completely is an issue
#nlp = spacy.load('en_core_web_sm')

nlp = spacy.load('en_core_web_lg')

config = {
   "phrase_matcher_attr": None,
   "validate": True,
   "overwrite_ents": True,
   "ent_id_sep": "||",
}

ruler = nlp.add_pipe("entity_ruler", config=config).from_disk("./peoples/circumpolar_peoples_patterns_lower_lemma.jsonl")


#from spacy.pipeline import EntityRuler
#ruler = EntityRuler(nlp, validate=True, overwrite_ents=True).from_disk("./peoples/circumpolar_peoples_patterns_lower_lemma.jsonl")
#new_ruler = nlp.add_pipe("entity_ruler").from_disk("./peoples/circumpolar_peoples_patterns_lower_lemma.jsonl")
#nlp.add_pipe('ruler')
#print(nlp.pipe_names)

text = "reindeer, saami, sami, circumpolar people, circumpolar peoples, Eskimo, eskimos, Inuit, inuits, inuit, Beluga whale, whale shark, polar bear, Escherichia coli, Banisteriopsis caapi, virus, Oldham 2108, (Oldham, 2018), stenolis sp, London, England, forest, savannah, Ebolavirus, Nairobi, Masai Mara, Johannesburg"
doc = nlp(text)

print([(ent.text, ent.label_) for ent in doc.ents])
nlp.to_disk("models/iplc_en_lg_arctic")
