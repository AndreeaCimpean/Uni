#include "Map.h"
#include "MapIterator.h"
#include <exception>
using namespace std;


MapIterator::MapIterator(const Map& d) : map(d)
{
	//TODO - Implementation
	current_node = map.head;
}


void MapIterator::first() {
	//TODO - Implementation
	current_node = map.head;
}


void MapIterator::next() {
	//TODO - Implementation
	if (valid())
		current_node = current_node->next;
	else
		throw exception();
}


TElem MapIterator::getCurrent(){
	//TODO - Implementation
	if (valid())
		return current_node->data;
	else
		throw exception();
}


bool MapIterator::valid() const {
	//TODO - Implementation
	return(current_node != NULL);
}



