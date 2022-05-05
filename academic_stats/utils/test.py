from parsers.parser import PubMedParser
from academic_stats.utils.processors import affiliations_processor

import os

pubmed = PubMedParser("/Users/ghoshk1/Downloads/pubmed_and_arxiv_data/pubmed//")
os.chdir("utils")
for i, author in enumerate(pubmed):
    if author.countries == set([]):
        pass
    else:
        print(author)
