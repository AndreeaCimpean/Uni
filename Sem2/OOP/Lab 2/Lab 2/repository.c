#include "repository.h"
#include <string.h>

Repository create_repository()
{
	Repository* newRepository = (Repository*)malloc(sizeof(Repository));
	if (newRepository == NULL)
		return NULL;
	newRepository->capacity = capacity;
	newRepository->length = 0;
	newRepository->elements = (Profile**)malloc(capacity * sizeof(Profile*));
	if (newRepository->elements == NULL)
		return NULL;
	return newRepository;
}

void destroy_repository(Repository* repository)
{
	for(int i = 0; i < repository->length)
}

int find_profile_index_by_profile_id(Repository* repository, int profileId)
{
	/*
	return:
		the position of a profile in the list of profiles
		-1 if profile not in list
	*/
	for (int i = 0; i < repository->length; ++i)
		if(get_profile_id_number(repository->elements[i]) == profileId)
			return i;
	return -1;
}

int add_profile_repository(Repository* repository, Profile profile)
{
	if (find_profile_index_by_profile_id(repository, profile.profileIdNumber) != -1)
		return 0;
	repository->elements[repository->length++] = profile;
	return 1;
}

Profile* get_all_profiles_repository(Repository* repository)
{
	return repository->elements;
}

int update_profile_repository(Repository* repository, int profileId, char newPlaceOfBirth[], char newPsychologicalProfile[], int newYearsOfRecordedService)
{
	/*
	If profile found update it and return 1, otherwise return 0 
	*/
	int found_profile = find_profile_index_by_profile_id(repository, profileId);
	if (found_profile == -1)
		return 0;
	repository->elements[found_profile].yearsOfRecordedService = newYearsOfRecordedService;
	strcpy(repository->elements[found_profile].placeOfBirth, newPlaceOfBirth);
	strcpy(repository->elements[found_profile].psychologicalProfile, newPsychologicalProfile);
	return 1;
}

int delete_profile_repository(Repository* repository, int profileId)
{
	/*
	If profile found delete it and return 1, otherwise return 0
	*/
	int found_profile = find_profile_index_by_profile_id(repository, profileId);
	if (found_profile == -1)
		return 0;
	for (int i = found_profile; i < repository->length - 1; ++i)
		repository->elements[i] = repository->elements[i + 1];
	repository->length--;
	return 1;
}

int get_number_of_profiles_repository(Repository* repository)
{
	return repository->length;
}
