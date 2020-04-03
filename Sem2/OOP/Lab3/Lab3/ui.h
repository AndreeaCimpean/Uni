#pragma once
#include "service.h"

typedef struct
{
	Service* service;
} UI;

UI* create_ui(Service* service);
void destroy_ui(UI* ui);
void start(UI* ui);
void list_all_profiles_ui(UI* ui);
void list_profiles_filtered_by_a_psychological_profile_ui(UI* ui, char* psychologicalProfile);
void add_profile_ui(UI* ui, int profileId, char* placeOfBirth, char* psychologicalProfile, int yearsOfRecordedService);
void update_profile_ui(UI* ui, int profileId, char* newPlaceOfBirth, char* newPsychologicalProfile, int newYearsOfRecordedService);
void delete_profile_ui(UI* ui, int profileId);
void list_newbies(UI* ui, int maximumYearsOfService);
void undo_ui(UI* ui);
void redo_ui(UI* ui);
