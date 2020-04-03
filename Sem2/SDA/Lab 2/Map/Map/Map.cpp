#include "Map.h"
#include "MapIterator.h"
#include <stdio.h>

Map::Map() {
	//TODO - Implementation
	this->head = NULL;
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
BC - Theta(1) key found at the beginning
AC - Theta(n)
WC - Theta(n) key not found in map
Overall complexity - O(n)
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
	new_node->previous = NULL;
	if (this->head == NULL)
	{
		new_node->next = NULL;
		this->head = new_node;
	}
	else 
	{
		new_node->next = this->head;
		this->head->previous = new_node;
		this->head = new_node;
	}
	return NULL_TVALUE;
}

/*
Complexity:
BC - Theta(1) key found at the beginning
AC - Theta(n)
WC - Theta(n) key not found in map
Overall complexity - O(n)
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
BC - Theta(1) key found at the beginning
AC - Theta(n)
WC - Theta(n) key not found in map
Overall complexity - O(n)
*/
TValue Map::remove(TKey c){
	//TODO - Implementation
	Node* currentNode = this->head;
	while (currentNode!= NULL && currentNode->data.first != c)
		currentNode = currentNode->next;
	if (currentNode != NULL)
	{
		TValue oldValue = currentNode->data.second;
		if (currentNode->next == NULL && currentNode->previous == NULL)
		{
			this->head = NULL;
		}
		else if (currentNode->previous == NULL)
		{
			this->head->next->previous = NULL;
			this->head = this->head->next;
			delete currentNode;
		}
		else if (currentNode->next == NULL)
		{
			currentNode->previous->next = NULL;
			delete currentNode;
		}
		else
		{
			Node* previousNode = currentNode->previous;
			Node* nextNode = currentNode->next;
			if (previousNode)
				previousNode->next = nextNode;
			nextNode->previous = previousNode;
			delete currentNode;
		}
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

MapIterator Map::iterator() const {
	return MapIterator(*this);
}



