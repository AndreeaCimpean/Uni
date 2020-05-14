#include "SetIterator.h"
#include "Set.h"
#include <stdio.h>
#include <exception>

using namespace std;

SetIterator::SetIterator(const Set& m) : set(m)
{
	//TODO - Implementation
	this->currentPosition = 0;
	while (this->currentPosition < this->set.m && this->set.hashTable[this->currentPosition] == NULL)
		this->currentPosition++;
	if (currentPosition < this->set.m)
		this->currentNode = this->set.hashTable[this->currentPosition];
	else this->currentNode = NULL;
}


void SetIterator::first() {
	//TODO - Implementation
	this->currentPosition = 0;
	while (this->currentPosition < this->set.m && this->set.hashTable[this->currentPosition] == NULL)
		this->currentPosition++;
	if (currentPosition < this->set.m)
		this->currentNode = this->set.hashTable[this->currentPosition];
	else this->currentNode = NULL;
}


void SetIterator::next() {
	//TODO - Implementation
	if (this->valid())
	{
		if (this->currentNode->next != NULL)
			this->currentNode = this->currentNode->next;
		else
		{
			this->currentPosition++;
			while (this->currentPosition < this->set.m && this->set.hashTable[this->currentPosition] == NULL)
				this->currentPosition++;
			if (currentPosition < this->set.m)
				this->currentNode = this->set.hashTable[this->currentPosition];
			else this->currentNode = NULL;
		}
	}
	else
		throw exception();
}


TElem SetIterator::getCurrent()
{
	//TODO - Implementation
	if (this->valid())
		return this->currentNode->key;
	else
		throw exception();
}

bool SetIterator::valid() const {
	//TODO - Implementation
	return (this->currentNode != NULL);
}



