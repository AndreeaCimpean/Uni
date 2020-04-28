#include "tests.h"
#include "Validations.h"
#include <vector>
#include <fstream>

using namespace std;

void TestEvidence::equal_evidences__two_equal_evidences__true()
{
	Evidence some_evidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence same_evidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	assert(some_evidence == same_evidence);
}

void TestEvidence::equal_evidences__two_different_evidences__false()
{
	Evidence some_evidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence other_evidence{ "ab", "11X3X4", 0.1, 3, "abc" };
	assert(!(some_evidence == other_evidence));
}

void TestMemoryRepository::find_evidence_by_id__existing_id__index_found()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	someRepository.add_evidence(someEvidence);
	assert(someRepository.find_evidence_by_id("abc") == 0);
}

void TestMemoryRepository::find_evidence_by_id__nonexisting_id__return_code()
{
	MemoryRepository someRepository{};
	assert(someRepository.find_evidence_by_id("abc") == -1);
}

void TestMemoryRepository::add_evidence__valid_evidence__evidence_added()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	someRepository.add_evidence(someEvidence);
	assert(someRepository.get_evidence_by_id("abc") == someEvidence);
}

void TestMemoryRepository::add_evidence__duplicate_evidence__throw_exception()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	someRepository.add_evidence(someEvidence);
	try
	{
		someRepository.add_evidence(someEvidence);}
	catch (...)
	{
		assert(true);
	}
}

void TestMemoryRepository::update_evidence__valid_evidence__evidence_updated()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	someRepository.add_evidence(someEvidence);
	Evidence newEvidence{ "abc", "12X4X5", 0.2, 4, "def" };
	someRepository.update_evidence(newEvidence.get_id(), newEvidence.get_measurement(), newEvidence.get_image_clarity_level(), newEvidence.get_quantity(), newEvidence.get_photograph());
	assert(someRepository.get_evidence_by_id("abc") == newEvidence);
}

void TestMemoryRepository::update_evidence__nonexisting_evidence__throw_exception()
{
	MemoryRepository someRepository{};
	try
	{
		someRepository.update_evidence("abc", "12X3X4", 0.2, 2, "abc"); }
	catch (...)
	{
		assert(true);
	}
}

void TestMemoryRepository::delete_evidence__valid_evidence__deleted_evidence()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	someRepository.add_evidence(someEvidence);
	someRepository.delete_evidence(someEvidence.get_id());
	assert(someRepository.find_evidence_by_id(someEvidence.get_id()) == -1);
}

void TestMemoryRepository::delete_evidence__nonexisting_evidence__throw_exception()
{
	MemoryRepository someRepository{};
	try
	{
		someRepository.delete_evidence("abc"); }
	catch (...)
	{
		assert(true);
	}
}

void TestMemoryRepository::get_evidence__nonexisting_evidence__throw_exception()
{
	MemoryRepository someRepository{};
	try
	{
		someRepository.get_evidence_by_id("abc"); }
	catch (...)
	{
		assert(true);
	}
}

void TestMemoryRepository::next_evidence__first_next__get_first_evidence()
{
	Evidence some_evidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence other_evidence{ "ab", "11X3X4", 0.1, 3, "abc" };
	MemoryRepository someRepository{};
	someRepository.add_evidence(some_evidence);
	someRepository.add_evidence(other_evidence);
	assert(someRepository.next_evidence() == some_evidence);
}

void TestMemoryRepository::next_evidence__end_of_list__get_first_evidence()
{
	Evidence some_evidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence other_evidence{ "ab", "11X3X4", 0.1, 3, "abc" };
	MemoryRepository someRepository{};
	someRepository.add_evidence(some_evidence);
	someRepository.add_evidence(other_evidence);
	someRepository.next_evidence();
	someRepository.next_evidence();
	assert(someRepository.next_evidence() == some_evidence);
}

void TestMemoryRepository::get_evidences_valid_input__get_all_evidences()
{
	Evidence some_evidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence other_evidence{ "ab", "11X3X4", 0.1, 3, "abc" };
	MemoryRepository someRepository{};
	someRepository.add_evidence(some_evidence);
	someRepository.add_evidence(other_evidence);
	vector<Evidence> evidences = someRepository.get_evidences();
	assert(evidences[0] == some_evidence && evidences[1] == other_evidence);
}

void TestTextFileRepository::find_evidence_by_id__existing_id__return_code()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	someRepository.add_evidence(someEvidence);
	assert(someRepository.find_evidence_by_id("abc") == 1);
}

