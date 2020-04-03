#include "service.h"
#include <stdlib.h>

Service* create_service(Repository* repository, OperationsStack* undoStack, OperationsStack* redoStack)
{
	/*
	Create a new variable of type Service by dynamically alocating memory for it
	Parameteres: repository->pointer to the repository of the new service
				 undoStack->pointer to the stack of undo operations
				 redoStack->pointer to the stack of redo operations
	Return: pointer to the created service 
			NULL if could not allocate memory
	*/
	Service* newService = (Service*)malloc(sizeof(Service));
	if (newService == NULL)
		return NULL;
	newService->repository = repository;
	newService->undoStack = undoStack;
	newService->redoStack = redoStack;
	return newService;
}

void destroy_service(Service* service)
{
	/*
	Free the memory allocated to a service and to its undo, redo stacks
	Parameters: service->pointer to the service
	*/
	destroy_repository(service->repository);
	destroy_operations_stack(service->undoStack);
	destroy_operations_stack(service->redoStack);
	free(service);
}

Profile** get_all_profiles_service(Service* service)
{
	/*
	Get all profiles
	Parameters: service->pointer to the service
	Return: pointer to the list of profiles from repository
	*/
	return get_all_profiles_repository(service->repository);
}

void get_profiles_filtered_by_psychological_profile_service(Profile** filteredList, int* lengthOfFilteredList, Service* service, char* psychologicalProfile)
{
	/*
	Get profiles filtered by a given psychological profile
	Parameteres: filteredList->pointer to a list of profile pointers, for storing the filtered profiles
				 lengthOfFilteredList->pointer to integer for storing the length of the filtered list
				 service->pointer to the service
				 psychologicalProfile->string pointer to the required psychological profile
	Return the filterd list using parameters filteredList and lengthOfFilteredList
	*/
	Profile** list_of_profiles = get_all_profiles_service(service);
	int number_of_profiles = get_number_of_profiles_service(service);
	for (int i = 0; i < number_of_profiles; ++i)
	{
		Profile* current_profile = list_of_profiles[i];
		if (strcmp(get_pshycological_profile(current_profile), psychologicalProfile) == 0)
		{
			filteredList[*lengthOfFilteredList] = current_profile;
			(*lengthOfFilteredList)++;
		}
	}
}

int add_profile_service(Service* service, int profileId, char* placeOfBirth, char* psychologicalProfile, int yearsOfRecordedService)
{
	/*
	Create a profile, call repository function to add it, register the operation for undo
	Parameters: service->pointer to the service
				profileId->the id of the new profile, integer
				placeOfBirth->string pointer to the place of birth of the new profile
				psychologicalProfile->string pointer to the psychological profile of the new profile
				yearsOfRecordedService-> years of service of the new profile
	Return: the result of adding the profile in the repository
	If profile added to repository register the operation for undo
	*/
	Profile* newProfile = create_profile(profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService);
	int result_of_adding_profile = add_profile_repository(service->repository, newProfile);
	if (result_of_adding_profile == 1)
	{
		Operation* newOperationUndo = create_operation(newProfile, "add");
		push_to_operations_stack(service->undoStack, newOperationUndo);
		destroy_operation(newOperationUndo);
	}
	else
	{
		destroy_profile(newProfile);
	}
	return result_of_adding_profile;
}

int update_profile_service(Service* service, int profileId, char* newPlaceOfBirth, char* newPsychologicalProfile, int newYearsOfRecordedService)
{
	/*
	Call repository function to update a profile and if successful, register the operation for undo  
	Parameters: service->pointer to the service
				profileId->id of the profile to be updated, integer
				newPlaceOfBirth->the new place of birth, pointer to string
				newPsychologicalProfile->the new psychological profile, pointer to string 
				newYearsOfRecordedService->new years of recorded service, integer
	Return: the result of the update(1 for success, 0 for profile not found)
	*/
	if(find_profile_index_by_profile_id(service->repository, profileId) == -1)
		return 0;
	else
	{
		Profile* profile_before_update = copy_profile(get_profile_from_profiles_service(service, profileId));
		update_profile_repository(service->repository, profileId, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService);
		Operation* newOperationUndo = create_operation(profile_before_update, "update");
		push_to_operations_stack(service->undoStack, newOperationUndo);
		destroy_operation(newOperationUndo);
		destroy_profile(profile_before_update);
		return 1;
	}
}

int delete_profile_service(Service* service, int profileId)
{
	/*
	Call repository function to delete a profile and if successful register operation for undo
	Parameteres: service->pointer tot the service
				 profileId->the id of the profile to be deleted
	Return: result of the delete(1 if successful, 0 if profile not found)
	*/
	
	if (find_profile_index_by_profile_id(service->repository, profileId) == -1)
		return 0;
	else
	{
		Profile* profile_before_delete = copy_profile(get_profile_from_profiles_service(service, profileId));
		delete_profile_repository(service->repository, profileId);
		Operation* newOperationUndo = create_operation(profile_before_delete, "delete");
		push_to_operations_stack(service->undoStack, newOperationUndo);
		destroy_operation(newOperationUndo);
		destroy_profile(profile_before_delete);
		return 1;
	}
}

int get_number_of_profiles_service(Service* service)
{
	/*
	Get the numer of profiles
	Parameters: service->pointer to the service
	Return: the number of profiles
	*/
	return get_number_of_profiles_repository(service->repository);
}

