set_a={1,2,3}
set_b=set()
print(type(set_a))
set_b.add(4)
print(set_b)
#set_b.remove(5)
print(set_b)
#set_b.#discard(5)
print(set_b)
#if the number is reapeated it will not show
set_c={2,3,2,4,5,5}
print(set_c)

#union or | to put them together
print(set_a.union(set_c))
#intertersection or & to find the common number
print(set_a.intersection(set_c))
#differnce or minus to take it
print(set_a.difference(set_c))
#symmetric difference to take awaay he common elements
print(set_a.symmetric_difference(set_c))


