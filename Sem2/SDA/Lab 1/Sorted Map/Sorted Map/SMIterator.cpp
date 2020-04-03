#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator(const SortedMap& m) : map(m){
	//TODO - Implementation
	this->current_position = 0;
}

//Complexity: theta(1)
void SMIterator::first(){
	//TODO - Implementation
	this->current_position = 0;
}

//Complexity: theta(1)
void SMIterator::next(){
	//TODO - Implementation
	if (this->valid())
		this->current_position++;
	else
		throw exception();
}

//Complexity: theta(1)
bool SMIterator::valid() const{
	//TODO - Implementation
	return 0 <= this->current_position && this->current_position < this->map.length;
}

//Complexity: theta(1)
TElem SMIterator::getCurrent() const{
	//TODO - Implementation
	if (this->valid())
		return this->map.array[this->current_position];
	throw exception();
}


