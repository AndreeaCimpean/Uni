#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
	//TODO - Implementation
	this->currentPosition = 0;
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
		return true;
	return false;
}

void SortedBagIterator::next() {
	//TODO - Implementation
	if (this->valid())
		if (this->currentFrequency == this->bag.frequencies[currentPosition])
			this->currentPosition = this->bag.next[currentPosition];
		else
			this->currentFrequency += 1;
}

void SortedBagIterator::first() {
	//TODO - Implementation
	this->currentPosition = 0;
	this->currentFrequency = 1;
}

