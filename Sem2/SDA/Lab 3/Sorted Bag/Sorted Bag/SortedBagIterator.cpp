#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

//Complexity: Theta(1)
SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	//TODO - Implementation
	this->currentPosition = this->bag.head;
	this->currentFrequency = 1;
}

//Complexity: Theta(1)
TComp SortedBagIterator::getCurrent() {
	//TODO - Implementation
	if (this->valid())
		return this->bag.elements[currentPosition];
	else
		throw exception();
}

//Complexity: Theta(1)
bool SortedBagIterator::valid() {
	//TODO - Implementation
	if(this->currentPosition == -1)
		return false;
	return true;
}

//Complexity: Theta(1)
void SortedBagIterator::next() {
	//TODO - Implementation
	if (this->valid())
		if (this->currentFrequency == this->bag.frequencies[currentPosition])
		{
			this->currentPosition = this->bag.next[currentPosition];
			this->currentFrequency = 1;
		}
		else
			this->currentFrequency += 1;
	else
		throw exception();
}

//Complexity: Theta(1)
void SortedBagIterator::first() {
	//TODO - Implementation
	this->currentPosition = this->bag.head;
	this->currentFrequency = 1;
}

