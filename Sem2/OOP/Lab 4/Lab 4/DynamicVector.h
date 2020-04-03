#pragma once
#include "Evidence.h"

typedef Evidence Element;

class DynamicVector
{
private:
	Element* elements;
	int size;
	int capacity;
public:
	DynamicVector(int capacity = 10);
	DynamicVector(const DynamicVector& dynamicVector);
	~DynamicVector();
	DynamicVector& operator=(const DynamicVector& dynamicVector);
	void add_element(const Element& element);
	void delete_element(const int position);
	Element get_element(int position) const;
	Element* get_elements() const;
	int get_size() const;
	int get_capacity() const;
	void update_element(const int position, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph);
	void resize(double factor = 2);
};

