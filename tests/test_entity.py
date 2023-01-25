from pywikidata import Entity


class TestEntity:
    def test_entity_init(self):
        entity = Entity("Q90")
        assert entity.label == "Paris"

        assert hasattr(entity, "label")
        assert hasattr(entity, "instance_of")

    def test_entity_init_from_label(self):
        assert len(Entity.from_label("Paris")) > 0

    def test_entity_type(self):
        assert Entity("Q90").is_property is False
        assert Entity("P81").is_property is True

    def test_neighbours(self):
        entity = Entity("Q107291621")
        assert len(entity.forward_one_hop_neighbours) > 0
        assert len(entity.backward_one_hop_neighbours) > 0
        assert len(entity.one_hop_neighbours) > 0