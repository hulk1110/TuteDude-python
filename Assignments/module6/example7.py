#frozen sets (immutaable sets)

fs1= frozenset({10,24,15})
print(fs1)
print(type(fs1))
# since frozen sets are immuatable below line will throw errors
fs1.add(40)
print(fs1)