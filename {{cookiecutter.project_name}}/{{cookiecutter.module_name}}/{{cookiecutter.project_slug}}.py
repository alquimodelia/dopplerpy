# Use this file to describe the datamodel handled by this module
# we recommend using abstract classes to achieve
#   proper service and interface insulation
from abc import ABC  # , abstractmethod

class MyModel(ABC):
   """
   A class that represents a model.

   Attributes
   ----------
   p1 : str
       Description of the attribute

   Methods
   -------
   my_method(p2)
       Description of the method
   """

   def __init__(self, p1: str = "whatever"):
       """
       Constructor method.

       Parameters
       ----------
       p1 : str, optional
           Description of the parameter, by default "whatever"
       """
       pass

   def my_method(self, p2: int = 0) -> float:
       """
       This method does something.

       Parameters
       ----------
       p2 : int, optional
           Description of the parameter, by default 0

       Returns
       -------
       float
           Description of the return value

       Raises
       ------
       MyException
           When something strange happens
       """
       assert 0 < p2 < 100, "parameter out of range"
       return pow(p2 / 100, 2)
