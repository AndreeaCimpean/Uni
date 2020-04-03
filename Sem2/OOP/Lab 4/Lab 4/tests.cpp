#include "tests.h"

void test_equal_evidences__two_equal_evidences__true()
{
	Evidence evidence1{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence evidence2{ "abc", "12X3X4", 0.2, 3, "abc" };
	assert(evidence1 == evidence2);
}

void test_equal_evidences__two_different_evidences__false()
{
	Evidence evidence1{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence evidence2{ "ab", "11X3X4", 0.1, 3, "abc" };
	assert(!(evidence1 == evidence2));
}

void test_dynamic_vector_resize__valid_input__increased_capacity()
{
	DynamicVector someDynamicVector{ 5 };
	someDynamicVector.resize();
	assert(someDynamicVector.get_capacity() == 10);
}

void test_dynamic_vector_resize__valid_input__same_elements()
{
	Evidence evidence1{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence evidence2{ "abd", "12X3X4", 0.2, 3, "abc" };
	DynamicVector someDynamicVector{ 5 };
	someDynamicVector.add_element(evidence1);
	someDynamicVector.add_element(evidence2);
	someDynamicVector.resize();
	assert(someDynamicVector.get_elements()[0] == evidence1 && someDynamicVector.get_elements()[1] == evidence2);
}

void test_dynamic_vector_add_element__without_resize__element_added()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	DynamicVector someDynamicVector{ 5 };
	someDynamicVector.add_element(someEvidence);
	assert(someDynamicVector.get_elements()[0] == someEvidence);
}

void test_dynamic_vector_add_element__with_resize__element_added()
{
	Evidence evidence1{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence evidence2{ "abd", "12X3X4", 0.2, 3, "abc" };
	DynamicVector someDynamicVector{ 1 };
	someDynamicVector.add_element(evidence1);
	someDynamicVector.add_element(evidence2);
	assert(someDynamicVector.get_elements()[1] == evidence2);
}

void test_dynamic_vector_add_element__valid_element__increased_vector_length()
{
	Evidence evidence1{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence evidence2{ "abd", "12X3X4", 0.2, 3, "abc" };
	DynamicVector someDynamicVector{ 5 };
	someDynamicVector.add_element(evidence1);
	someDynamicVector.add_element(evidence2);
	assert(someDynamicVector.get_size() == 2);
}

void test_dynamic_vector_delete_element__valid_elemnt__elemnet_deleted()
{
	Evidence evidence1{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence evidence2{ "abd", "12X3X4", 0.2, 3, "abc" };
	DynamicVector someDynamicVector{ 5 };
	someDynamicVector.add_element(evidence1);
	someDynamicVector.add_element(evidence2);
	someDynamicVector.delete_element(1);
	assert(someDynamicVector.get_elements()[0] == evidence1);
}

void test_dynamic_vector_delete_element__valid_element__decreased_vector_length()
{
	Evidence evidence1{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence evidence2{ "abd", "12X3X4", 0.2, 3, "abc" };
	DynamicVector someDynamicVector{ 5 };
	someDynamicVector.add_element(evidence1);
	someDynamicVector.add_element(evidence2);
	someDynamicVector.delete_element(0);
	assert(someDynamicVector.get_size() == 1);
}

void test_dynamic_vector_get_element__valid_input__get_element()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	DynamicVector someDynamicVector{ 5 };
	someDynamicVector.add_element(someEvidence);
	assert(someDynamicVector.get_element(0) == someEvidence);
}

void test_dynamic_vector_update_element__valid_input__element_updated()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	DynamicVector someDynamicVector{ 5 };
	someDynamicVector.add_element(someEvidence);
	Evidence newEvidence{ "abc", "12X4X5", 0.2, 4, "def" };
	someDynamicVector.update_element(0, newEvidence.get_measurement(), newEvidence.get_image_clarity_level(), newEvidence.get_quantity(), newEvidence.get_photograph());
	assert(someDynamicVector.get_element(0) == newEvidence);
}

void test_repository_find_evidence_index_by_id__existing_id__index_found()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Repository someRepository{};
	someRepository.add_evidence(someEvidence);
	assert(someRepository.find_evidence_index_by_id("abc") == 0);
}

void test_repository_find_evidence_index_by_id__nonexisting_id__return_code()
{
	Repository someRepository{};
	assert(someRepository.find_evidence_index_by_id("abc") == -1);
}

void test_repository_add_evidence__valid_evidence__evidence_added()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Repository someRepository{};
	someRepository.add_evidence(someEvidence);
	assert(someRepository.get_evidences()[0] == someEvidence);
}

void test_repository_add_evidence__duplicate_evidence__throw_exception()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Repository someRepository{};
	someRepository.add_evidence(someEvidence);
	try
	{
		someRepository.add_evidence(someEvidence);
		assert(false);
	}
	catch (...)
	{
		assert(true);
	}
}

void test_repository_update_evidence__valid_evidence__evidence_updated()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Repository someRepository{};
	someRepository.add_evidence(someEvidence);
	Evidence newEvidence{ "abc", "12X4X5", 0.2, 4, "def" };
	someRepository.update_evidence(newEvidence.get_id(), newEvidence.get_measurement(), newEvidence.get_image_clarity_level(), newEvidence.get_quantity(), newEvidence.get_photograph());
	assert(someRepository.get_evidences()[0] == newEvidence);
}

