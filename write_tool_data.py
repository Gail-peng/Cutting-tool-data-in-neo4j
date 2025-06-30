import json
from py2neo import Graph, Node, Relationship, NodeMatcher
import tqdm

graph = Graph("bolt://localhost:7687", user="neo4j", password="password")
matcher = NodeMatcher(graph)

node_id_list = []

# create node in neo4j
# with open('./data.json','r') as f:
#     nodes = json.loads(f.read())['nodes']
#     for data in nodes:
#         label = data['labels'][0]
#         del data['labels']
#         # print(label,data)
#         if data['id'] not in node_id_list:
#             node_id_list.append(data['id'])
#             node = Node(label,**data)
#             graph.create(node)


# create relation in neo4j
with open('./data.json','r') as f:
    rels = json.loads(f.read())['relationships']
    for rel in rels:
        # node_head = Node(id=rel['start'])
        # node_tail = Node(id=rel['end'])
        type = rel['type']
        node_head = matcher.match(id=rel['start']).first()
        node_tail = matcher.match(id=rel['end']).first()
        relation = Relationship(node_head, type, node_tail)
        graph.create(relation)
        print(node_head,node_tail)
        # print(rel)
