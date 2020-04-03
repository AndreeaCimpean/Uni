#include "tests.h"
#include <assert.h>
#include <string.h>


void test_all()
{
	test__create_profile__valid_input__created();
	test__copy_profile__valid_profile__copy_created();
	test__get_profile_id__valid_profile__get_id();
	test__get_years_of_recorded_service__valid_profile__get_years();
	test__get_place_of_birth__valid_profile__get_place();
	test__get_psychological_profile__valid_profile__get_psychological_profile();

	test__create_dynamic_array__valid_input__created();
	test__resize_dynamic_array__valid_array__increased_size();
	test__add_element_dynamic_array__valid_input_without_resize__added_element();
	test__add_element_dynamic_array__valid_input_with_resize__added_element();
	test__delete_element_from_dynamic_array__valid_input__deleted_element();
	test__get_length_dynamic_array__valid_array__get_length();
	test__get_element_from_dynamic_array__valid_position__get_element();
	test__get_element_from_dynamic_array__inavlid_postion__return_null();


	test__create_operation__valid_input__created_operation();
	test__get_operation_type__valid_operation__get_type();
	test__get_profile_from_operation__valid_operation__get_profile();
	test__copy_operation__valid_operation__copy_created();

	test__create_operations_stack__created_stack();
	test__push_to_operations_stack__valid_input__operation_added();
	test__pop_from_operations_stack__valid_stack__operation_popped();
	test__operations_stack_is_empty__valid_stack__check();

	
	test__create_repository__created_repository();
	test__find_profile_index_by_profile_id__existing_profile__get_index();
	test__find_profile_index_by_profile_id__non_existing_profile__return_code();
	test__add_profile_repository__valid_profile__added_profile();
	test__add_profile_repository__dupliacated_profile__return_code();
	test__get_all_profiles_repository__valid_repository__get_profiles();
	test__update_profile_repository__existing_profile__update_profile();
	test__update_profile_repository__non_existing_profile__return_code();
	test__delete_profile_repository__existing_profile__deleted_profile();
	test__delete_profile_repository__non_existing_profile__return_code();
	test__get_number_of_profiles_repository__valid_repository__get_number();
	test__get_profile_from_list_of_profiles__valid_input__get_profile();
	
	test__create_service__valid_input__created_service();
	test__get_all_profiles_service__valid_service__get_profiles();
	test__get_profiles_filtered_by_psychological_profile__valid_input__filtered_profiles();
	test__add_profile_service__valid_profile__added_profile();
	test__add_profile_service_duplicate_profile__return_code();
	test__update_profile_service__existing_profile__updated_profile();
	test__update_profile_service__non_existing_profile__return_code();
	test__delete_profile_service__existing_profile__deleted_profile();
	test__delete_profile_service_non_existing_profile__return_code();
	test__get_newbies__valid_input__get_list_of_newbies();
	test__get_profile_from_profiles_service__valid_input__get_profile();
	test__undo__can_undo__undo_last_operation();
	test__undo__no_more_undos__return_code();
	test__redo__can_redo__redo_the_last_operation();
	test__redo__no_more_redos__return_code();
}

void test__create_profile__valid_input__created()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* newProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(strcmp(newProfile->placeOfBirth, somePlaceOfBirth) == 0);
	assert(strcmp(newProfile->psychologicalProfile, somePsychologicalProfile) == 0);
	assert(newProfile->profileIdNumber == someProfileId);
	assert(newProfile->yearsOfRecordedService == someYearsOfRecordedService);
	destroy_profile(newProfile);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* newOtherProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(strcmp(newOtherProfile->placeOfBirth, somePlaceOfBirth) == 0);
	assert(strcmp(newOtherProfile->psychologicalProfile, somePsychologicalProfile) == 0);
	assert(newOtherProfile->profileIdNumber == someProfileId);
	assert(newOtherProfile->yearsOfRecordedService == someYearsOfRecordedService);
	destroy_profile(newOtherProfile);
}