void TestTextFileRepository::find_evidence_by_id__nonexisting_id__return_code()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	assert(someRepository.find_evidence_by_id("abc") == 0);
}

void TestTextFileRepository::add_evidence__valid_evidence__evidence_added()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	someRepository.add_evidence(someEvidence);
	assert(someRepository.get_evidence_by_id("abc") == someEvidence);
}

void TestTextFileRepository::add_evidence__duplicate_evidence__throw_exception()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	someRepository.add_evidence(someEvidence);
	try
	{
		someRepository.add_evidence(someEvidence); }
	catch (...)
	{
		assert(true);
	}
}

void TestTextFileRepository::update_evidence__valid_evidence__evidence_updated()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	someRepository.add_evidence(someEvidence);
	Evidence newEvidence{ "abc", "12X4X5", 0.2, 4, "def" };
	someRepository.update_evidence(newEvidence.get_id(), newEvidence.get_measurement(), newEvidence.get_image_clarity_level(), newEvidence.get_quantity(), newEvidence.get_photograph());
	assert(someRepository.get_evidence_by_id("abc") == newEvidence);
}

void TestTextFileRepository::update_evidence__nonexisting_evidence__throw_exception()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	try
	{
		someRepository.update_evidence("abc", "12X3X4", 0.2, 2, "abc"); }
	catch (...)
	{
		assert(true);
	}
}

void TestTextFileRepository::delete_evidence__valid_evidence__deleted_evidence()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab", "11X3X4", 0.1, 3, "abc" };
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	someRepository.add_evidence(someEvidence);
	someRepository.add_evidence(otherEvidence);
	someRepository.delete_evidence(someEvidence.get_id());
	assert(someRepository.find_evidence_by_id(someEvidence.get_id()) == 0);
}

void TestTextFileRepository::delete_evidence__nonexisting_evidence__throw_exception()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	try
	{
		someRepository.delete_evidence("abc"); }
	catch (...)
	{
		assert(true);
	}
}

void TestTextFileRepository::get_evidence__nonexisting_evidence__throw_exception()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	try
	{
		someRepository.get_evidence_by_id("abc"); }
	catch (...)
	{
		assert(true);
	}
}

void TestTextFileRepository::next_evidence__first_next__get_first_evidence()
{	
	ofstream file("empty.txt");
	file << "";
	file.close();
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab", "11X3X4", 0.1, 3, "abc" };
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	someRepository.add_evidence(someEvidence);
	someRepository.add_evidence(otherEvidence);
	assert(someRepository.next_evidence() == someEvidence);
}

void TestTextFileRepository::next_evidence__end_of_list__get_first_evidence()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab", "11X3X4", 0.1, 3, "abc" };
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	someRepository.add_evidence(someEvidence);
	someRepository.add_evidence(otherEvidence);
	someRepository.next_evidence();
	someRepository.next_evidence();
	assert(someRepository.next_evidence() == someEvidence);
}

void TestTextFileRepository::get_evidences_valid_input__get_all_evidences()
{
	ofstream file("empty.txt");
	file << "";
	file.close();
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab", "11X3X4", 0.1, 3, "abc" };
	TextFileRepository someRepository{};
	someRepository.set_file_name("empty.txt");
	someRepository.add_evidence(someEvidence);
	someRepository.add_evidence(otherEvidence);
	vector<Evidence> evidences = someRepository.get_evidences();
	assert(evidences[0] == someEvidence && evidences[1] == otherEvidence);
}


void TestService::add_evidence__valid_input__evidence_added()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	vector<Evidence> evidences = someService.get_evidences();
	assert(evidences[0] == someEvidence);
}

void TestService::update_evidence__valid_input__evidence_updated()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	Evidence newEvidence{ "abc", "12X4X5", 0.4, 2, "def" };
	someService.update_evidence(newEvidence.get_id(), newEvidence.get_measurement(), newEvidence.get_image_clarity_level(), newEvidence.get_quantity(), newEvidence.get_photograph());
	vector<Evidence> evidences = someService.get_evidences();
	assert(evidences[0] == newEvidence);
}

void TestService::delte_evidence__valid_input__deleted_evidence()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	someService.delete_evidence(someEvidence.get_id());
	assert(someService.get_number_of_evidences() == 0);
}

void TestService::save_physical_copy__valid_input__copy_added()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	someService.save_physical_copy(someEvidence.get_id());
	vector<Evidence> physical_copies = someService.get_physical_copies();
	assert(physical_copies[0] == someEvidence);
}

