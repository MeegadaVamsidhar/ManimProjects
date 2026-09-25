import unittest

from commonFun import HashRing, HashRingManager, KeyNode, ServerNode

class HashRingManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = HashRingManager(HashRing())
    def test_clockwise_lookup_and_wraparound(self):
        self.manager.add_server(ServerNode("A", 100))
        self.manager.add_server(ServerNode("B", 500))
        self.assertEqual(self.manager.find_owner(100).name, "A")
        self.assertEqual(self.manager.find_owner(101).name, "B")
        self.assertEqual(self.manager.find_owner(900).name, "A")
    def test_adding_server_only_moves_keys_in_its_interval(self):
        self.manager.add_server(ServerNode("A", 100))
        self.manager.add_server(ServerNode("C", 800))
        keys = [KeyNode("low", 50), KeyNode("middle", 500), KeyNode("high", 900)]
        for key in keys:
            self.manager.add_key(key)
        self.manager.assign_keys()
        before = self.manager.snapshot()
        self.manager.add_server(ServerNode("B", 600))
        self.manager.update()
        changes = self.manager.changed_keys(before)
        self.assertEqual([(key.name, old.name, new.name) for key, old, new in changes], [("middle", "C", "B")])
    def test_virtual_nodes_refer_to_physical_server(self):
        self.manager.add_server(ServerNode("A", 100))
        self.manager.add_server(ServerNode("B", 500))
        self.manager.add_virtual_nodes("A", [300, 700])
        owner = self.manager.find_owner(250)
        self.assertEqual(owner.name, "A1")
        self.assertEqual(owner.physical_name, "A")
        self.manager.remove_server("A")
        self.assertEqual(self.manager.server_names(), ["B"])
    def test_replication_uses_distinct_physical_servers(self):
        self.manager.add_server(ServerNode("A", 100))
        self.manager.add_server(ServerNode("B", 500))
        self.manager.add_server(ServerNode("C", 800))
        self.manager.add_virtual_nodes("A", [300, 700])
        targets = self.manager.replication_targets(self.manager.find_owner(50), replicas=5)
        self.assertEqual([target.physical_name for target in targets], ["B", "C"])

if __name__ == "__main__":
    unittest.main()
