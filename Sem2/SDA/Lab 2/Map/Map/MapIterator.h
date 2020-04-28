#pragma once
#include "Map.h"
class MapIterator
{
	//DO NOT CHANGE THIS PART
	friend class Map;
private:
	Map& map;
	//TODO - Representation
	Node* current_node;

	MapIterator(Map& m);
public:
	void first();
	void next();
	TElem getCurrent();
	bool valid() const;
	TElem remove();
};



