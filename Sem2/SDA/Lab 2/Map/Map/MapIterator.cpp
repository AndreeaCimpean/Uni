#include "Map.h"
#include "MapIterator.h"
#include <exception>
#include <stdio.h>
using namespace std;

//Complexity: Theta(1)
MapIterator::MapIterator(Map& d) : map(d)
{
	//TODO - Implementation
	current_node = map.head;
}

//Complexity: Theta(1)
void MapIterator::first() {
	//TODO - Implementation
	current_node = map.head;
}

//Complexity: Theta(1)
void MapIterator::next() {
	//TODO - Implementation
	if (valid())
		current_node = current_node->next;
	else
		throw exception();
}

//Complexity: Theta(1)
TElem MapIterator::getCurrent(){
	//TODO - Implementation
	if (valid())
		return current_node->data;
	else
		throw exception();
}

//Complexity: Theta(1)
bool MapIterator::valid() const {
	//TODO - Implementation
	return(current_node != NULL);
}



/*
Change the iterator to be able to remove the current element. Add the following operation in the MapIterator class:

//removes and returns the current pair from the iterator
//after the operation the current pair from the Iterator is the next element from the Map, or, if the removed element was the last one, the iterator is invalid
//throws exception if the iterator is invalid
TElem remove();

Obs: In order for this operation to work, you need to perform some other changes in code:
Iterator operation from the Map no longer is const
The reference to the  Map in the iterator is no longer const (but it is still a reference!)
The parameter passed to the constructor of the iterator class is no longer const
*/

//Complexity: Theta(1)
TElem MapIterator::remove()
{
	if (!valid())
		throw exception();
	else
	{
		TElem current_element = current_node->data;
		Node* next_node = this->current_node->next;
		if (this->current_node == this->map.head)
		{
			if (this->current_node == this->map.tail)
			{
				this->map.head = NULL;
				this->map.tail = NULL;
			}
			else
			{
				this->map.head = this->map.head->next;
				this->map.head->previous = NULL;
			}
		}
		else if (this->current_node == this->map.tail)
		{
			this->map.tail = this->map.tail->previous;
			this->map.tail->next = NULL;
		}
		else
		{
			this->current_node->next->previous = this->current_node->previous;
			this->current_node->previous->next = this->current_node->next;
		}
		delete this->current_node;
		this->current_node = next_node;
		return current_element;
	}
}



