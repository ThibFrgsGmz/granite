# External includes
# Import the Beautiful Soup library to scrape information from XML files
import bs4 as bs
import markdown_generator as mg

# Internal includes
from granite.generator.c_wrapper import CFileWrapper
from granite.generator.md_wrapper import MarkDownFileWrapper

HEADER_TABLE_MD = { "Name":         mg.Alignment.CENTER, 
                    "Description":  mg.Alignment.LEFT, 
                    "Value":        mg.Alignment.CENTER, 
                    "Type":         mg.Alignment.CENTER, 
                    "Min":          mg.Alignment.CENTER, 
                    "Max":          mg.Alignment.CENTER} 

class IcdXmlAnalysis():
    """
    Analyze the XML file
    """

    def __init__(
        self,
        xml_to_scrape: str,
        icd_file_name_generated: str,
        icd_source_c_generated: str
    ) -> None:
        """
        Method for initializing the object instance
        """

        # Open the ICD to analyze
        with open(xml_to_scrape, "r") as fp:
            # Soup the XML page, i.e. parse xml into a soup data structure
            soup = bs.BeautifulSoup( fp, "lxml")

            # Create a Markdown file object for output
            self.md = MarkDownFileWrapper(filename= ".\\examples\\output\\PROJECT_A\\0.0.0\\"+"README.md")

            # Create a C header file object for output
            self.h_file = CFileWrapper(filename = ".\\examples\\output\\PROJECT_A\\0.0.0\\"+ "H_SOURCE.h")

            # Get the tag of all data streams with the uplink class
            uplink_data_stream = soup.find('uplink_data_stream')

            # Find all the tc tags
            telecommands = uplink_data_stream.find_all('tc')
            
            # For all telecommands
            for telecommand in (telecommands):
                # Parse the telecommand
                self._parse_tc(telecommand)

    def _parse_tc(
        self,
        telecommand: bs.element.Tag
    ) -> None:
        """
        Method for parsing a telecommand

        :param telecommand: Input telecommand object
        """

        # Find the telecommand name
        tc_name = self._get_tag_content( telecommand, 'tc_name')

        # Write the telecommand name
        self.md.write_heading(tc_name, 1)

        # Find all the descriptions of the telecommand
        tc_description  = self._get_tag_content( telecommand, 'tc_description')

        # Write the telecommand description
        self.md.writeline(tc_description)

        # Find the telecommand name
        tc_fields = telecommand.find_all('field')

        # Write the header of the telecommad table
        self.md.write_header_table(HEADER_TABLE_MD)

        # Find the telecommand name
        structure_name_c = self._get_tag_content( telecommand, 'tc_tag_name')

        # Instantiate a list to retrieve all field of a telecommand
        members = []

        # Parse all the field of the TC
        self._parse_tc_fields(tc_fields, members)

        # Populate the C Structure into the C Header file
        self.h_file.populate_structure(structure_name_c, members)

        # Write the table content into the md file
        self.md.write_table()
        # Write the structure into the header file
        self.h_file.write_structure()

        # Write the source code into the md file
        structure   =   self.h_file.get_c_structure()

        # Write the C structure into the Markdown file
        self.md.write_source_code(tc_name, structure)

    def _parse_tc_fields(
        self, 
        tc_fields: bs.element.ResultSet,
        members: list
    ) -> None:
        """
        Method for parsing a telecommand

        :param telecommand: Input telecommand object
        """

        # Instantiate a dictionary to retrieve all field of the telecommand
        dict_field = {}

        # For each filed of the structure
        for field in tc_fields:

            # Parse the telecommand field
            self._parse_tc_field(field, members, dict_field)

            # Append the field dictionnary into a table for the Markdown output file
            self.md.append_table(dict_field)

    def _parse_tc_field(
        self,
        field: bs.element.Tag,
        members: list,
        dict_field: dict
    ) -> None:
        """
        Method for parsing a telecommand field

        :param field: Input telecommand field
        :param members: members telecommand field
        :param dict_field: Output dictionary to retrieve all field characteristics
        """
        # Find the telecommand name
        dict_field["field_name"] = self._get_tag_content( field, 'field_name')
        
        # Find the telecommand description
        dict_field["field_description"] = self._get_tag_content( field, 'field_description')

        # Find the telecommand name
        dict_field["field_value"] = self._get_tag_content( field, 'field_value')

        # Find the telecommand name
        dict_field["field_type"] = self._get_tag_content( field, 'field_type')

        # Find the telecommand name
        dict_field["field_min"] = self._get_tag_content( field, 'field_min')

        # Find the telecommand name
        dict_field["field_max"] = self._get_tag_content( field, 'field_max')

        # Find the telecommand name
        field_name_c = self._get_tag_content(field, 'field_tag_name')

        # Add the field (name and type) as a member of the C structure.
        members.append( dict(   ctype = dict_field["field_type"],
                                name = field_name_c   
                            )
                        )
    
    def _get_tag_content(
        self,
        tag: bs.element.Tag,
        name: str
    ) -> str:
        """
        Method for getting the text of the first tag name of the upper tag.

        :param tag: Upper Tag
        :param name: name of the lower tag
        """

        # Find all the "name" in the tag
        tags_found = tag.find_all(name)

        # Return the text of the tag
        return tags_found[0].text
