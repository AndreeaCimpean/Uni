#include "repository.h"
#include <string.h>
#include <stdlib.h>

Repository* create_repository()
{
	/*
	Create a new variable of type Repository by dynamically allocating memory for it
	Return: a pointer to the created repository
			NULL if could not allocate memory
	*/
	Repository* newRepository = (Repository*)malloc(sizeof(Repository));
	if (newRepository == NULL)
		return NULL;
	newRepository->profiles = create_dynamic_array(INITIAL_CAPACITY);
	return newRepository;
}

void destroy_repository(Repository* repository)
{
	/*
	Free memory allocated to a repository and its dynamic array
	Parameters: repository->pointer to the repository
	*/
	if (repository == NULL)
		return;
	destroy_dynamic_array(repository->profiles);
	free(repository);
}


int find_profile_index_by_profile_id(Repository* repository, int profileId)
{
	/*
	Find position of a profile in the profiles list of a repository
	Parameters: repository->pointer to the repository
				profileId->the id of the profile searched, integer
	Return:	the position of the profile in the list of profiles
			-1 if profile not in the list
	*/
	for (int i = 0; i < repository->profiles->length; ++i)
		if(get_profile_id_number(repository->profiles->elements[i]) == profileId)
			return i;
	return -1;
}

int add_profile_repository(Repository* repository, Profile* profile)
{
	/*
	Add a profile in a repository
	Parameters: repository->pointer to the repository
				profile->pointer to the profile to be added
	Return: 0 if the profile already exists
			1 if profile added
			
	*/
	if (find_profile_index_by_profile_id(repository, profile->profileIdNumber) != -1)
		return 0;
	add_element_dynamic_array(repository->profiles, profile);
	return 1;
}

Profile** get_all_profiles_repository(Repository* repository)
{
	/*
	Get all profiles from a repository
	Parameters: repository->pointer to the repository
	Return: pointer to the list of profiles
	*/
	return repository->profiles->elements;
}

int update_profile_repository(Repository* repository, int profileId, char* newPlaceOfBirth, char* newPsychologicalProfile, int newYearsOfRecordedService)
{
	/*
	Update a profile from repository
	Parameters: repository->pointer to the repository
				profileId->id of the profile to be updated, integer
				newPlafeOfBirth->the new place of birth, pointer to string
				newPsychologicalProfile->the new psychological profile, pointer to string
				newYearsOfRecordedService->the new number of years of service, integer
	Return:	1 if successfully updated the profile
			0 otherwise(profile not found) 
	*/
	int found_profile = find_profile_index_by_profile_id(repository, profileId);
	if (found_profile == -1)
		return 0;
	repository->profiles->elements[found_profile]->yearsOfRecordedService = newYearsOfRecordedService;
	strcpy(repository->profiles->elements[found_profile]->placeOfBirth, newPlaceOfBirth);
	strcpy(repository->profiles->elements[found_profile]->psychologicalProfile, newPsychologicalProfile);
	return 1;
}

int delete_profile_repository(Repository* repository, int profileId)
{
	/*
	Delete a profile from a repository
	Parameters: repository->pointer to the repository
				profileId->the id of the profile to be deleted
	Return: 1 if successfullt deleted the profile
			0 otherwise(profile not found)
	*/
	int found_profile = find_profile_index_by_profile_id(repository, profileId);
	if (found_profile == -1)
		return 0;
	delete_element_from_dynamic_array(repository->profiles, found_profile);
	return 1;
}

int get_number_of_profiles_repository(Repository* repository)
{
	/*
	Get the number of profiles from a repository
	Parameters: repository->pointer to the repository
	Return: the number of profiles
	*/
	return repository->profiles->length;
}

Profile* get_profile_from_list_of_profiles(Repository* repository, int profileId)
{
	/*
	Get a profile from profiles list of a repository
	Parameteres: repository->pointer to the repository
				 profileId-> the id of the serched profile
	Return: a pointer to the profile
	*/
	return repository->profiles->elements[find_profile_index_by_profile_id(repository, profileId)];
}
