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
    """
    Generate the language C structure
    """

    def __init__(self) -> None:
        """
        Initialize the object instance
        """

        self.c_struct           =   {}
        self.struct_members     =   []
        self.struct_template    =   Template(template_c_struct)
        self.member_template    =   Template(template_c_struct_field)

    def set_struct_name(self, struct_name: str ) -> None:
        self.c_struct['structname'] = struct_name

    def set_struct_members( self, struct_members : List[str]) -> None:
        self.c_struct['members'] = struct_members

    def spec_to_struct(self) -> str:

        structname = self.c_struct['structname']
        member_data = self.c_struct['members']

        members = [self.member_template.substitute(d) for d in member_data]
        return self.struct_template.safe_substitute(structname = structname, defs = "\n".join(members))