"""UnionFind.py

Union-find data structure. Based on Josiah Carlson's code,
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/215912
with significant additional changes by D. Eppstein.

M. Liedloff changes in the "union" function
heaviest = max([(self.weights[r],r) for r in roots])[1]
to
heaviest = max([(self.weights[r],r) for r in roots], key=lambda x: x[0])[1]

M. Liedloff adds 'sets' and '__str__' methods
"""

class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def __str__(self):
        """Build a string representig the set of sets."""
        return "{"+",".join([str(set(s)) for s in self.sets()])+"}"
	
    def sets(self):
        """Return the set of sets contained in this structure."""
        # build a dict D indexed by the names of sets in this structure
        D = dict()
        for x in self:
            p = self[x]
            if p not in D:
                D[p] = set()
            D[p].add(x)
        # return the set of (frozen)sets
        return { frozenset(x for x in D[s]) for s in D}


    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots], key=lambda x: x[0])[1]
        
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest
