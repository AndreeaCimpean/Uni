#include "dynarray.h"
#include <stdlib.h>
DynamicArray* create(int capacity)
{
	DynamicArray* arr = (DynamicArray*)malloc(sizeof(DynamicArray));
	if (arr == NULL)
		return NULL;
	arr->capacity = capacity;
	arr->size = 0;

	arr->elems = (TElem*)malloc(capacity * sizeof(TElem));

	return arr;
}

void destory(DynamicArray* array)
{
	if (array == NULL)
		return;
	free(array->elems);
	free(array);
}

void add(DynamicArray* array, TElem elem)
{
	if (array == NULL)
		return;
	if (array->size == array->capacity)
		resize(array);
	array->elems[array->size++] = elem;
}
