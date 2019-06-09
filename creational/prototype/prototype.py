"""
Demonstrates Pythonic prototype pattern.

Copyright (c) 2019, Waterlootec, Canada. All rights reserved.

Author: GAN MOHIM.
https://youtu.be/tEUjpmwZbBc
"""
import copy


class Prototype(object):

    def __new__(cls, *args, **kwargs):
        print("__new__ is being called")
        return super(Prototype, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        self.prototype_dict = {}

    def register(self, name, object_to_save):
        self.prototype_dict[name] = object_to_save

    def unregister(self, name):
        del self.prototype_dict[name]

    def clone(self, object_name, **new_object_attributes):
        object_to_copy = self.prototype_dict[object_name]
        cloned_object = copy.deepcopy(object_to_copy)

        # What is __dict__ ?
        # Ref: http://docs.python.org/2/library/stdtypes.html#object.__dict__
        # "A dictionary or other mapping object used
        # to store an object’s (writable) attributes."
        cloned_object.__dict__.update(new_object_attributes)

        return cloned_object


class House(object):
    pass


# A plain house object is being created
house_obj = House()


# Prototype object being created
proto_obj = Prototype()

# We register house_obj so others can clone it
proto_obj.register('house', house_obj)

# Notice that we did not have to write a new class for duplex house
duplex_house_obj = proto_obj.clone('house', door=13, window=9)

# Now, we can create any type of house rapidly
konak_house_obj = proto_obj.clone('house', door=50, window=100, pool=2)

# dir(an_obj) gives you listing of all attributes
# getattr(an_obj, att_name) gets the value of attribute
for dup_att, kon_att in zip(dir(duplex_house_obj), dir(konak_house_obj)):
    print("==")
    print("[Duplex] {}".format(dup_att), getattr(duplex_house_obj, dup_att))
    print("[Konak ] {}".format(kon_att), getattr(konak_house_obj, kon_att))
    print("--")

print(isinstance(duplex_house_obj, House))
print(id(duplex_house_obj) == id(konak_house_obj))