#include "domain.h"
#include <string.h>
#include <stdlib.h>
#include <stdio.h>

Profile* create_profile(int profileIdNumber, char* placeOfBirth, char* psychologicalProfile, int yearsOfRecordedService)
{
	Profile* newProfile = (Profile*)malloc(sizeof(Profile));
	if (newProfile == NULL)
		return NULL;
	newProfile->profileIdNumber = profileIdNumber;
	newProfile->yearsOfRecordedService = yearsOfRecordedService;
	newProfile->placeOfBirth = (char*)malloc(sizeof(char) * (strlen(placeOfBirth) + 1));
	if (newProfile->placeOfBirth != NULL)
		strcpy(newProfile->placeOfBirth, placeOfBirth);
	newProfile->psychologicalProfile = (char*)malloc(sizeof(char) * strlen(psychologicalProfile) + 1);
	if (newProfile->psychologicalProfile != NULL)
		strcpy(newProfile->psychologicalProfile, psychologicalProfile);
	return newProfile;
}

void destroy_profile(Profile* profile)
{
	free(profile->placeOfBirth);
	free(profile->psychologicalProfile);
	free(profile);
}

int get_profile_id_number(Profile* profile)
{
	return profile->profileIdNumber;
}

int get_years_of_recorded_service(Profile* profile)
{
	return profile->yearsOfRecordedService;
}

char* get_place_of_birth(Profile* profile)
{
	return profile->placeOfBirth;
}

char* get_pshycological_profile(Profile* profile)
{
	return profile->psychologicalProfile;
}
