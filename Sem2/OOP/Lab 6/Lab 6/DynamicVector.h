#pragma once
#include "Evidence.h"


template <typename T>
class DynamicVector
{
private:
	T* elements;
	int size;
	int capacity;
public:
	DynamicVector(int capacity = 10);
	DynamicVector(const DynamicVector& dynamicVector);
	~DynamicVector();
	DynamicVector& operator=(const DynamicVector& dynamicVector);
	T& operator[](int position);
	void add_element(const T& element);
	void delete_element(const int position);
	T& get_element(int position) const;
	T* get_elements() const;
	int get_size() const;
	int get_capacity() const;
	void update_element(const int position, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph);
	void resize(double factor = 2);
public:
	class iterator
	{
	private:
		T* currentElement;
	public:
		iterator(T* currentElement): currentElement{currentElement}{}
		T& operator*();
		bool operator!=(const iterator& it);
		bool operator==(const iterator& it);
		iterator operator++();
		iterator operator++(int);
	};
	typename iterator begin();
	typename iterator end();
};

template <typename T>
DynamicVector<T>::DynamicVector(int capacity)
{
	this->size = 0;
	this->capacity = capacity;
	this->elements = new T[capacity];
}

template <typename T>
DynamicVector<T>::DynamicVector(const DynamicVector<T>& dynamicVector)
{
	this->size = dynamicVector.size;
	this->capacity = dynamicVector.capacity;
	this->elements = new T[this->capacity];
	for (int i = 0; i < this->size; ++i)
		this->elements[i] = dynamicVector.elements[i];
}

template <typename T>
DynamicVector<T>::~DynamicVector()
{
	delete[] this->elements;
}

template <typename T>
DynamicVector<T>& DynamicVector<T>::operator=(const DynamicVector<T>& dynamicVector)
{
	if (this == &dynamicVector)
		return *this;
	this->size = dynamicVector.size;
	this->capacity = dynamicVector.capacity;
	delete[] this->elements;
	this->elements = new T[this->capacity];
	for (int i = 0; i < this->size; ++i)
		this->elements[i] = dynamicVector.elements[i];
	return *this;
}

template <typename T>
T& DynamicVector<T>::operator[](int position)
{
	return this->elements[position];
}

template <typename T>
void DynamicVector<T>::add_element(const T& element)
{
	if (this->size == this->capacity)
		this->resize();
	this->elements[this->size] = element;
	this->size++;
}

template <typename T>
void DynamicVector<T>::delete_element(const int position)
{
	for (int i = position; i < this->size - 1; ++i)
		this->elements[i] = this->elements[i + 1];
	this->size--;
}

template <typename T>
T& DynamicVector<T>::get_element(int position) const
{
	return this->elements[position];
}

template <typename T>
T* DynamicVector<T>::get_elements() const
{
	return this->elements;
}

template <typename T>
int DynamicVector<T>::get_size() const
{
	return this->size;
}

template <typename T>
int DynamicVector<T>::get_capacity() const
{
	return this->capacity;
}

template <typename T>
void DynamicVector<T>::update_element(const int position, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph)
{
	this->elements[position].set_measurement(measurement);
	this->elements[position].set_image_clarity_level(imageClarityLevel);
	this->elements[position].set_quantity(quantity);
	this->elements[position].set_photograph(photograph);
}

template <typename T>
void DynamicVector<T>::resize(double factor)
{
	this->capacity *= factor;
	T* new_list_elements = new T[this->capacity];
	for (int i = 0; i < this->size; ++i)
		new_list_elements[i] = this->elements[i];
	delete[] this->elements;
	this->elements = new_list_elements;
}

template<typename T>
typename DynamicVector<T>::iterator DynamicVector<T>::begin()
{
	return iterator{ this->elements };
}

template <typename T>
typename DynamicVector<T>::iterator DynamicVector<T>::end()
{
	return iterator{ this->elements + this->size };
}

template<typename T>
T& DynamicVector<T>::iterator::operator*()
{
	return *this->currentElement;
}

template <typename T>
bool DynamicVector<T>::iterator::operator!=(const iterator& iterator)
{
	return this->currentElement != iterator.currentElement;
}


template <typename T>
bool DynamicVector<T>::iterator::operator==(const iterator& iterator)
{
	return this->currentElement == iterator.currentElement;
}

template <typename T>
typename DynamicVector<T>::iterator DynamicVector<T>::iterator::operator++()
{
	this->currentElement++;
	return *this;
}

template <typename T>
typename DynamicVector<T>::iterator DynamicVector<T>::iterator::operator++(int)
{
	iterator iterator_before = *this;
	this->currentElement++;
	return iterator_before;
}
