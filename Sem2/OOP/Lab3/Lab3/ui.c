#include "ui.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

UI* create_ui(Service* service)
{
	/*
	Create a new variable of type UI by dynamically allocating memory for it
	Parameters: service->pointer to the service of the new ui
	Return: pointer to the allocated memory
			NULL if could not allocate memory
	*/
	UI* newUI = (UI*)malloc(sizeof(UI));
	if (newUI == NULL)
		return NULL;
	newUI->service = service;
	return newUI;
}

void destroy_ui(UI* ui)
{
	/*
	Free memory allocated for ui, and its service
	Parameters: ui-> pointer to the ui
	*/
	destroy_service(ui->service);
	free(ui);
}

void start(UI* ui)
{
	/*
	Read user input and call appropriate functions
	Parameters: ui->pointer to the ui
	*/
	char command[MAX_LENGTH_STRING];
	char delimiter;
	scanf("%s", command);
	while (strcmp(command, "exit") != 0)
	{
		if (strcmp(command, "list") == 0)
		{
			scanf("%c", &delimiter);
			if (delimiter == '\n')
				list_all_profiles_ui(ui);
			else
			{
				char read_string[50];
				scanf("%s", read_string);
				int string_contains_only_digits = 1;
				for (int i = 0; i < strlen(read_string); ++i)
					if (!isdigit(read_string[i]))
						string_contains_only_digits = 0;
				if (string_contains_only_digits)
				{
					int maximumYearsOfService = atoi(read_string);
					list_newbies(ui, maximumYearsOfService);
				}
				else
					list_profiles_filtered_by_a_psychological_profile_ui(ui, read_string);
			}
		}
		else if (strcmp(command, "add") == 0)
		{
			int profileId, yearsOfRecordedService;
			char psychologicalProfile[MAX_LENGTH_STRING], placeOfBirth[MAX_LENGTH_STRING];
			scanf("%d", &profileId);
			scanf("%c", &delimiter);
			scanf("%s", placeOfBirth);
			placeOfBirth[strlen(placeOfBirth) - 1] = NULL;
			scanf("%s", psychologicalProfile);
			psychologicalProfile[strlen(psychologicalProfile) - 1] = NULL;
			scanf("%d", &yearsOfRecordedService);
			add_profile_ui(ui, profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService);
		}
		else if (strcmp(command, "update") == 0)
		{
			int profileId, newYearsOfRecordedService;
			char newPsychologicalProfile[MAX_LENGTH_STRING], newPlaceOfBirth[MAX_LENGTH_STRING];
			scanf("%d", &profileId);
			scanf("%c", &delimiter);
			scanf("%s", newPlaceOfBirth);
			newPlaceOfBirth[strlen(newPlaceOfBirth) - 1] = NULL;
			scanf("%s", newPsychologicalProfile);
			newPsychologicalProfile[strlen(newPsychologicalProfile) - 1] = NULL;
			scanf("%d", &newYearsOfRecordedService);
			update_profile_ui(ui, profileId, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService);
		}
		else if (strcmp(command, "delete") == 0)
		{
			int profileId;
			scanf("%d", &profileId);
			delete_profile_ui(ui, profileId);
		}
		else if (strcmp(command, "undo") == 0)
			undo_ui(ui);
		else if (strcmp(command, "redo") == 0)
			redo_ui(ui);
		scanf("%s", command);
	}
}

void list_all_profiles_ui(UI* ui)
{
	/*
	Print all profiles
	Parameters: ui->pointer to the ui
	*/
	Profile** list_of_profiles = get_all_profiles_service(ui->service);
	int number_of_profiles = get_number_of_profiles_service(ui->service);
	for (int i = 0; i < number_of_profiles; ++i)
	{
		Profile* current_profile = list_of_profiles[i];
		printf("Id: %d Place of birth: %s Psychological profile: %s Years of service: %d \n", current_profile->profileIdNumber, current_profile->placeOfBirth, current_profile->psychologicalProfile, current_profile->yearsOfRecordedService);
	}
}

