''' 
As an object-oriented language, Python provides two scopes for attributes: class attributes and instance attributes.

Class attributes
----------------
are the variables defined directly in the class that are shared by all objects of the class.
1.Defined directly inside a class.
2.Shared across all objects.
3.Accessed using class name as well as using object with dot notation, 
    e.g. classname.class_attribute or object.class_attribute
4.Changing value by using classname.class_attribute = value will be reflected to all the objects.	
    Changing value of instance attribute will 

--------------------------------------------------------


Instance attributes
-------------------
are attributes or properties attached to an instance of a class. 
Instance attributes are defined in the constructor.
1.Defined inside a constructor using the self parameter.
2.Specific to object.
3.Accessed using object dot notation e.g. object.instance_attribute
4.Changing value of instance attribute will not be reflected to other objects.

NOTE: 
Method = Function   #These can be used interchangeably
But in class Method/Function are called Member function(in C++)

I PREFER TO USE FUNCTION AS IT IS MATHEMATICALLY CORRECT TERM.


Attributes = variable = properties  #These can be used interchangeably
But in class they are called Data members(in C++)

'''

