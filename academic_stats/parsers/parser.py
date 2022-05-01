from academic_stats.utils.types import Author
from academic_stats.utils.processors import affiliations_processor, name_processor
from xml.etree import ElementTree
import glob


class generic_parser:
    def __init__(self, path_to_dir):
        self.path = path_to_dir
        self.files = glob.glob(f"{self.path}/*.xml")

    def __iter__(self):
        """
        Processes the next xml file and yields an author object
        """
        for file in self.files:
            self.curr_file = file

            try:
                xml_data = self._get_xml_root(file)
            except ElementTree.ParseError:
                # Ignore file
                continue

            authors = self._get_authors(xml_data)
            for author in authors:
                name = name_processor(self._get_name(author))
                countries = []
                for affiliation in self._get_affiliations(author):
                    countries.extend(affiliations_processor(affiliation.text))
                yield Author(name, set(countries))

    def _get_xml_root(self, file: str):
        tree = ElementTree.parse(file)
        return tree

    def _get_authors(self, xml_data):
        raise NotImplementedError

    def _get_name(self, xml_data):
        raise NotImplementedError

    def _get_affiliations(self, xml_data):
        raise NotImplementedError


class PubMed(generic_parser):
    def _get_authors(self, xml_data):
        authors = xml_data.findall(".//Author")
        return authors

    def _get_name(self, xml_data):
        """
        If we don't find the tags we return an empty string as the name
        """
        forename, initials, lastname = " ", " ", " "
        try:
            forename = xml_data.find("ForeName").text
            initials = xml_data.find("Initials").text
            lastname = xml_data.find("LastName").text
        except AttributeError:
            pass
            #  print(f"Author tag without ForeName Initials LastName {e}")
        return f"{forename} {initials} {lastname}"

    def _get_affiliations(self, xml_data):
        return xml_data.findall(".//Affiliation")


class Arxiv(generic_parser):
    def _get_authors(self, xml_data):
        authors = xml_data.findall(".//{http://www.w3.org/2005/Atom}author")
        return authors

    def _get_name(self, xml_data):
        return xml_data.find("{http://www.w3.org/2005/Atom}name").text

    def _get_affiliations(self, xml_data):
        return xml_data.findall(
            ".//arxiv:affiliation", {"arxiv": "http://arxiv.org/schemas/atom"}
        )
