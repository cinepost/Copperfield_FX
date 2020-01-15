from enum import IntEnum

class attribType(IntEnum):
    Point = 0
    Prim = 1
    Vertex = 2
    Global = 3

class attribData(IntEnum):
    Int = 0
    Float = 1
    String = 2

class Attrib():
    def __init__(self, geometry, attrib_type: attribType, name: str, default_value, transform_as_normal=False, create_local_variable=True):
        if type(default_value) in (tuple, list):
            self._attr_size = len(default_value)
            value_check = default_value
        else:
            self._attr_size = 1
            value_check = [default_value]

        assert all(isinstance(x, (int, float, str)) for x in value_check), "Wrong default_value type !"
        
        self._geometry = geometry
        self._attrib_type = attrib_type
        self._name = name
        self._defaul_value = default_value
        self._transform_as_normal = transform_as_normal
        self._create_local_variable = create_local_variable

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        if isinstance(other, str):
            return self._name == other
        return self._name == other._name

    def type(self) -> attribType:
        return self._attrib_type

    def isArrayType(self) -> bool:
        '''
        Return True if the attribute is a type that contains array data (i.e. Float Array, Integer Array, String Array) and False otherwise.
        '''

        return self._is_array

    def defaultValue(self) -> int or float or str or tuple:
        '''
        Return the attribute’s default value.
        '''
        return self._defaul_value