void list_profiles_filtered_by_a_psychological_profile_ui(UI* ui, char* psychologicalProfile)
{
	/*
	Print profiles filtered by psychological profile
	Parameters: ui->pointer to ui
				psychologicalProfile->the required profile, pointer to string
	*/
	Profile* filteredList[MAX_DIMENSION_LIST_PROFILES];
	int lengthOfFilteredList = 0;
	get_profiles_filtered_by_psychological_profile_service(filteredList, &lengthOfFilteredList, ui->service, psychologicalProfile);
	for (int i = 0; i < lengthOfFilteredList; ++i)
	{
		Profile* current_profile = filteredList[i];
		printf("Id: %d Place of birth: %s Psychological profile: %s Years of service: %d \n", current_profile->profileIdNumber, current_profile->placeOfBirth, current_profile->psychologicalProfile, current_profile->yearsOfRecordedService);
	}
}

void add_profile_ui(UI* ui, int profileId, char* placeOfBirth, char* psychologicalProfile, int yearsOfRecordedService)
{
	/*
	Call service function to add a new profile
	Parameters: ui->pointer to the ui
				profileId->the id of the profile, integer
				placeOfBirth->place of birth of the profile, pointer to string
				psychologicalProfile-> the psychological profile of the profile to be added, pointer to string
				yearsOfRecordedService->years of recorded service of the profile, integer
	If the profile can not be added(duplicate profile) print a message
	*/
	if (add_profile_service(ui->service, profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService) == 0)
		printf("No!\n");
}

void update_profile_ui(UI* ui, int profileId, char* newPlaceOfBirth, char* newPsychologicalProfile, int newYearsOfRecordedService)
{
	/*
	Call service function to update profile
	Parameters: ui->pointer to the ui
				profileId->the id of the profile to be updated, integer
				newPlaceOfBirth-> the new place of of birth, pointer to string
				newPsychologicalProfile-> the new psychological profile, pointer to string
				newYearsOfRecordedService-> the new number of years of recorded service, integer
	If profile can not be updated(doesn't exist) print a message 
	*/

	if (update_profile_service(ui->service, profileId, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService) == 0)
		printf("No!\n");
}

void delete_profile_ui(UI* ui, int profileId)
{
	/*
	Call service function to delete a profile
	Parameters: ui->pointer to the ui
				profileId-> the id of the profile to be deleted, integer
	If profile can not be deleted(doesn't exist) print a message
	*/
	if (delete_profile_service(ui->service, profileId) == 0)
		printf("No!\n");
}

void list_newbies(UI* ui, int maximumYearsOfService)
{
	/*
	Print newbies(those who don't exccesd a given number of years of service)
	Parameters: ui->pointer to the ui
				maximumYearsOfService->the maximum years of recorded service, integer
	*/
	Profile* filteredList[MAX_DIMENSION_LIST_PROFILES];
	int lengthOfFilteredList = 0;
	get_newbies(filteredList, &lengthOfFilteredList, ui->service, maximumYearsOfService);
	for (int i = 0; i < lengthOfFilteredList; ++i)
	{
		Profile* current_profile = filteredList[i];
		printf("Id: %d Place of birth: %s Psychological profile: %s Years of service: %d \n", current_profile->profileIdNumber, current_profile->placeOfBirth, current_profile->psychologicalProfile, current_profile->yearsOfRecordedService);
	}
}

void undo_ui(UI* ui)
{
	/*
	Call service function undo
	Parameters: ui->pointer to the ui
	If no more undos print a message
	*/
	if (undo(ui->service) == 0)
		printf("No more undos!");
}

void redo_ui(UI* ui)
{
	/*
	Call service function redo
	Paramters: ui->pointer to the ui
	If no more redos print a message
	*/
	if (redo(ui->service) == 0)
		printf("No more redos!");
}