void test_repository_update_evidence__nonexisting_evidence__throw_exception()
{
	Repository someRepository{};
	try
	{
		someRepository.update_evidence("abc", "12X3X4", 0.2, 2, "abc");
		assert(false);
	}
	catch (...)
	{
		assert(true);
	}
}

void test_repository_delete_evidence__valid_evidence__deleted_evidence()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Repository someRepository{};
	someRepository.add_evidence(someEvidence);
	someRepository.delete_evidence(someEvidence.get_id());
	assert(someRepository.find_evidence_index_by_id(someEvidence.get_id()) == -1);
}

void test_repository_delete_evidence__nonexisting_evidence__throw_exception()
{
	Repository someRepository{};
	try
	{
		someRepository.delete_evidence("abc");
		assert(false);
	}
	catch (...)
	{
		assert(true);
	}
}

void test_service_add_evidence__valid_input__evidence_added()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Repository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence.get_id(), someEvidence.get_measurement(), someEvidence.get_image_clarity_level(), someEvidence.get_quantity(), someEvidence.get_photograph());
	assert(someService.get_evidences()[0] == someEvidence);
}

void test_service_update_evidence__valid_input__evidence_updated()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Repository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence.get_id(), someEvidence.get_measurement(), someEvidence.get_image_clarity_level(), someEvidence.get_quantity(), someEvidence.get_photograph());
	Evidence newEvidence{ "abc", "12X4X5", 0.4, 2, "def" };
	someService.update_evidence(newEvidence.get_id(), newEvidence.get_measurement(), newEvidence.get_image_clarity_level(), newEvidence.get_quantity(), newEvidence.get_photograph());
	assert(someService.get_evidences()[0] == newEvidence);
}

void test_service_delte_evidence__valid_input__deleted_evidence()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Repository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence.get_id(), someEvidence.get_measurement(), someEvidence.get_image_clarity_level(), someEvidence.get_quantity(), someEvidence.get_photograph());
	someService.delete_evidence(someEvidence.get_id());
	assert(someService.get_number_of_evidences() == 0);
}


void test_all()
{
	test_equal_evidences__two_equal_evidences__true();
	test_equal_evidences__two_different_evidences__false();

	
	test_dynamic_vector_resize__valid_input__increased_capacity();
	test_dynamic_vector_resize__valid_input__same_elements();
	test_dynamic_vector_add_element__without_resize__element_added();
	test_dynamic_vector_add_element__with_resize__element_added();
	test_dynamic_vector_add_element__valid_element__increased_vector_length();
	test_dynamic_vector_delete_element__valid_elemnt__elemnet_deleted();
	test_dynamic_vector_delete_element__valid_element__decreased_vector_length();
	test_dynamic_vector_get_element__valid_input__get_element();
	test_dynamic_vector_update_element__valid_input__element_updated();
	
	test_repository_find_evidence_index_by_id__existing_id__index_found();
	test_repository_find_evidence_index_by_id__nonexisting_id__return_code();
	test_repository_add_evidence__valid_evidence__evidence_added();
	test_repository_add_evidence__duplicate_evidence__throw_exception();
	test_repository_update_evidence__valid_evidence__evidence_updated();
	test_repository_update_evidence__nonexisting_evidence__throw_exception();
	test_repository_delete_evidence__valid_evidence__deleted_evidence();
	test_repository_delete_evidence__nonexisting_evidence__throw_exception();

	test_service_add_evidence__valid_input__evidence_added();
	test_service_update_evidence__valid_input__evidence_updated();
	test_service_delte_evidence__valid_input__deleted_evidence();
}
