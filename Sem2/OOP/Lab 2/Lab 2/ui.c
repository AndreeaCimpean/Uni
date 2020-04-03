#include "ui.h"
#include <stdio.h>
#include <string.h>

UI create_ui(Service* service)
{
	UI newUI;
	newUI.service = service;
	return newUI;
}

void start(UI* ui)
{
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
				char psychologicalProfile[50];
				scanf("%s", psychologicalProfile);
				list_profiles_filtered_by_a_psychological_profile_ui(ui, psychologicalProfile);
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
		scanf("%s", command);
	}
}

void list_all_profiles_ui(UI* ui)
{
	Profile* list_of_profiles = get_all_profiles_service(ui->service);
	int number_of_profiles = get_number_of_profiles_service(ui->service);
	for (int i = 0; i < number_of_profiles; ++i)
	{
		Profile current_profile = (*(list_of_profiles + i));
		printf("Id: %d Place of birth: %s Psychological profile: %s Years of service: %d \n", current_profile.profileIdNumber, current_profile.placeOfBirth, current_profile.psychologicalProfile, current_profile.yearsOfRecordedService);
	}
}

void list_profiles_filtered_by_a_psychological_profile_ui(UI* ui, char psychologicalProfile[])
{
	Profile filteredList[MAX_DIMENSION_LIST_PROFILES];
	int lengthOfFilteredList = 0;
	list_profiles_filtered_by_psychological_profile_service(filteredList, &lengthOfFilteredList, ui->service, psychologicalProfile);
	for (int i = 0; i < lengthOfFilteredList; ++i)
	{
		Profile current_profile = filteredList[i];
		printf("Id: %d Place of birth: %s Psychological profile: %s Years of service: %d \n", current_profile.profileIdNumber, current_profile.placeOfBirth, current_profile.psychologicalProfile, current_profile.yearsOfRecordedService);
	}
}

void add_profile_ui(UI* ui, int profileId, char placeOfBirth[], char psychologicalProfile[], int yearsOfRecordedService)
{
	if (add_profile_service(ui->service, profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService) == 0)
		printf("No!\n");
}

void update_profile_ui(UI* ui, int profileId, char newPlaceOfBirth[], char newPsychologicalProfile[], int newYearsOfRecordedService)
{
	if (update_profile_service(ui->service, profileId, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService) == 0)
		printf("No!\n");
}

void delete_profile_ui(UI* ui, int profileId)
{
	if (delete_profile_service(ui->service, profileId) == 0)
		printf("No!\n");
}

