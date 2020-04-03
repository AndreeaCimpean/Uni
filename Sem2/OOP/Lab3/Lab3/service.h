#pragma once
#include "repository.h"
#include "domain.h"
#include "operationStack.h"

typedef struct
{
	Repository* repository;
	OperationsStack* undoStack;
	OperationsStack* redoStack;
} Service;

Service* create_service(Repository* repository, OperationsStack* undoStack, OperationsStack* redoStack);
void destroy_service(Service* service);
Profile** get_all_profiles_service(Service* service);
void get_profiles_filtered_by_psychological_profile_service(Profile** filteredList, int* lengthOfFilteredList, Service* service, char* psychologicalProfile);
int add_profile_service(Service* service, int profileId, char* placeOfBirth, char* psychologicalProfile, int yearsOfRecordedService);
int update_profile_service(Service* service, int profileId, char* newPlaceOfBirth, char* newPsychologicalProfile, int newYearsOfRecordedService);
int delete_profile_service(Service* service, int profileId);
int get_number_of_profiles_service(Service* service);
void get_newbies(Profile** filteredList, int* lengthOfFilteredList, Service* service, int maximumYearsOfService);
Profile* get_profile_from_profiles_service(Service* service, int profileId);
int undo(Service* service);
int redo(Service* service);