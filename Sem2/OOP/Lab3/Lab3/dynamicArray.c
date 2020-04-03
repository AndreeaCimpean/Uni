#include "dynamicArray.h"
#include <stdlib.h>

DynamicArray* create_dynamic_array(int capacity)
{
	/*
	Create a new variable of type DynamicArray by dynamically allocating memory for it
	Parameters: capacity->the capcity of the array
	Return: a pointer to the dynamic array
			 NULL if could not allocate memory
	*/
	DynamicArray* newDynamicArray = (DynamicArray*)malloc(sizeof(DynamicArray));
	if (newDynamicArray == NULL)
		return NULL;
	newDynamicArray->capacity = capacity;
	newDynamicArray->length = 0;
	newDynamicArray->elements = (Element*)malloc(capacity * sizeof(Element));
	if (newDynamicArray->elements == NULL)
		return NULL;
	return newDynamicArray;
}

void destroy_dynamic_array(DynamicArray* dynamicArray)
{
	/*
	Free the memory allocated for a dynamic array and its elemnts
	Parameters: dynamicArray->pointer to the dynamic array

	*/
	if (dynamicArray == NULL)
		return;
	for (int i = 0; i < dynamicArray->length; ++i)
		destroy_profile(dynamicArray->elements[i]);
	free(dynamicArray->elements);
	free(dynamicArray);
}

void resize_dynamic_array(DynamicArray* dynamicArray)
{
	/*
	Resize a dynamic array(increase cpacity)
	Parameters: dynamicArray->pointer to the dynamic array
	*/
	dynamicArray->capacity *= 2;
	Element* resized_list_of_elements = (Element*)realloc(dynamicArray->elements, dynamicArray->capacity * sizeof(Element));
	dynamicArray->elements = resized_list_of_elements;
}

void add_element_dynamic_array(DynamicArray* dynamicArray, Element element)
{
	/*
	Add an element to the dynamic array
	Parameters: dynamicArray-> pointer to the dynamic array
				element-> the element to be added
	*/
	if (dynamicArray->length == dynamicArray->capacity)
		resize_dynamic_array(dynamicArray);
	dynamicArray->elements[dynamicArray->length++] = element;
}

void delete_element_from_dynamic_array(DynamicArray* dynamicArray, int position)
{
	/*
	Delete an element from a dynamic array from a given position
	Parameters: dynamicArray->pointer to the dynamic array
				position->the given position, integer
	*/
	Element element = get_element_from_dynamic_array(dynamicArray, position);
	destroy_profile(element);
	for (int i = position; i < dynamicArray->length - 1; ++i)
		dynamicArray->elements[i] = dynamicArray->elements[i + 1];
	dynamicArray->length--;
}

int get_length_dynamic_array(DynamicArray* dynamicArray)
{
	/*
	Get the length of a dynamic array
	Parameters: dynamicArray->pointer to the dynamic array
	Return: the length of the dynamic array
	*/
	return dynamicArray->length;
}

Element get_element_from_dynamic_array(DynamicArray* dynamicArray, int position)
{
	/*
	Get element from a given position in a dynamic array
	Parameters: dynamicArray->pointer to the dynamic array
				poisiton->the given position, integer
	Return: the element at given position if valid position
			 NULL if invalid position
	*/
	if (position < 0 || position >= dynamicArray->length)
		return NULL;
	return dynamicArray->elements[position];
}
