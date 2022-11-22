"""
Class responsible for generating and returning various cost functions that has been defined
"""

class CostfunctionGenerator():
    #declare and/or instantiate class attributes
    __some_attr = None

    def __init__(self):
        #declare and/or instantiate instance attributes by the help of self
        return None


    @classmethod
    def some_classmethod(cls) -> any:
        #access class attributs by the help of cls.
        return None

    def cost_function1(self, scr:int, dst:int, d:dict) -> int:
        full_length = min(attr.get('full_length', 0) for attr in d.values())
        shadow_length = min(attr.get('shadowed_part_length', 1) for attr in d.values())
        result = (shadow_length/full_length) + (full_length/shadow_length)
        return result

    def cost_function2(self, scr:int, dst:int, d:dict) -> int:
        full_length = min(attr.get('full_length', 0) for attr in d.values()) 
        shadow_length = min(attr.get('shadowed_part_length', 0) for attr in d.values())
        sunny_length = full_length-shadow_length
        result = (full_length*0.8) + (sunny_length*1.2)
        return result



    #def get_cost_function1() -> function:
    #    return CostfunctionGenerator().cost_function1()