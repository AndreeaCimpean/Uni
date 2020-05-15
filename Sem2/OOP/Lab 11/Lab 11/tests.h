#pragma once
#include "Evidence.h"
#include "RepositoryInterafce.h"
#include "MemoryRepository.h"
#include "TextFileRepository.h"
#include "Service.h"
#include <assert.h>

class TestEvidence 
{
public:
	void equal_evidences__two_equal_evidences__true();
	void equal_evidences__two_different_evidences__false();
};

class TestMemoryRepository 
{
public:
	void find_evidence_by_id__existing_id__index_found();
	void find_evidence_by_id__nonexisting_id__return_code();
	void add_evidence__valid_evidence__evidence_added();
	void add_evidence__duplicate_evidence__throw_exception();
	void update_evidence__valid_evidence__evidence_updated();
	void update_evidence__nonexisting_evidence__throw_exception();
	void delete_evidence__valid_evidence__deleted_evidence();
	void delete_evidence__nonexisting_evidence__throw_exception();
	void get_evidence__nonexisting_evidence__throw_exception();
	void next_evidence__first_next__get_first_evidence();
	void next_evidence__end_of_list__get_first_evidence();
	void get_evidences_valid_input__get_all_evidences();

};

class TestTextFileRepository
{
public:
	void find_evidence_by_id__existing_id__return_code();
	void find_evidence_by_id__nonexisting_id__return_code();
	void add_evidence__valid_evidence__evidence_added();
	void add_evidence__duplicate_evidence__throw_exception();
	void update_evidence__valid_evidence__evidence_updated();
	void update_evidence__nonexisting_evidence__throw_exception();
	void delete_evidence__valid_evidence__deleted_evidence();
	void delete_evidence__nonexisting_evidence__throw_exception();
	void get_evidence__nonexisting_evidence__throw_exception();
	void next_evidence__first_next__get_first_evidence();
	void next_evidence__end_of_list__get_first_evidence();
	void get_evidences_valid_input__get_all_evidences();
};

class TestService
{
public:
	void add_evidence__valid_input__evidence_added();
	void update_evidence__valid_input__evidence_updated();
	void delte_evidence__valid_input__deleted_evidence();
	void save_physical_copy__valid_input__copy_added();
	void update_evidence__valid_input__evidence_updated_in_physical_copies();
	void delete_evidence__valid_input__evidence_deleted_in_physical_copies();
	void filter_evidences_by_measurement_and_quantity__both_conditions__filtered_list();
	void filter_evidences_by_measurement_and_quantity__only_measurement__filtered_list();
	void filter_evidences_by_measurement_and_quantity__only_quantity_greater__filtered_list();
	void set_file__valid_repository__file_set();
	void set_file__invalid_repository__file_set();
	void next_evidence__second_next__get_second_evidence();
};


void test_all();

