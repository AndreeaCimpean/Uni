#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	//TODO - Implementation
	this->currentPosition = this->bag.head;
	this->currentFrequency = 1;
}

TComp SortedBagIterator::getCurrent() {
	//TODO - Implementation
	if (this->valid())
		return this->bag.elements[currentPosition];
	else
		throw exception();
}

bool SortedBagIterator::valid() {
	//TODO - Implementation
	if(this->currentPosition == -1)
		return false;
	return true;
}

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

void SortedBagIterator::first() {
	//TODO - Implementation
	this->currentPosition = this->bag.head;
	this->currentFrequency = 1;
}

