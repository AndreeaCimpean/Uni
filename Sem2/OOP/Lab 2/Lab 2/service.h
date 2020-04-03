#pragma once
#include "repository.h"
#include "domain.h"

typedef struct
{
	Repository* repository;
} Service;

Service create_service(Repository* repository);
Profile* get_all_profiles_service(Service* service);
void list_profiles_filtered_by_psychological_profile_service(Profile* filteredList, int* lengthOfFilteredList, Service* service, char psychologicalProfile[]);
int add_profile_service(Service* service, int profileId, char placeOfBirth[], char psychologicalProfile[], int yearsOfRecordedService);
int update_profile_service(Service* service, int profileId, char newPlaceOfBirth[], char newPsychologicalProfile[], int newYearsOfRecordedService);
int delete_profile_service(Service* service, int profileId);
int get_number_of_profiles_service(Service* service);