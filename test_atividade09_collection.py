import pytest
from atividades.src.atividade09_collection import Item, ItemCollection

def test_create_Item():
    item = Item("item")
    assert item.name == "item"

def test_create_ItemCollection():
    item_collection = ItemCollection()
    assert item_collection.items == []

def test_add_Item_to_ItemCollection():
    item = Item("item")
    item_collection = ItemCollection()

    item_collection.add_item(item)

    assert item_collection.get_items() == [item]

def test_remove_Item_of_ItemCollection():
    item1 = Item("item1")
    item2 = Item("item2")
    item_collection = ItemCollection()
    item_collection.add_item(item1)
    item_collection.add_item(item2)

    item_collection.remove_item(item1)

    assert item_collection.get_items() == [item2]

def test_getItems_of_ItemCollection():
    item1 = Item("item1")
    item2 = Item("item2")
    item_collection = ItemCollection()
    item_collection.add_item(item1)
    item_collection.add_item(item2)

    assert item_collection.get_items() == [item1, item2]