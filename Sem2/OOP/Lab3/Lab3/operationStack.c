#include "operationStack.h"
#include <string.h>
#include <stdlib.h>

Operation* create_operation(Profile* profile, char* type)
{
	/*
	Create a new variable of type Operation by dynamically allocating memory for it
	Parameters: profile->pointer to the profile of the new operation
				type->the type of the new operation, pointer to string
	Return: a pointer to the created operation
			 NULL if could not allocate memory
	*/
	Operation* newOperation = (Operation*)malloc(sizeof(Operation));
	if (newOperation == NULL)
		return NULL;
	newOperation->profile = copy_profile(profile);
	newOperation->type = (char*)malloc(sizeof(char) * (strlen(type) + 1));
	if (newOperation->type == NULL)
		return NULL;
	strcpy(newOperation->type, type);
	return newOperation;
}

void destroy_operation(Operation* operation)
{
	/*
	Free memory allocated for an operation and its profile
	Parameters: operation->pointer to the operation
	*/
	if (operation == NULL)
		return;
	destroy_profile(operation->profile);
	free(operation->type);
	free(operation);
}

char* get_operation_type(Operation* operation)
{
	/*
	Get the type of an operation
	Parameters: operation->pointer to the operation
	Return: a pointer to the type of the operation
	*/
	return operation->type;
}

Profile* get_profile_from_operation(Operation* operation)
{
	/*
	Get the profile from an operation
	Parameters: operatoin->pointer to the operation
	Return: a pointer to the profile of the operation
	*/
	return operation->profile;
}

Operation* copy_operation(Operation* operation)
{
	/*
	Create a copy of an operation
	Parameters: operation->pointer to the operation
	Return: pointer to the copy of the operation
	*/
	Operation* copy_operation = create_operation(get_profile_from_operation(operation), get_operation_type(operation));
	return copy_operation;
}

OperationsStack* create_operations_stack()
{
	/*
	Create a new variable of type OperationsStack by dynamically allocating memory for it
	Return: a pointer to the created operations stack
	*/
	OperationsStack* newOperationsStack = (OperationsStack*)malloc(sizeof(OperationsStack));
	if (newOperationsStack == NULL)
		return NULL;
	newOperationsStack->length = 0;
	return newOperationsStack;
}

void destroy_operations_stack(OperationsStack* operationsStack)
{
	/*
	Free memory allocated for an operations stack
	Parameters: operationsStack-> a pointer to the stack of operations
	*/
	for (int i = 0; i < operationsStack->length; ++i)
		destroy_operation(operationsStack->operations[i]);
	free(operationsStack);
}

void push_to_operations_stack(OperationsStack* operationsStack, Operation* operation)
{
	/*
	Push an operation to an operations stack
	Parameters: operationsStack->pointer to the stack of operations
				operation->pointer to the operation to be added
	*/
	Operation* copyOperation = copy_operation(operation);
	operationsStack->operations[operationsStack->length] = copyOperation;
	operationsStack->length++;
}

Operation* pop_from_operations_stack(OperationsStack* operationsStack)
{	
	/*
	Pop an operation from an operations stack
	Parameters: operationsStack->pointer to the stack of operations
	Return: pointer to the poped operation
	*/
	operationsStack->length--;
	return operationsStack->operations[operationsStack->length];
}

int operations_stack_is_empty(OperationsStack* operationsStack)
{
	/*
	Check if an operations stack is empty
	Parameters: operationsStack->pointer tot the stack of operations
	Return: 1 if the stack is empty
			0 otherwise
	*/
	if (operationsStack->length == 0)
		return 1;
	return 0;
}
