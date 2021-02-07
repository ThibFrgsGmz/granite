# External includes
from string import Template
from typing import List

template_c_struct = '''
typedef struct __${structname}__ {
${defs}
} Typ${structname};
'''
template_c_struct_field = '''\t$ctype\t\t\t$name;'''

class CStructureGenerator():
    """Generate the language C structure

    """

    def __init__(self) -> None:
        """Initialize the object instance

        """

        self.c_struct           =   {}
        self.struct_members     =   []

        # Initialize a structure template
        self.struct_template    =   Template(template_c_struct)

        # Initialize a structure members template
        self.member_template    =   Template(template_c_struct_field)

    def set_struct_name(self, struct_name: str ) -> None:
        """Set the name of the C structure.

        Parameters
        ----------
        struct_name:
            The name of the structure in C

        """

        self.c_struct['structname'] = struct_name

    def set_struct_members( self, struct_members: List[str]) -> None:
        """Set the members of the C structure.

        Parameters
        ----------
        struct_members:
            List of members of structure in C

        """

        self.c_struct['members'] = struct_members

    def spec_to_struct(self) -> str:
        """Transform the pre-specified structure into the C language format.

        Returns
        -------
        str
            Structure in C language
        """
        # Retrieve structure name
        structname = self.c_struct['structname']
        
        # Retrieve structure members
        member_data = self.c_struct['members']

        # Replace members of the structure according to the defined members template
        members = [self.member_template.substitute(d) for d in member_data]

        # Return the structure by replacing the name and the member according to the defined structure template
        return self.struct_template.safe_substitute(structname = structname, defs = "\n".join(members))