void test__copy_profile__valid_profile__copy_created()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	Profile* copyProfile = copy_profile(someProfile);
	assert(someProfile->profileIdNumber == copyProfile->profileIdNumber);
	assert(someProfile->yearsOfRecordedService == copyProfile->yearsOfRecordedService);
	assert(strcmp(someProfile->placeOfBirth, copyProfile->placeOfBirth) == 0);
	assert(strcmp(someProfile->psychologicalProfile, copyProfile->psychologicalProfile) == 0);
	assert(someProfile != copy_profile);
	destroy_profile(someProfile);
	destroy_profile(copyProfile);
}

void test__get_profile_id__valid_profile__get_id()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	int profileId = get_profile_id_number(someProfile);
	assert(profileId == someProfile->profileIdNumber);
	destroy_profile(someProfile);
}

void test__get_years_of_recorded_service__valid_profile__get_years()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(get_years_of_recorded_service(someProfile) == someYearsOfRecordedService);
	destroy_profile(someProfile);
}

void test__get_place_of_birth__valid_profile__get_place()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(strcmp(get_place_of_birth(someProfile), somePlaceOfBirth) == 0);
	destroy_profile(someProfile);
}

void test__get_psychological_profile__valid_profile__get_psychological_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(strcmp(get_pshycological_profile(someProfile), somePsychologicalProfile) == 0);
	destroy_profile(someProfile);
}

void test__create_dynamic_array__valid_input__created()
{
	int someCapacity = 10;
	DynamicArray* someDynamicArray = create_dynamic_array(someCapacity);
	assert(someDynamicArray->length == 0);
	assert(someDynamicArray->capacity == someCapacity);
	destroy_dynamic_array(someDynamicArray);
}

void test__resize_dynamic_array__valid_array__increased_size()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	int someCapacity = 2;
	DynamicArray* someDynamicArray = create_dynamic_array(someCapacity);
	add_element_dynamic_array(someDynamicArray, profile1);
	add_element_dynamic_array(someDynamicArray, profile2);

	resize_dynamic_array(someDynamicArray);
	assert(someDynamicArray->capacity > someCapacity);
	assert(someDynamicArray->elements[0], profile1);
	assert(someDynamicArray->elements[1], profile2);
	assert(someDynamicArray->length == 2);
	destroy_dynamic_array(someDynamicArray);
}

void test__add_element_dynamic_array__valid_input_without_resize__added_element()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	int someCapacity = 10;
	DynamicArray* someDynamicArray = create_dynamic_array(someCapacity);
	
	add_element_dynamic_array(someDynamicArray, profile1);
	add_element_dynamic_array(someDynamicArray, profile2);
	assert(someDynamicArray->length == 2);
	assert(someDynamicArray->elements[0], profile1);
	assert(someDynamicArray->elements[1], profile2);
	destroy_dynamic_array(someDynamicArray);
}

void test__add_element_dynamic_array__valid_input_with_resize__added_element()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	int someCapacity = 1;
	DynamicArray* someDynamicArray = create_dynamic_array(someCapacity);

	add_element_dynamic_array(someDynamicArray, profile1);
	add_element_dynamic_array(someDynamicArray, profile2);
	assert(someDynamicArray->capacity > someCapacity);
	assert(someDynamicArray->length == 2);
	assert(someDynamicArray->elements[0], profile1);
	assert(someDynamicArray->elements[1], profile2);
	destroy_dynamic_array(someDynamicArray);
}

void test__delete_element_from_dynamic_array__valid_input__deleted_element()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	int someCapacity = 10;
	DynamicArray* someDynamicArray = create_dynamic_array(someCapacity);
	add_element_dynamic_array(someDynamicArray, profile1);
	add_element_dynamic_array(someDynamicArray, profile2);

	delete_element_from_dynamic_array(someDynamicArray, 0);
	assert(someDynamicArray->length == 1);
	assert(someDynamicArray->elements[0] == profile2);
	destroy_dynamic_array(someDynamicArray);
}

