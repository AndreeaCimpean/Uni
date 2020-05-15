#include "Service.h"
#include "MyExceptions.h"
#include "TextFileRepository.h"
#include "MemoryRepository.h"
#include "HTMLRepository.h"
#include <vector>
#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

void Service::add_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const double quantity, const std::string& photograph)
{
	Evidence evidence{ id, measurement, imageClarityLevel, quantity, photograph };
	this->evidenceValidator.validate(evidence);
	this->repository.add_evidence(evidence);
}

void Service::update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const double quantity, const std::string& photograph)
{
	/*
	Update an evidence in the list of evidences and in the physical copies as well
	*/
	Evidence evidence{ id, measurement, imageClarityLevel, quantity, photograph };
	this->evidenceValidator.validate(evidence);
	
	this->repository.update_evidence(id, measurement, imageClarityLevel, quantity, photograph);

	if (this->find_evidence_in_physical_copies_by_id(id))
		this->physicalCopiesRepository->update_evidence(id, measurement, imageClarityLevel, quantity, photograph);
}

void Service::delete_evidence(const std::string& id)
{
	/*
	Delete an evidence from the list of evidences and from the physical copies as well
	*/
	this->repository.delete_evidence(id);
	
	vector<Evidence> physicalCopies = this->get_physical_copies();
	if (this->find_evidence_in_physical_copies_by_id(id))
		this->physicalCopiesRepository->delete_evidence(id);
}

std::vector<Evidence> Service::get_evidences() const
{
	return this->repository.get_evidences();
}

int Service::get_number_of_evidences() const
{
	return this->repository.get_number_of_evidences();
}

Evidence Service::next_evidence()
{
	/*
	Return the next evidence to be displayed to the user
	*/
	return this->repository.next_evidence();
}

void Service::save_physical_copy(const std::string& id)
{
	/*
	Save a copy of an evidence in the list of physical copies
	parameter: id - the id of the evidence to be saved
	*/
	Evidence copy_evidence = this->repository.get_evidence_by_id(id);
	this->physicalCopiesRepository->add_evidence(copy_evidence);
}

int Service::find_evidence_in_physical_copies_by_id(const std::string& id) const
{
	/*
	Find an evidence in the list of physical copies by its id
	Return:
		1 - if found
		0 - otherwise
	*/
	vector<Evidence> physicalCopies = this->get_physical_copies();
	auto iterator_to_searched_evidence = std::find_if(physicalCopies.begin(), physicalCopies.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == physicalCopies.end())
		return 0;
	else
		return 1;
}

const std::vector<Evidence> Service::get_physical_copies() const
{
	return this->physicalCopiesRepository->get_evidences();
}

int Service::get_number_of_physical_copies() const
{
	return this->get_physical_copies().size();
}

std::vector<Evidence> Service::filter_evidences_by_measurement_and_quantity(const std::string& measurement, const double quantity) const
{
	/*
	Filter evidences by measurement and quantity
	parameter: measurement - the exact measurement
			   quantity - the minimum quantity
	If measurement is empty or the quntity is -1 filter evidences only by the other condition
	Return: the filtered list
	*/
	vector<Evidence> filtered_list;
	vector<Evidence> evidences = this->get_evidences();
	if (measurement != "" && quantity != -1)
	{
		copy_if(evidences.begin(), evidences.end(), back_inserter(filtered_list), [measurement, quantity](const Evidence evidence)->bool { return evidence.get_measurement() == measurement && evidence.get_quantity() >= quantity; });
	}
	else if (measurement == "")
	{
		copy_if(evidences.begin(), evidences.end(), back_inserter(filtered_list), [measurement, quantity](const Evidence evidence)->bool { return evidence.get_quantity() >= quantity; });
	}
	else
	{
		copy_if(evidences.begin(), evidences.end(), back_inserter(filtered_list), [measurement, quantity](const Evidence evidence)->bool { return evidence.get_measurement() == measurement; });
	}
	return filtered_list;
}

void Service::set_repository_file(const std::string& file)
{
	/*
	Set the file name for the text repository
	parameter: file - the name of the file
	Set the file name, if the repository of the service is a text repository
	Throw an exception if the repository of teh service is not a text one
	*/
	try
	{
		TextFileRepository& text_repository = dynamic_cast<TextFileRepository&>(this->repository);
		text_repository.set_file_name(file);
	}
	catch (bad_cast)
	{
		throw ServiceException("Wrong repository type!\n");
	}
}

void Service::set_physical_copies_file(const std::string& file)
{
	this->physicalCopiesRepository->set_file_name(file);
}

std::string Service::get_physical_copies_file() const
{
	return this->physicalCopiesRepository->get_file_name();
}

void Service::set_physical_copies_repository(TextFileRepository* repository)
{
	this->physicalCopiesRepository = repository;
}

