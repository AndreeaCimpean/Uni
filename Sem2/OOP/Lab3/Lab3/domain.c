#include "domain.h"
#include <string.h>
#include <stdlib.h>

Profile* create_profile(int profileIdNumber, char* placeOfBirth, char* psychologicalProfile, int yearsOfRecordedService)
{
	/*
	Create a new variable of type Profile by dynamically allocating memory for it
	Parameters: profileIdNumber->the id of the new profile, integer
				placeOfBirth->the place of birth for the new profile, pointer to string
				psychologicalProfile->the psychological profile of the new profile, pointer to string
				yearsOfRecordedService->years of recorded service of the new profile, integer
	Return: a pointer to the created profile
			 NULL if could not allocate memory
	*/
	Profile* newProfile = (Profile*)malloc(sizeof(Profile));
	if (newProfile == NULL)
		return NULL;
	newProfile->profileIdNumber = profileIdNumber;
	newProfile->yearsOfRecordedService = yearsOfRecordedService;
	
	newProfile->placeOfBirth = (char*)malloc(sizeof(char) * (strlen(placeOfBirth) + 1));
	if (newProfile->placeOfBirth == NULL)
		return NULL;
	strcpy(newProfile->placeOfBirth, placeOfBirth);

	newProfile->psychologicalProfile = (char*)malloc(sizeof(char) * (strlen(psychologicalProfile) + 1));
	if (newProfile->psychologicalProfile == NULL)
		return NULL;
	strcpy(newProfile->psychologicalProfile, psychologicalProfile);

	return newProfile;
}

Profile* copy_profile(Profile* profile)
{
	/*
	Create a copy of a profile
	Parameters: profile->pointer to the profile to be copied
	Return: a pointer to the copy of the profile
	*/
	if (profile == NULL)
		return NULL;
	Profile* copyProfile = create_profile(get_profile_id_number(profile), get_place_of_birth(profile), get_pshycological_profile(profile), get_years_of_recorded_service(profile));
	return copyProfile;
}

void destroy_profile(Profile* profile)
{
	/*
	Free memory allocated for a profile
	Parameters: profile->pointer to the profile 
	*/
	free(profile->placeOfBirth);
	free(profile->psychologicalProfile);
	free(profile);
}


int get_profile_id_number(Profile* profile)
{
	/*
	Get the id of a profile
	Parameters: profile->the given profile
	Return: id of the profile
	*/
	return profile->profileIdNumber;
}

int get_years_of_recorded_service(Profile* profile)
{
	/*
	Get years of recorded service for a rofile
	Parameters: profile->pointer to the given profile
	Return: years of recorded service for the profile
	*/
	return profile->yearsOfRecordedService;
}

char* get_place_of_birth(Profile* profile)
{
	/*
	Get place of birth from a profile
	Parameters: profile->the given profile
	Return: pointer to the place of birth
	*/
	return profile->placeOfBirth;
}

char* get_pshycological_profile(Profile* profile)
{
	/*
	Get psychological profile from a profile
	Parameters: profile->the given profile
	Return: pointer to the psychological profile
	*/
	return profile->psychologicalProfile;
}
