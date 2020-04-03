#include "service.h"

Service create_service(Repository* repository)
{
	Service newService;
	newService.repository = repository;
	return newService;
}

Profile* get_all_profiles_service(Service* service)
{
	return get_all_profiles_repository(service->repository);
}

void list_profiles_filtered_by_psychological_profile_service(Profile* filteredList, int* lengthOfFilteredList, Service* service, char psychologicalProfile[])
{
	Profile* list_of_profiles = get_all_profiles_service(service);
	int number_of_profiles = get_number_of_profiles_service(service);
	for (int i = 0; i < number_of_profiles; ++i)
	{
		Profile current_profile = (*(list_of_profiles + i));
		if (strcmp(get_pshycological_profile(&current_profile), psychologicalProfile) == 0)
		{
			filteredList[*lengthOfFilteredList] = current_profile;
			(*lengthOfFilteredList)++;
		}
	}
}

int add_profile_service(Service* service, int profileId, char placeOfBirth[], char psychologicalProfile[], int yearsOfRecordedService)
{
	Profile newProfile = create_profile(profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService);
	return add_profile_repository(service->repository, newProfile);
}

int update_profile_service(Service* service, int profileId, char newPlaceOfBirth[], char newPsychologicalProfile[], int newYearsOfRecordedService)
{
	return update_profile_repository(service->repository, profileId, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService);
}

int delete_profile_service(Service* service, int profileId)
{
	return delete_profile_repository(service->repository, profileId);
}

int get_number_of_profiles_service(Service* service)
{
	return get_number_of_profiles_repository(service->repository);
}
