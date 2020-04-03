#pragma once

#define MAX_LENGTH_STRING 50

typedef struct
{
	int profileIdNumber;
	char* placeOfBirth;
	char* psychologicalProfile;
	int yearsOfRecordedService;
} Profile;

Profile* create_profile(int profileIdNumber, char* placeOfBirth, char* psychologicalProfile, int yearsOfRecordedService);
void destroy_profile(Profile* profile);
//Profile* copy_planet(Profile* profile);

int get_profile_id_number(Profile* profile);
int get_years_of_recorded_service(Profile* profile);
char* get_place_of_birth(Profile* profile);
char* get_pshycological_profile(Profile* profile);
