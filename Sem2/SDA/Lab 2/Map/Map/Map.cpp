#include "Map.h"
#include "MapIterator.h"
#include <stdio.h>

//Complexity: Theta(1)
Map::Map() {
	//TODO - Implementation
	this->head = NULL;
	this->tail = NULL;
}

Map::~Map() {
	//TODO - Implementation
	Node* currentNode = this->head;
	while (currentNode != NULL)
	{
		Node* nextNode = currentNode->next;
		delete currentNode;
		currentNode = nextNode;
	}
}

/*
Complexity:
BC - Theta(1) - element is in the map and is the first(the head)
WC - Theta(n) - element is not in the map
Overall complexity: O(n)
*/
TValue Map::add(TKey c, TValue v){
	//TODO - Implementation
	Node* currentNode = this->head;
	while (currentNode != NULL)
	{
		if (currentNode->data.first == c)
		{
			TValue oldValue = currentNode->data.second;
			currentNode->data.second = v;
			return oldValue;
		}
		currentNode = currentNode->next;
	}

	TElem element = TElem(c, v);
	Node* new_node = new Node;
	new_node->data = element;
	new_node->next = NULL;
	new_node->previous = this->tail;

	if (this->head == NULL)
	{
		this->head = new_node;
		this->tail = new_node;
	}
	else
	{
		this->tail->next = new_node;
		this->tail = new_node;
	}

	return NULL_TVALUE;
}

/*
Complexity:
BC - Theta(1) - element is the first in the map (the head)
WC - Theta(n) - element is not in the map
Overall complexity: O(n)
*/
TValue Map::search(TKey c) const{
	//TODO - Implementation
	Node* currentNode = this->head;
	while (currentNode != NULL)
	{
		if (currentNode->data.first == c)
			return currentNode->data.second;
		currentNode = currentNode->next;
	}
	return NULL_TVALUE;
}

/*
Complexity:
BC - Theta(1) element is the first in the map(the head)
WC - Theta(n) elemnt not found in the map
Overall complexity: O(n)
*/
TValue Map::remove(TKey c){
	//TODO - Implementation
	Node* currentNode = this->head;
	while (currentNode!= NULL && currentNode->data.first != c)
		currentNode = currentNode->next;
	if (currentNode != NULL)
	{
		TValue oldValue = currentNode->data.second;
		if (currentNode == this->head)
		{
			if (currentNode == this->tail)
			{
				this->head = NULL;
				this->tail = NULL;
			}
			else
			{
				this->head = this->head->next;
				this->head->previous = NULL;
			}
		}
		else if (currentNode == this->tail)
		{
			this->tail = this->tail->previous;
			this->tail->next = NULL;
		}
		else
		{
			currentNode->next->previous = currentNode->previous;
			currentNode->previous->next = currentNode->next;
			currentNode->previous = NULL;
			currentNode->next = NULL;
		}
		delete currentNode;
		return oldValue;
	}
	return NULL_TVALUE;
}

//Complexity: Theta(n)
int Map::size() const {
	//TODO - Implementation
	Node* current_node = this->head;
	int count = 0;
	while (current_node != NULL)
	{
		count++;
		current_node = current_node->next;
	}
	return count;
}
 
//Complexity - Theta(1)
bool Map::isEmpty() const{
	//TODO - Implementation
	if (this->head == NULL)
		return true;
	return false;
}

MapIterator Map::iterator() {
	return MapIterator(*this);
}



