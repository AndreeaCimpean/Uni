#pragma once
#include "domain.h"
#include <string.h>

typedef struct
{
	Profile* profile;
	char* type;
} Operation;

Operation* create_operation(Profile* profile, char* operationType);
void destroy_operation(Operation* operation);
char* get_operation_type(Operation* operation);
Profile* get_profile_from_operation(Operation* operation);
Operation* copy_operation(Operation* operation);

typedef struct
{
	Operation* operations[100];
	int length;
} OperationsStack;

OperationsStack* create_operations_stack();
void destroy_operations_stack(OperationsStack* operationsStack);
void push_to_operations_stack(OperationsStack* operationsStack, Operation* operation);
Operation* pop_from_operations_stack(OperationsStack* operationsStack);
int operations_stack_is_empty(OperationsStack* operationsStack);