#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>

using namespace std;

SortedBag::SortedBag(Relation r) {
	//TODO - Implementation
	this->capacity = 5;
	this->elements = new TComp[capacity];
	this->frequencies = new int[this->capacity];
	this->next = new int[this->capacity];
	this->head = -1;
	for (int i = 0; i < this->capacity - 1; ++i)
		this->next[i] = i + 1;
	this->next[this->capacity-1] = -1;
	this->firstEmpty = 0;
	this->relation = r;
	this->length = 0;
}

/*
Complexity:
BC - Theta(1) - element found on the first position
WC - Theta(n) - element not in the bag, "grater" than all elements
Overall complexity: O(n)
*/
void SortedBag::add(TComp e) {
	//TODO - Implementation
	this->length++;
	int current = head;
	int position = 0;
	while (current != -1 && this->relation(this->elements[current], e) && this->elements[current] != e)
	{
		position++;
		current = this->next[current];
	}
	if (current != -1 && this->elements[current] == e)
			this->frequencies[current]++;
	else
	{
		if (this->firstEmpty == -1)
		{
			TComp* newElements = new TComp[capacity*2];
			int* newFrequencies = new int[capacity*2];
			int* newNext = new int[capacity*2];
			for (int i = 0; i < this->capacity; ++i)
			{
				newElements[i] = this->elements[i];
				newFrequencies[i] = this->frequencies[i];
				newNext[i] = this->next[i];
			}
			for (int i = this->capacity; i < this->capacity * 2 - 1; ++i)
				newNext[i] = i + 1;
			newNext[this->capacity * 2 - 1] = -1;
			delete[] this->elements;
			delete[] this->frequencies;
			delete[] this->next;
			this->elements = newElements;
			this->frequencies = newFrequencies;
			this->next = newNext;
			this->firstEmpty = this->capacity;
			this->capacity *= 2;
		}
		if (position == 0)
		{
			int newPosition = this->firstEmpty;
			this->elements[newPosition] = e;
			this->frequencies[newPosition] = 1;
			this->firstEmpty = this->next[this->firstEmpty];
			this->next[newPosition] = this->head;
			this->head = newPosition;
		}
		else
		{
			int current_position = 0;
			int current_node = this->head;
			while (current_position < position - 1)
			{
				current_position++;
				current_node = this->next[current_node];
			}
			int newElement = this->firstEmpty;
			this->firstEmpty = this->next[this->firstEmpty];
			this->elements[newElement] = e;
			this->frequencies[newElement] = 1;
			this->next[newElement] = this->next[current_node];
			this->next[current_node] = newElement;
		}
	}
}

/*
Complexity:
BC - Theta(1) - element found on the first position
WC - Theta(n) - element not in the bag, "grater" than all elements
Overall complexity: O(n)
*/
bool SortedBag::remove(TComp e) {
	//TODO - Implementation
	int current = head;
	int previous = -1;
	while (current != -1 && this->relation(this->elements[current], e) && this->elements[current] != e)
	{
		previous = current;
		current = this->next[current];
	}
	if (this->elements[current] == e)
	{
		this->length--;
		if (frequencies[current] > 1)
			frequencies[current]--;
		else
		{
			if (current == this->head)
				this->head = this->next[this->head];
			else
				this->next[previous] = this->next[current];
			this->next[current] = this->firstEmpty;
			this->firstEmpty = current;
		}
		return true;
	}
	return false;
}

/*
Complexity:
BC - Theta(1) - element found on the first position/element "smaller" than all elements
WC - Theta(n) - element not in the bag and "greater"than all elemnts 
Overall complexity: O(n)
*/
bool SortedBag::search(TComp elem) const {
	//TODO - Implementation
	int current = this->head;
	while (current != -1 && this->relation(this->elements[current], elem) && this->elements[current] != elem)
		current = this->next[current];
	if (this->elements[current] == elem)
		return true;
	return false;
}

/*
Complexity:
BC - Theta(1) - element found on the first position/element "smaller" than all elements
WC - Theta(n) - element not in the bag and "greater"than all elemnts
Overall complexity: O(n)
*/
int SortedBag::nrOccurrences(TComp elem) const {
	//TODO - Implementation
	int current = this->head;
	while (current != -1 && this->relation(this->elements[current], elem) && this->elements[current] != elem)
		current = this->next[current];
	if (this->elements[current] == elem)
		return this->frequencies[current];
	return 0;
}


//Complexity: Theta(1)
int SortedBag::size() const {
	//TODO - Implementation
	return this->length;
}

//Complexity: Theta(1)
bool SortedBag::isEmpty() const {
	//TODO - Implementation
	if (this->head == -1)
		return true;
	return false;
}

//Complexity: Theta(1)
SortedBagIterator SortedBag::iterator() const {
	return SortedBagIterator(*this);
}


SortedBag::~SortedBag() {
	//TODO - Implementation
	delete[] this->elements;
	delete[] this->frequencies;
	delete[] this->next;
}
