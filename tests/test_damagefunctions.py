from damagefunctions import damagefunctions

def test_pistrika_US_2010_block():
    assert damagefunctions.pistrika_US_2010_block_group(1,1) == 0.497
