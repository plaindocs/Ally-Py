'''
Created on Mar 21, 2013

@package: ally core
@copyright: 2012 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Gabriel Nistor

Provides representation objects for encoders. 
'''

# --------------------------------------------------------------------

class Property:
    '''
    Representation for a encoded property.
    '''
    __slots__ = ('name', 'flags')
    
    def __init__(self, name, *flags):
        '''
        Construct the property representation.
        
        @param name: string|None
            The property name, a None value means the name is not known or is dynamic by nature.
        @param flags: arguments[object]
            Flag objects specific for property.
        '''
        assert name is None or isinstance(name, str), 'Invalid name %s' % name
        
        self.name = name
        self.flags = flags
        
class Attribute:
    '''
    Representation for a encoded attribute.
    '''
    __slots__ = ('flags',)
    
    def __init__(self, *flags):
        '''
        Construct the attribute representation.
        
        @param flags: arguments[object]
            Flag objects specific for attribute.
        '''
        self.flags = flags
        
class Object:
    '''
    Representation for a encoded object.
    '''
    __slots__ = ('name', 'flags', 'attributes', 'properties')
    
    def __init__(self, name, *flags, attributes=None):
        '''
        Construct the object representation.
        
        @param name: string|None
            The object name, a None value means the name is not known or is dynamic by nature.
        @param flags: arguments[object]
            Flag objects specific for object.
        @param attributes: dictionary{string: Attribute}|None
            The attributes of the object.
        '''
        assert name is None or isinstance(name, str), 'Invalid name %s' % name
        if __debug__:
            if attributes:
                assert isinstance(attributes, dict), 'Invalid attributes %s' % attributes
                for name, attribute in attributes.items():
                    assert isinstance(name, str), 'Invalid name %s' % name
                    assert isinstance(attribute, Attribute), 'Invalid attribute %s' % attribute

        self.name = name
        self.flags = flags
        self.attributes = attributes
        self.properties = []
    
class Collection:
    '''
    Representation for a encoded collection.
    '''
    __slots__ = ('name', 'item', 'flags', 'attributes')
    
    def __init__(self, name, item, *flags, attributes=None):
        '''
        Construct the collection representation.
        
        @param name: string|None
            The collection name, a None value means the name is not known or is dynamic by nature.
        @param item: Object
            The object represented in the collection.
        @param flags: arguments[object]
            Flag objects specific for collection.
        @param attributes: dictionary{string: Attribute}|None
            The attributes of the collection.
        '''
        assert name is None or isinstance(name, str), 'Invalid name %s' % name
        assert isinstance(item, Object), 'Invalid item %s' % item
        if __debug__:
            if attributes:
                assert isinstance(attributes, dict), 'Invalid attributes %s' % attributes
                for name, attribute in attributes.items():
                    assert isinstance(name, str), 'Invalid name %s' % name
                    assert isinstance(attribute, Attribute), 'Invalid attribute %s' % attribute
                    
        self.name = name
        self.item = item
        self.flags = flags
        self.attributes = attributes