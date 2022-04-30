from parsers.parser import PubMed
from utils.processors import affiliations_processor

import os

pubmed = PubMed("/Users/ghoshk1/Downloads/pubmed_and_arxiv_data/pubmed//")
os.chdir("utils")
for i, author in enumerate(pubmed):
    if author.countries == set([]):
        pass
    else:
        print(author)
