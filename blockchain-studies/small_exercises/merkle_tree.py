
import hashlib
from itertools import zip_longest


class Node(object):
    def __init__(self, datum, data=None, children=None):
        self.parent = None
        self.datum = datum.encode('utf-8')
        self.children = []
        # only for leaf nodes
        self.data = data

    def __repr__(self):
        return str(self.datum)

    def add_children(self, new_children):
        self.children += new_children
        for child in new_children:
            child.parent = self


def grouper(n, iterable):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args)


def nodify(data):
    """ Return list of nodes """
    nodes = []
    for chunk in data:
        datum = hashlib.sha256(chunk.encode('utf-8')).hexdigest()
        nodes.append(Node(datum, data=chunk))
    return nodes


def create_parents(nodes):
    parents = []
    for a, b in grouper(2, nodes):
        try:
            import ipdb; ipdb.set_trace()
            parent_datum = hashlib.sha256("%s||%s" % (a.datum, b.datum))
            children = [a, b]
        except AttributeError:
            parent_datum = hashlib.sha256(str(a.datum).encode('utf-8')).hexdigest()
            children = [a]

        # create parent and link parent and children together
        parent = Node(parent_datum)
        parent.add_children(children)
        parents.append(parent)

    return parents


def condense_to_parent_layer(nodes):
    parents = create_parents(nodes)
    print(len(parents))
    if len(parents) == 1:
        return parents[0]
    else:
        condense_to_parent_layer(parents)


def merklize(data):
    # if len(data) > 1: we can continue, clean up later

    # take the data, hash it into a node per datum
    nodes = nodify(data)

    # if len(nodes) == 1
    condense_to_parent_layer(nodes)


def test_merkilize(data):
    root = merklize(data)
    assert root.data == '4a359c93d6b6c9beaa3fe8d8e68935aa5b5081bd2603549af88dee298fbfdd0a'


data = ["We", "hold", "these", "truths", "to", "be", "self-evident", "that"]

test_merkilize(data)
