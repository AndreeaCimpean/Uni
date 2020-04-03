#pragma once
#include "domain.h"
#include "dynamicArray.h"

#define MAX_DIMENSION_LIST_PROFILES 100

typedef struct
{
	DynamicArray* profiles;
} Repository;

Repository* create_repository();
void destroy_repository(Repository* repository);
int find_profile_index_by_profile_id(Repository* repository, int profileId);
int add_profile_repository(Repository* repository, Profile* profile);
Profile** get_all_profiles_repository(Repository* repository);
int update_profile_repository(Repository* repository, int profileId, char* newPlaceOfBirth, char* newPsychologicalProfile, int newYearsOfRecordedService);
int delete_profile_repository(Repository* repository, int profileId);
int get_number_of_profiles_repository(Repository* repository);
Profile* get_profile_from_list_of_profiles(Repository* repository, int profieId);
