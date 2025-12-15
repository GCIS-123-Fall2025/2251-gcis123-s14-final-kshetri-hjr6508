"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""
def sort_key( value ):
    return value.get_item_code()
class Item:
    __slots__ = [ '__itemcode', '__name', '__price' ]
    def __init__( self, itemcode, name, price ):
        self.__itemcode = itemcode
        self.__name = name
        self.__price = price
    def get_item_code( self ):  return self.__itemcode
    def get_name( self ): return self.__name
    def get_price( self ):  return self.__price
    def __eq__(self, value):
        if type(self) == type(value):
            return self.__itemcode == value.__itemcode
    def __hash__(self):
        return hash( self.__itemcode )
    def __repr__(self):
        return '(' + self.__itemcode + ', ' + self.__name + ', ' + str(self.__price) + ')'


# manual test from main() method
def main():
    i1 = Item( "ABCD-1234", "Sliky Camisole", 24 )
    i2 = Item( "ABCD-1234", "Sliky Camisole", 25 )
    i3 = Item( "EFGH-5678", "Choclate Milk", 24 )
    print( "item 1 == item 2", i1 == i2 )
    print( "item 1 == item 3", i1 == i3 )
    test_list = [ i3, i1, i2, ]
    print( "list", test_list )
    test_set = { i1, i2, i3 }
    print( "set", test_set )

    print( "sorted", sorted( test_list, key=sort_key ) )


if __name__ == "__main__":    main()