void test__get_length_dynamic_array__valid_array__get_length()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	int someCapacity = 10;
	DynamicArray* someDynamicArray = create_dynamic_array(someCapacity);
	assert(someDynamicArray->length == 0);
	add_element_dynamic_array(someDynamicArray, profile1);
	add_element_dynamic_array(someDynamicArray, profile2);
	assert(someDynamicArray->length == 2);
	destroy_dynamic_array(someDynamicArray);
}

void test__get_element_from_dynamic_array__valid_position__get_element()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	int someCapacity = 10;
	DynamicArray* someDynamicArray = create_dynamic_array(someCapacity);
	add_element_dynamic_array(someDynamicArray, profile1);
	add_element_dynamic_array(someDynamicArray, profile2);
	assert(get_element_from_dynamic_array(someDynamicArray, 0) == profile1);
	assert(get_element_from_dynamic_array(someDynamicArray, 1) == profile2);
	destroy_dynamic_array(someDynamicArray);
}

void test__get_element_from_dynamic_array__inavlid_postion__return_null()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	int someCapacity = 10;
	DynamicArray* someDynamicArray = create_dynamic_array(someCapacity);
	add_element_dynamic_array(someDynamicArray, profile1);
	add_element_dynamic_array(someDynamicArray, profile2);
	assert(get_element_from_dynamic_array(someDynamicArray, -4) == NULL);
	assert(get_element_from_dynamic_array(someDynamicArray, 5) == NULL);
	destroy_dynamic_array(someDynamicArray);
}

void test__create_operation__valid_input__created_operation()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	char someOperationType[] = "add";

	Operation* newOperation = create_operation(someProfile, someOperationType);
	assert(strcmp(newOperation->type, someOperationType) == 0);
	assert(strcmp(newOperation->profile->placeOfBirth, somePlaceOfBirth) == 0);
	assert(strcmp(newOperation->profile->psychologicalProfile, somePsychologicalProfile) == 0);
	assert(newOperation->profile->profileIdNumber == someProfileId);
	assert(newOperation->profile->yearsOfRecordedService == someYearsOfRecordedService);
	destroy_profile(someProfile);
	destroy_operation(newOperation);
}

void test__get_operation_type__valid_operation__get_type()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	char someOperationType[] = "add";

	Operation* someOperation = create_operation(someProfile, someOperationType);
	assert(strcmp(get_operation_type(someOperation), someOperationType) == 0);
	destroy_profile(someProfile);
	destroy_operation(someOperation);
}

void test__get_profile_from_operation__valid_operation__get_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	char someOperationType[] = "add";

	Operation* someOperation = create_operation(someProfile, someOperationType);
	
	Profile* profileOperation = get_profile_from_operation(someOperation);
	assert(strcmp(profileOperation->placeOfBirth, somePlaceOfBirth) == 0);
	assert(strcmp(profileOperation->psychologicalProfile, somePsychologicalProfile) == 0);
	assert(profileOperation->profileIdNumber == someProfileId);
	assert(profileOperation->yearsOfRecordedService == someYearsOfRecordedService);
	destroy_profile(someProfile);
	destroy_operation(someOperation);
}

void test__copy_operation__valid_operation__copy_created()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	char someOperationType[] = "add";

	Operation* someOperation = create_operation(someProfile, someOperationType);
	Operation* copyOperation = copy_operation(someOperation);
	
	assert(strcmp(copyOperation->type, someOperation->type) == 0);
	assert(strcmp(copyOperation->profile->placeOfBirth, someOperation->profile->placeOfBirth) == 0);
	assert(strcmp(copyOperation->profile->psychologicalProfile, someOperation->profile->psychologicalProfile) == 0);
	assert(copyOperation->profile->profileIdNumber == someOperation->profile->profileIdNumber);
	assert(copyOperation->profile->yearsOfRecordedService == someOperation->profile->yearsOfRecordedService);
	destroy_profile(someProfile);
	destroy_operation(someOperation);
	destroy_operation(copyOperation);
}

void test__create_operations_stack__created_stack()
{
	OperationsStack* newOperationsStack = create_operations_stack();
	assert(newOperationsStack->length == 0);
	destroy_operations_stack(newOperationsStack);
}