void TestService::update_evidence__valid_input__evidence_updated_in_physical_copies()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	someService.save_physical_copy(someEvidence.get_id());
	Evidence newEvidence{ "abc", "12X4X5", 0.4, 2, "def" };
	someService.update_evidence(newEvidence.get_id(), newEvidence.get_measurement(), newEvidence.get_image_clarity_level(), newEvidence.get_quantity(), newEvidence.get_photograph());
	vector<Evidence> physical_copies = someService.get_physical_copies();
	assert(physical_copies[0] == newEvidence);
}

void TestService::delete_evidence__valid_input__evidence_deleted_in_physical_copies()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab" ," 12X4X5", 0.6, 4, "ab" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	someService.add_evidence(otherEvidence);
	someService.save_physical_copy(someEvidence.get_id());
	someService.save_physical_copy(otherEvidence.get_id());
	someService.delete_evidence(someEvidence.get_id());
	vector<Evidence> physical_copies = someService.get_physical_copies();
	assert(physical_copies[0] == otherEvidence && someService.get_number_of_physical_copies() == 1);
}

void TestService::filter_evidences_by_measurement_and_quantity__both_conditions__filtered_list()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab", " 12X4X5", 0.6, 4, "ab" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	someService.add_evidence(otherEvidence);
	vector<Evidence> filteredList;
	string measurement = "12X3X4";
	double quantity = 3;
	someService.filter_evidences_by_measurement_and_quantity(filteredList, measurement, quantity);
	assert(filteredList[0] == someEvidence && filteredList.size() == 1);
}

void TestService::filter_evidences_by_measurement_and_quantity__only_measurement__filtered_list()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab" ," 12X4X5", 0.6, 4, "ab" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	someService.add_evidence(otherEvidence);
	vector<Evidence> filteredList;
	string measurement = "12X3X4";
	someService.filter_evidences_by_measurement_and_quantity(filteredList, measurement, -1);
	assert(filteredList[0] == someEvidence && filteredList.size() == 1);
}

void TestService::filter_evidences_by_measurement_and_quantity__only_quantity_greater__filtered_list()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab" ," 12X4X5", 0.6, 4, "ab" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	someService.add_evidence(otherEvidence);
	vector<Evidence> filteredList;
	int quantity = 2;
	someService.filter_evidences_by_measurement_and_quantity(filteredList, "", quantity);
	assert(filteredList[0] == someEvidence && filteredList[1] == otherEvidence);
}

void TestService::set_file__valid_repository__file_set()
{
	TextFileRepository someRepository{};
	Service someService{ someRepository };
	string file = "evidences.txt";
	someService.set_file(file);
	assert(someRepository.get_file_name() == file);
}

void TestService::set_file__invalid_repository__file_set()
{
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	string file = "evidences.txt";
	try
	{
		someService.set_file(file); }
	catch(...)
	{
		assert(true);
	}
}

void TestService::next_evidence__second_next__get_second_evidence()
{
	Evidence someEvidence{ "abc", "12X3X4", 0.2, 3, "abc" };
	Evidence otherEvidence{ "ab" ," 12X4X5", 0.6, 4, "ab" };
	MemoryRepository someRepository{};
	Service someService{ someRepository };
	someService.add_evidence(someEvidence);
	someService.add_evidence(otherEvidence);
	someService.next_evidence();
	assert(someService.next_evidence() == otherEvidence);
}

void TestValidations::check_measurement__first_charcter_not_a_digit__throw_exception()
{
	string some_measurement = "a12X4X5";
	try
	{
		check_measurement(some_measurement); }
	catch(...)
	{
		assert(true);
	}
}

void TestValidations::check_measurement__less_than_three_dimensions__throw_exception()
{
	string some_measurement = "4X5";
	try
	{
		check_measurement(some_measurement); }
	catch (...)
	{
		assert(true);
	}
}

void TestValidations::check_measurement__some_invalid_string__throw_exception()
{
	string some_measurement = "abcd";
	try
	{
		check_measurement(some_measurement); }
	catch (...)
	{
		assert(true);
	}
}

void TestValidations::check_measurement__some_invalid_string_containingX__throw_exception()
{
	string some_measurement = "1XX2";
	try
	{
		check_measurement(some_measurement); }
	catch (...)
	{
		assert(true);
	}
}

void TestValidations::check_measurement__measurement_zero__throw_exception()
{
	string some_measurement = "1X0X2";
	try
	{
		check_measurement(some_measurement); }
	catch (...)
	{
		assert(true);
	}
}

void TestValidations::image_clarity_level__some_invalid_string__throw_exception()
{
	string some_image_clarity_level = "abcd";
	try
	{
		check_image_clarity_level(some_image_clarity_level); }
	catch (...)
	{
		assert(true);
	}
}

