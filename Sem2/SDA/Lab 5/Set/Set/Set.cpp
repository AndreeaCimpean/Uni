#include "Set.h"
#include "SetITerator.h"
#include <cstdlib>
#include <stdio.h>

using namespace std;

int Set::hashFunction(TElem key) const
{
	return abs(key) % this->m;
}

Set::Set() {
	//TODO - Implementation
	this->m = 6;
	this->hashTable = new Node*[this->m];
	for (int i = 0; i < m; ++i)
		this->hashTable[i] = NULL;
	this->maximumLoadFactor = 0.7;
	this->length = 0;
}


bool Set::add(TElem elem) {
	//TODO - Implementation
	if (this->search(elem))
		return false;
	int position = this->hashFunction(elem);
	Node* newNode = new Node;
	newNode->key = elem;
	newNode->next = this->hashTable[position];
	this->hashTable[position] = newNode;
	this->length++;
	if ((double)(this->length) / (double)(this->m) > this->maximumLoadFactor)
	{
		int previous_m = this->m;

		this->length = 0;
		this->m *= 2;

		Node** temporaryTable = new Node* [this->m];
		for (int i = 0; i < previous_m; ++i)
			temporaryTable[i] = this->hashTable[i];

		Node** newTable = new Node * [this->m];
		for (int i = 0; i < this->m; ++i)
			newTable[i] = NULL;

		delete[] this->hashTable;
		this->hashTable = newTable;

		for (int i = 0; i < previous_m; ++i)
		{
			Node* node = temporaryTable[i];
			while (node != NULL)
			{
				this->add(node->key);
				node = node->next;
			}
		}
		delete[] temporaryTable;
	}
	return true;
}


bool Set::remove(TElem elem) {
	//TODO - Implementation
	int position = this->hashFunction(elem);
	Node* currentNode = this->hashTable[position];
	Node* previousNode = NULL;
	while (currentNode != NULL && currentNode->key != elem)
	{
		previousNode = currentNode;
		currentNode = currentNode->next;
	}
	if (currentNode == NULL)
		return false;
	this->length--;
	if (previousNode == NULL)
		this->hashTable[position] = currentNode->next;
	else
		previousNode->next = currentNode->next;
	delete currentNode;
	return true;
}

bool Set::search(TElem elem) const {
	//TODO - Implementation
	int position = this->hashFunction(elem);
	Node* currentNode = this->hashTable[position];
	while (currentNode != NULL && currentNode->key != elem)
		currentNode = currentNode->next;
	if (currentNode != NULL)
		return true;
	return false;
}


int Set::size() const {
	//TODO - Implementation
	return this->length;
}


bool Set::isEmpty() const {
	//TODO - Implementation
	return (this->length == 0);
}


Set::~Set() {
	//TODO - Implementation
	delete[]this->hashTable;
}


SetIterator Set::iterator() const {
	return SetIterator(*this);
}