void test__push_to_operations_stack__valid_input__operation_added()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	char someOperationType[] = "add";

	Operation* someOperation = create_operation(someProfile, someOperationType);

	OperationsStack* someOperationsStack = create_operations_stack();
	push_to_operations_stack(someOperationsStack, someOperation);
	assert(someOperationsStack->length == 1);
	Operation* operationAdded = someOperationsStack->operations[0];
	assert(strcmp(operationAdded->type, someOperation->type) == 0);
	assert(strcmp(operationAdded->profile->placeOfBirth, someOperation->profile->placeOfBirth) == 0);
	assert(strcmp(operationAdded->profile->psychologicalProfile, someOperation->profile->psychologicalProfile) == 0);
	assert(operationAdded->profile->profileIdNumber == someOperation->profile->profileIdNumber);
	assert(operationAdded->profile->yearsOfRecordedService == someOperation->profile->yearsOfRecordedService);
	
	destroy_profile(someProfile);
	destroy_operation(someOperation);
	destroy_operations_stack(someOperationsStack);
}

void test__pop_from_operations_stack__valid_stack__operation_popped()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	char someOperationType[] = "add";

	Operation* someOperation = create_operation(someProfile, someOperationType);

	OperationsStack* someOperationsStack = create_operations_stack();
	push_to_operations_stack(someOperationsStack, someOperation);
	assert(someOperationsStack->length == 1);
	Operation* operationAdded = someOperationsStack->operations[0];
	assert(pop_from_operations_stack(someOperationsStack) == operationAdded);
	assert(someOperationsStack->length == 0);
	destroy_profile(someProfile);
	destroy_operation(someOperation);
	destroy_operation(operationAdded);
	destroy_operations_stack(someOperationsStack);
}

void test__operations_stack_is_empty__valid_stack__check()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	char someOperationType[] = "add";

	Operation* someOperation = create_operation(someProfile, someOperationType);

	OperationsStack* someOperationsStack = create_operations_stack();
	assert(operations_stack_is_empty(someOperationsStack) == 1);

	push_to_operations_stack(someOperationsStack, someOperation);
	assert(operations_stack_is_empty(someOperationsStack) == 0);

	destroy_profile(someProfile);
	destroy_operation(someOperation);
	destroy_operations_stack(someOperationsStack);
}

void test__create_repository__created_repository()
{
	Repository* newRepository = create_repository();
	assert(newRepository->profiles->length == 0);
	assert(newRepository->profiles->capacity == INITIAL_CAPACITY);
	destroy_repository(newRepository);
}

void test__find_profile_index_by_profile_id__existing_profile__get_index()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	
	Repository* someRepository = create_repository();
	add_profile_repository(someRepository, someProfile);
	assert(find_profile_index_by_profile_id(someRepository, someProfile->profileIdNumber) == 0);
	destroy_repository(someRepository);
}

void test__find_profile_index_by_profile_id__non_existing_profile__return_code()
{
	Repository* someRepository = create_repository();
	assert(find_profile_index_by_profile_id(someRepository, 0) == -1);
	destroy_repository(someRepository);
}

void test__add_profile_repository__valid_profile__added_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	Repository* someRepository = create_repository();
	assert(add_profile_repository(someRepository, someProfile) == 1);
	assert(someRepository->profiles->elements[0], someProfile);
	destroy_repository(someRepository);
}

void test__add_profile_repository__dupliacated_profile__return_code()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	Repository* someRepository = create_repository();
	add_profile_repository(someRepository, someProfile);
	assert(add_profile_repository(someRepository, someProfile) == 0);
	destroy_repository(someRepository);
}

void test__get_all_profiles_repository__valid_repository__get_profiles()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	Repository* someRepository = create_repository();
	add_profile_repository(someRepository, profile1);
	add_profile_repository(someRepository, profile2);
	Profile** list_of_profiles = get_all_profiles_repository(someRepository);
	assert(list_of_profiles[0] == profile1);
	assert(list_of_profiles[1] == profile2);
	destroy_repository(someRepository);
}

