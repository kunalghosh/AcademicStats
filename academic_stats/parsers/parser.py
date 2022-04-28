from collections import Counter
from utils.types import Author
from utils.processors import affiliations_processor, name_processor
from xml.etree import ElementTree
import glob


class generic_parser:
    def __init__(self, path_to_dir):
        self.path = path_to_dir
        self.files = glob.glob(f"{self.path}/*.xml")

    # def __iter__(self):
    #     return self

    def __iter__(self):
        """
        Processes the next xml file and yields an author object
        """
        for file in self.files:
            xml_data = self._get_xml_root(file)
            authors = self._get_authors(xml_data)
            for author in authors:
                name = name_processor(self._get_name(author))
                countries = [
                    affiliations_processor(_) for _ in self._get_affiliations(author)
                ]
                #  country_count = Counter(countries)
                yield Author(name, set(countries))

    def _get_xml_root(self, file: str):
        tree = ElementTree.parse(file)
        return tree

    def _get_authors(self, xml_data):
        raise NotImplementedError

    def _get_name(self, xml_data):
        raise NotImplementedError

    def _get_affiliation(self, xml_data):
        raise NotImplementedError


class PubMed(generic_parser):
    def _get_authors(self, xml_data):
        authors = xml_data.findall(".//Author")
        return authors

    def _get_name(self, xml_data):
        forename = xml_data.find("ForeName").text
        initials = xml_data.find("Initials").text
        lastname = xml_data.find("LastName").text
        return f"{forename} {initials} {lastname}"

    def _get_affiliations(self, xml_data):
        return xml_data.findall(".//Affiliation")


class Arxiv(generic_parser):
    def _get_authors(self, xml_data):
        authors = xml_data.findall("author")
        return authors

    def _get_name(self, xml_data):
        return xml_data.find("name")

    def _get_affiliation(self, xml_data):
        return xml_data.findall("affiliation")
