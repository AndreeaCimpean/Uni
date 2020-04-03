#pragma once

typedef int TElem;

typedef struct
{
	TElem* elems;
	int capacity;
	int size;
} DynamicArray;

DynamicArray* create(int capacity);
void destory(DynamicArray* array);
void add(DynamicArray* array, TElem elem);