void test__update_profile_repository__existing_profile__update_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	char newPlaceOfBirth[] = "Alba";
	char newPsychologicalProfile[] = "def";
	int newYearsOfRecordedService = 4;

	Repository* someRepository = create_repository();
	add_profile_repository(someRepository, someProfile);
	assert(update_profile_repository(someRepository, someProfile->profileIdNumber, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService) == 1);
	assert(someRepository->profiles->elements[0]->profileIdNumber == someProfileId);
	assert(someRepository->profiles->elements[0]->yearsOfRecordedService == newYearsOfRecordedService);
	assert(strcmp(someRepository->profiles->elements[0]->placeOfBirth, newPlaceOfBirth) == 0);
	assert(strcmp(someRepository->profiles->elements[0]->psychologicalProfile, newPsychologicalProfile) == 0);
	destroy_repository(someRepository);
}

void test__update_profile_repository__non_existing_profile__return_code()
{
	int someProfileId = 12;
	char newPlaceOfBirth[] = "Alba";
	char newPsychologicalProfile[] = "def";
	int newYearsOfRecordedService = 4;

	Repository* someRepository = create_repository();
	assert (update_profile_repository(someRepository, someProfileId, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService) == 0);
	destroy_repository(someRepository);
}

void test__delete_profile_repository__existing_profile__deleted_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	Repository* someRepository = create_repository();
	add_profile_repository(someRepository, someProfile);
	assert(delete_profile_repository(someRepository, someProfile->profileIdNumber) == 1);
	assert(someRepository->profiles->length == 0);
	destroy_repository(someRepository);
}

void test__delete_profile_repository__non_existing_profile__return_code()
{
	int someProfileId = 12;

	Repository* someRepository = create_repository();
	assert(delete_profile_repository(someRepository, someProfileId) == 0);
	destroy_repository(someRepository);
}

void test__get_number_of_profiles_repository__valid_repository__get_number()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	Repository* someRepository = create_repository();
	assert(get_number_of_profiles_repository(someRepository) == 0);
	add_profile_repository(someRepository, someProfile);
	assert(get_number_of_profiles_repository(someRepository) == 1);
	destroy_repository(someRepository);
}

void test__get_profile_from_list_of_profiles__valid_input__get_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* someProfile = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	Repository* someRepository = create_repository();
	add_profile_repository(someRepository, someProfile);
	assert(get_profile_from_list_of_profiles(someRepository, someProfileId) == someProfile);
	destroy_repository(someRepository);
}

void test__create_service__valid_input__created_service()
{
	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* newService = create_service(repository, undoStack, redoStack);
	assert(newService->undoStack == undoStack);
	assert(newService->redoStack == redoStack);
	assert(newService->repository == repository);
	destroy_service(newService);
}

void test__get_all_profiles_service__valid_service__get_profiles()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	
	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_repository(repository, profile1);
	add_profile_repository(repository, profile2);
	Profile** list_of_profiles = get_all_profiles_service(service);
	assert(list_of_profiles[0] == profile1);
	assert(list_of_profiles[1] == profile2);
	destroy_service(service);
}

void test__get_profiles_filtered_by_psychological_profile__valid_input__filtered_profiles()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_repository(repository, profile1);
	add_profile_repository(repository, profile2);
	
	Profile* list_of_profiles[100];
	int length_list_of_profiles = 0;
	get_profiles_filtered_by_psychological_profile_service(list_of_profiles, &length_list_of_profiles, service, somePsychologicalProfile);
	assert(list_of_profiles[0] == profile2);
	assert(length_list_of_profiles == 1);
	destroy_service(service);
}

void test__add_profile_service__valid_profile__added_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	assert(add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService) == 1);
	assert(find_profile_index_by_profile_id(service->repository, someProfileId) != -1);
	assert(operations_stack_is_empty(service->undoStack) == 0);
	assert(operations_stack_is_empty(service->redoStack) == 1);
	destroy_service(service);
}

void test__add_profile_service_duplicate_profile__return_code()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(update_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService) == 1);
	destroy_service(service);
}

