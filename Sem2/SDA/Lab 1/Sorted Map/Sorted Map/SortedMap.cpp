#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
using namespace std;

SortedMap::SortedMap(Relation r) {
	//TODO - Implementation
	this->capacity = 5;
	this->length = 0;
	this->array = new TElem[this->capacity];
	this->relation = r;
}


//Complexity: theta(n); no BC, WC
TValue SortedMap::add(TKey k, TValue v) {
	//TODO - Implementation
	int index = 0;
	while (index < this->length && this->relation(this->array[index].first, k))
	{
		if (this->array[index].first == k)
		{
			TValue oldValue = this->array[index].second;
			this->array[index].second = v;
			return oldValue;
		}
		index += 1;
	}
	if (this->length == this->capacity)
	{
		this->capacity *= 2;
		TElem* newArray = new TElem[this->capacity];
		for (int i = 0; i < this->length; ++i)
			newArray[i] = this->array[i];
		delete[] this->array;
		this->array = newArray;
	}
	for (int i = length - 1; i >= index; --i)
		this->array[i + 1] = this->array[i];
	TElem element = TElem(k, v);
	this->array[index] = element;
	this->length += 1;
	return NULL_TVALUE;
}

/*
Complexity:
BC - theta(1) - element found in the middle
AC - theta(log2n)
WC - theta(log2n) - element not in the list
Overall complexity - O(log2n)
*/
TValue SortedMap::search(TKey k) const {
	//TODO - Implementation
	int left = 0, right = this->length - 1;
	int middle;
	while (left <= right)
	{
		middle = (left + right) / 2;
		if (this->array[middle].first == k)
			return this->array[middle].second;
		else if (this->relation(this->array[middle].first, k))
			left = middle + 1;
		else
			right = middle - 1;	
	}
	return NULL_TVALUE;
}

//Complexity: theta(n)
TValue SortedMap::remove(TKey k) {
	//TODO - Implementation
	int index = 0;
	while (index < this->length)
	{
		if (this->array[index].first == k)
			break;
		index += 1;
	}
	if (index == this->length)
		return NULL_TVALUE;
	TValue oldValue = this->array[index].second;
	for (int i = index; i < length - 1; ++i)
		this->array[i] = this->array[i + 1];
	this->length--;
	return oldValue;
}

//Complexity: theta(1)
int SortedMap::size() const {
	//TODO - Implementation
	return this->length;
}

//Complexity: theta(1)
bool SortedMap::isEmpty() const {
	//TODO - Implementation
	if (this->length == 0)
		return true;
	return false;
}

SMIterator SortedMap::iterator() const {
	return SMIterator(*this);
}

SortedMap::~SortedMap() {
	//TODO - Implementation
	delete[] this->array;
}
