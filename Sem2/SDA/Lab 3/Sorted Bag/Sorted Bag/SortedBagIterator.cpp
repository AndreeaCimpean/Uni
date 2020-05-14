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


//Make the iterator bidirectional.Add the following operation in the SortedBagIterator class.

//changes the current element from the iterator to the previous element, or, 
//if the current element was the first, makes the iterator invalid
//throws an exception if the iterator is not valid
/*

BC: Theta(1) - current element is the head/appears several times in the bag before
WC: Theta(n) - current is the first appearance of the last element
Overall complexity: O(n)
*/
void SortedBagIterator::previous()
{
	if (!this->valid())
		throw exception();
	else
	{
		if (this->currentFrequency > 1)
			this->currentFrequency--;
		else
		{
			if (this->currentPosition == this->bag.head)
				this->currentPosition = -1;
			else
			{
				int current = this->bag.head;
				int previous;
				while (current != this->currentPosition)
				{
					previous = current;
					current = this->bag.next[previous];
				}
				this->currentPosition = previous;
				this->currentFrequency = this->bag.frequencies[previous];
			}
		}
	}
}