void test__update_profile_service__existing_profile__updated_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	

	char newPlaceOfBirth[] = "Alba";
	char newPsychologicalProfile[] = "def";
	int newYearsOfRecordedService = 4;

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(update_profile_service(service, someProfileId, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService) == 1);
	assert(repository->profiles->elements[0]->profileIdNumber == someProfileId);
	assert(repository->profiles->elements[0]->yearsOfRecordedService == newYearsOfRecordedService);
	assert(strcmp(repository->profiles->elements[0]->placeOfBirth, newPlaceOfBirth) == 0);
	assert(strcmp(repository->profiles->elements[0]->psychologicalProfile, newPsychologicalProfile) == 0);
	assert(operations_stack_is_empty(service->undoStack) == 0);
	assert(operations_stack_is_empty(service->redoStack) == 1);
	destroy_service(service);
}

void test__update_profile_service__non_existing_profile__return_code()
{
	int someProfileId = 12;
	char newPlaceOfBirth[] = "Alba";
	char newPsychologicalProfile[] = "def";
	int newYearsOfRecordedService = 4;
	
	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	assert(update_profile_service(service, someProfileId, newPlaceOfBirth, newPsychologicalProfile, newYearsOfRecordedService) == 0);
	destroy_service(service);
}

void test__delete_profile_service__existing_profile__deleted_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(delete_profile_service(service, someProfileId) == 1);
	assert(get_number_of_profiles_repository(repository) == 0);
	assert(operations_stack_is_empty(service->undoStack) == 0);
	assert(operations_stack_is_empty(service->redoStack) == 1);
	destroy_service(service);
}

void test__delete_profile_service_non_existing_profile__return_code()
{
	int someProfileId = 12;
	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	assert(delete_profile_service(service, someProfileId) == 0);
	destroy_service(service);
}

void test__get_newbies__valid_input__get_list_of_newbies()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	Profile* profile1 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	someProfileId = 1;
	strcpy(somePlaceOfBirth, "Alba");
	strcpy(somePsychologicalProfile, "def");
	someYearsOfRecordedService = 4;
	Profile* profile2 = create_profile(someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_repository(repository, profile1);
	add_profile_repository(repository, profile2);

	Profile* list_of_profiles[100];
	int length_list_of_profiles = 0;
	get_newbies(list_of_profiles, &length_list_of_profiles, service, 15);
	assert(list_of_profiles[0] == profile2);
	assert(list_of_profiles[1] == profile1);
	assert(length_list_of_profiles == 2);
	destroy_service(service);
}

void test__get_profile_from_profiles_service__valid_input__get_profile()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	assert(get_profile_from_profiles_service(service, someProfileId));
	destroy_service(service);
}

void test__undo__can_undo__undo_last_operation()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	undo(service);
	assert(repository->profiles->length == 0);
	assert(find_profile_index_by_profile_id(repository, someProfileId) == -1);
	assert(operations_stack_is_empty(redoStack) == 0);
	destroy_service(service);
}

void test__undo__no_more_undos__return_code()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;
	
	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	assert(undo(service) == 0);
	add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	undo(service);
	assert(undo(service) == 0);
	destroy_service(service);
}

void test__redo__can_redo__redo_the_last_operation()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	undo(service);
	redo(service);
	assert(operations_stack_is_empty(service->redoStack) == 1);
	assert(repository->profiles->length == 1);
	assert(repository->profiles->elements[0]->profileIdNumber == someProfileId);
	destroy_service(service);
}

void test__redo__no_more_redos__return_code()
{
	int someProfileId = 12;
	char somePlaceOfBirth[] = "Cluj";
	char somePsychologicalProfile[] = "abc";
	int someYearsOfRecordedService = 3;

	OperationsStack* undoStack = create_operations_stack();
	OperationsStack* redoStack = create_operations_stack();
	Repository* repository = create_repository();
	Service* service = create_service(repository, undoStack, redoStack);
	assert(redo(service) == 0);
	add_profile_service(service, someProfileId, somePlaceOfBirth, somePsychologicalProfile, someYearsOfRecordedService);
	undo(service);
	redo(service);
	assert(redo(service) == 0);
	destroy_service(service);
}

