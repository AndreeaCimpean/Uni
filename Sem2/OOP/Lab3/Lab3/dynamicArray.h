#pragma once
#include "domain.h"

#define INITIAL_CAPACITY 10

typedef Profile* Element;

typedef struct
{
	Element* elements;
	int length;
	int capacity;
} DynamicArray;

DynamicArray* create_dynamic_array(int capacity);
void destroy_dynamic_array(DynamicArray* dynamicArray);
void resize_dynamic_array(DynamicArray* dynamicArray);
void add_element_dynamic_array(DynamicArray* dynamicArray, Element element);
void delete_element_from_dynamic_array(DynamicArray* dynamicArray, int position);
int get_length_dynamic_array(DynamicArray* dynamicArray);
Element get_element_from_dynamic_array(DynamicArray* dynamicArray, int position);