void TestValidations::image_clarity_level__some_invalid_string_containig_dots__throw_exception()
{
	string some_image_clarity_level = "a.b.cd";
	try
	{
		check_image_clarity_level(some_image_clarity_level); }
	catch (...)
	{
		assert(true);
	}
}

void TestValidations::quantity__some_invalid_string__throw_exception()
{
	string quantity = "abcd";
	try
	{
		check_quantity(quantity);	}
	catch (...)
	{
		assert(true);
	}
}

void TestValidations::quantity__some_invalid_string_containig_dots__throw_exception()
{
	string quantity = "1.2.cd";
	try
	{
		check_quantity(quantity); }
	catch (...)
	{
		assert(true);
	}
}


void test_all()
{
	TestEvidence test_evidences;
	test_evidences.equal_evidences__two_equal_evidences__true();
	test_evidences.equal_evidences__two_different_evidences__false();

	TestMemoryRepository test_memory_repository;
	test_memory_repository.find_evidence_by_id__existing_id__index_found();
	test_memory_repository.find_evidence_by_id__nonexisting_id__return_code();
	test_memory_repository.add_evidence__valid_evidence__evidence_added();
	test_memory_repository.add_evidence__duplicate_evidence__throw_exception();
	test_memory_repository.update_evidence__valid_evidence__evidence_updated();
	test_memory_repository.update_evidence__nonexisting_evidence__throw_exception();
	test_memory_repository.delete_evidence__valid_evidence__deleted_evidence();
	test_memory_repository.delete_evidence__nonexisting_evidence__throw_exception();
	test_memory_repository.get_evidence__nonexisting_evidence__throw_exception();
	test_memory_repository.next_evidence__first_next__get_first_evidence();
	test_memory_repository.next_evidence__end_of_list__get_first_evidence();
	test_memory_repository.get_evidences_valid_input__get_all_evidences();

	TestTextFileRepository test_text_file_repository;
	test_text_file_repository.find_evidence_by_id__existing_id__return_code();
	test_text_file_repository.find_evidence_by_id__nonexisting_id__return_code();
	test_text_file_repository.add_evidence__valid_evidence__evidence_added();
	test_text_file_repository.add_evidence__duplicate_evidence__throw_exception();
	test_text_file_repository.update_evidence__valid_evidence__evidence_updated();
	test_text_file_repository.update_evidence__nonexisting_evidence__throw_exception();
	test_text_file_repository.delete_evidence__valid_evidence__deleted_evidence();
	test_text_file_repository.delete_evidence__nonexisting_evidence__throw_exception();
	test_text_file_repository.get_evidence__nonexisting_evidence__throw_exception();
	test_text_file_repository.next_evidence__first_next__get_first_evidence();
	test_text_file_repository.next_evidence__end_of_list__get_first_evidence();
	test_text_file_repository.get_evidences_valid_input__get_all_evidences();

	TestService test_service;
	test_service.add_evidence__valid_input__evidence_added();
	test_service.update_evidence__valid_input__evidence_updated();
	test_service.delte_evidence__valid_input__deleted_evidence();
	test_service.save_physical_copy__valid_input__copy_added();
	test_service.update_evidence__valid_input__evidence_updated_in_physical_copies();
	test_service.delete_evidence__valid_input__evidence_deleted_in_physical_copies();
	test_service.filter_evidences_by_measurement_and_quantity__both_conditions__filtered_list();
	test_service.filter_evidences_by_measurement_and_quantity__only_measurement__filtered_list();
	test_service.filter_evidences_by_measurement_and_quantity__only_quantity_greater__filtered_list();
	test_service.set_file__valid_repository__file_set();
	test_service.set_file__invalid_repository__file_set();
	test_service.next_evidence__second_next__get_second_evidence();

	TestValidations test_validations;
	test_validations.check_measurement__first_charcter_not_a_digit__throw_exception();
	test_validations.check_measurement__less_than_three_dimensions__throw_exception();
	test_validations.check_measurement__some_invalid_string__throw_exception();
	test_validations.check_measurement__some_invalid_string_containingX__throw_exception();
	test_validations.check_measurement__measurement_zero__throw_exception();

	test_validations.image_clarity_level__some_invalid_string__throw_exception();
	test_validations.image_clarity_level__some_invalid_string_containig_dots__throw_exception();
	test_validations.quantity__some_invalid_string__throw_exception();
	test_validations.quantity__some_invalid_string_containig_dots__throw_exception();
}
