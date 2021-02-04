#getting index value from dict

nums = [3,2,3]

hash_ds = { i : i for i in nums }  # comprehensioon to make dict from list
value_needed = 2
list(hash_ds.keys()).index(value_needed)  # index value of required value needed
