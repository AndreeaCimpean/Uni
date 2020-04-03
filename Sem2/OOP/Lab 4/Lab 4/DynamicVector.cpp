#include "DynamicVector.h"

DynamicVector::DynamicVector(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elements = new Element[capacity];
}

DynamicVector::DynamicVector(const DynamicVector& dynamicVector)
{
	this->size = dynamicVector.size;
	this->capacity = dynamicVector.capacity;
	this->elements = new Element[this->capacity];
	for (int i = 0; i < this->size; ++i)
		this->elements[i] = dynamicVector.elements[i];
}

DynamicVector::~DynamicVector()
{
	delete[] this->elements;
}

DynamicVector& DynamicVector::operator=(const DynamicVector& dynamicVector)
{
	if (this == &dynamicVector)
		return *this;
	this->size = dynamicVector.size;
	this->capacity = dynamicVector.capacity;
	delete[] this->elements;
	this->elements = new Element[this->capacity];
	for (int i = 0; i < this->size; ++i)
		this->elements[i] = dynamicVector.elements[i];
	return *this;
}

void DynamicVector::add_element(const Element& element)
{
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size] = element;
	this->size++;
}


void DynamicVector::delete_element(const int position)
{
	for (int i = position; i < this->size - 1; ++i)
		this->elements[i] = this->elements[i + 1];
	this->size--;
}

Element DynamicVector::get_element(int position) const
{
	return this->elements[position];
}

Element* DynamicVector::get_elements() const
{
	return this->elements;
}

int DynamicVector::get_size() const
{
	return this->size;
}

int DynamicVector::get_capacity() const
{
	return this->capacity;
}

void DynamicVector::update_element(const int position, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph)
{
	this->elements[position].set_measurement(measurement);
	this->elements[position].set_image_clarity_level(imageClarityLevel);
	this->elements[position].set_quantity(quantity);
	this->elements[position].set_photograph(photograph);
}

void DynamicVector::resize(double factor)
{
	this->capacity *= factor;
	Element* new_list_elements = new Element[this->capacity];
	for (int i = 0; i < this->size; ++i)
		new_list_elements[i] = this->elements[i];
	delete[] this->elements;
	this->elements = new_list_elements;
}