void get_newbies(Profile** filteredList, int* lengthOfFilteredList, Service* service, int maximumYearsOfService)
{
	/*
	Get newbies(those with a maximum years of service) in ascending order by place of birth
	Parameters: filterdList->pointer to a list of profile pointers, for storing the list of newbies
				lengthOfFilterdList->pointer to an integer for storing the length of the filterd list
				service->pointer to the service
				maximumYearsOfService->the limit of years of recorded service, integer
	Return the list of newbies using parameters filteredList and lengthOfFilteredList
	*/
	Profile** list_of_profiles = get_all_profiles_service(service);
	int number_of_profiles = get_number_of_profiles_service(service);
	for (int i = 0; i < number_of_profiles; ++i)
	{
		Profile* current_profile = list_of_profiles[i];
		if (current_profile->yearsOfRecordedService<maximumYearsOfService)
		{
			filteredList[*lengthOfFilteredList] = current_profile;
			(*lengthOfFilteredList)++;
		}
	}
	for (int i = 0; i < *lengthOfFilteredList - 1; ++i)
	{
		for (int j = 0; j < *lengthOfFilteredList; ++j)
		{
			if (strcmp(filteredList[i]->placeOfBirth, filteredList[j]->placeOfBirth) > 0)
			{
				Profile* auxiliary_profile = filteredList[i];
				filteredList[i] = filteredList[j];
				filteredList[j] = auxiliary_profile;
			}
		}
	}
}

Profile* get_profile_from_profiles_service(Service* service, int profileId)
{
	/*
	Get a profile from the list of profiles
	Parameters: service->pointer to the service
				profileId->the id of the searched profile
	Return: a pointer to the profile
	*/
	return get_profile_from_list_of_profiles(service->repository, profileId);
}

int undo(Service* service)
{
	/*
	Undo the last performed operation and regiser it for redo
	Parameters: service->pointer to the servcie
	Return:	0 if no more undos
			1 otherwise
	*/
	if (operations_stack_is_empty(service->undoStack))
		return 0;
	Operation* operation = pop_from_operations_stack(service->undoStack);
	Profile* profile = get_profile_from_operation(operation);
	if (strcmp(operation->type, "add") == 0)
	{
		Operation* newOperationRedo = create_operation(profile, "add");
		push_to_operations_stack(service->redoStack, newOperationRedo);
		destroy_operation(newOperationRedo);

		int profileId = get_profile_id_number(profile);
		delete_profile_repository(service->repository, profileId);
	}
	else if (strcmp(operation->type, "update") == 0)
	{
		Profile* current_profile = get_profile_from_profiles_service(service, profile->profileIdNumber);
		Operation* newOperationRedo = create_operation(current_profile, "update");
		push_to_operations_stack(service->redoStack, newOperationRedo);
		destroy_operation(newOperationRedo);

		int profileId = get_profile_id_number(profile);
		int yearsOfRecordedService = get_years_of_recorded_service(profile);
		char placeOfBirth[50], psychologicalProfile[50];
		strcpy(placeOfBirth, get_place_of_birth(profile));
		strcpy(psychologicalProfile, get_pshycological_profile(profile));
		update_profile_repository(service->repository, profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService);
	}
	else
	{
		Operation* newOperationRedo = create_operation(profile, "delete");
		push_to_operations_stack(service->redoStack, newOperationRedo);
		destroy_operation(newOperationRedo);

		int profileId = get_profile_id_number(profile);
		int yearsOfRecordedService = get_years_of_recorded_service(profile);
		char placeOfBirth[50], psychologicalProfile[50];
		strcpy(placeOfBirth, get_place_of_birth(profile));
		strcpy(psychologicalProfile, get_pshycological_profile(profile));
		Profile* newProfile = create_profile(profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService);
		add_profile_repository(service->repository, newProfile);
	}
	destroy_operation(operation);
	return 1;
}

int redo(Service* service)
{
	/*
	Redo the last performed operation and regiser it for undo
	Parameters: service->pointer to the servcie
	Return:	0 if no more redos
			1 otherwise
	*/
	if (operations_stack_is_empty(service->redoStack))
		return 0;
	Operation* operation = pop_from_operations_stack(service->redoStack);
	Profile* profile = get_profile_from_operation(operation);
	if (strcmp(operation->type, "add") == 0)
	{
		Operation* newOperationUndo = create_operation(profile, "add");
		push_to_operations_stack(service->undoStack, newOperationUndo);
		destroy_operation(newOperationUndo);

		int profileId = get_profile_id_number(profile);
		int yearsOfRecordedService = get_years_of_recorded_service(profile);
		char placeOfBirth[50], psychologicalProfile[50];
		strcpy(placeOfBirth, get_place_of_birth(profile));
		strcpy(psychologicalProfile, get_pshycological_profile(profile));
		Profile* newProfile = create_profile(profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService);
		add_profile_repository(service->repository, newProfile);
	}
	else if (strcmp(operation->type, "update") == 0)
	{
		Profile* profile_before_update = get_profile_from_profiles_service(service, profile->profileIdNumber);
		Operation* newOperationUndo = create_operation(profile_before_update, "update");
		push_to_operations_stack(service->undoStack, newOperationUndo);
		destroy_operation(newOperationUndo);

		int profileId = get_profile_id_number(profile);
		int yearsOfRecordedService = get_years_of_recorded_service(profile);
		char placeOfBirth[50], psychologicalProfile[50];
		strcpy(placeOfBirth, get_place_of_birth(profile));
		strcpy(psychologicalProfile, get_pshycological_profile(profile));
		update_profile_repository(service->repository, profileId, placeOfBirth, psychologicalProfile, yearsOfRecordedService);
	}
	else
	{
		Operation* newOperationUndo = create_operation(profile, "delete");
		push_to_operations_stack(service->undoStack, newOperationUndo);
		destroy_operation(newOperationUndo);

		int profileId = get_profile_id_number(profile);
		delete_profile_repository(service->repository, profileId);
	}
	destroy_operation(operation);
	return 1;
}
