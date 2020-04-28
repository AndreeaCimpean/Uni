#include "MemoryRepository.h"

using namespace std;

void MemoryRepository::add_evidence(const Evidence& evidence)
{
	/*
	Add an evidence to the memory repository
	If it already exists throw an exception
	*/
	if (this->find_evidence_by_id(evidence.get_id()) == -1)
		this->evidences.push_back(evidence);
	else
		throw "Duplicate evidence!";
}

int MemoryRepository::find_evidence_by_id(const std::string& id) const
{
	/*
	Find an evidence index in the list of evidences
	parameter: id - the id of the evidence
	return:
		-1 if it doesn't exist
		its index in the list of evidences otherwise
	*/
	auto iterator_to_searched_evidence = std::find_if(this->evidences.begin(), this->evidences.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == this->evidences.end())
		return -1;
	else
		return distance(this->evidences.begin(), iterator_to_searched_evidence); }

void MemoryRepository::update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph)
{
	/*
	Update an evidence
	parameter: id - the id of the evidence
			   meaurement - the new measurement
			   imageClarityLevel - the new image clarity level
			   quantity - the new quantity
			   photograph - the new photograph
	*/
	int evidence_index = this->find_evidence_by_id(id);
	if (evidence_index != -1)
	{
		this->evidences[evidence_index].set_measurement(measurement);
		this->evidences[evidence_index].set_image_clarity_level(imageClarityLevel);
		this->evidences[evidence_index].set_quantity(quantity);
		this->evidences[evidence_index].set_photograph(photograph);
	}
	else
		throw "Invalid id!";
}

void MemoryRepository::delete_evidence(const std::string& id)
{
	/*
	Delete an evidence from the repository
	parameters: id - the id of the evidence
	Throw an exception if it doesn't exist
	*/
	int evidence_index = this->find_evidence_by_id(id);
	if (evidence_index != -1)
		this->evidences.erase(this->evidences.begin() + evidence_index);
	else
		throw "Invalid id!";
}

std::vector<Evidence> MemoryRepository::get_evidences() const
{
	/*
	Get the list of evidences
	*/
	return this->evidences;
}

int MemoryRepository::get_number_of_evidences() const
{
	return this->evidences.size();
}


Evidence MemoryRepository::next_evidence()
{
	/*
	Return the next evidence to be displayed to the user
	*/
	Evidence evidence_before = this->evidences[evidencesIterator];
	evidencesIterator++;
	if (this->evidencesIterator == this->get_number_of_evidences())
		this->evidencesIterator = 0;
	return evidence_before;
}

Evidence MemoryRepository::get_evidence_by_id(const std::string& id) const
{
	/*
	Get an evidence given by its id
	Throw an exception if it doesn't exist
	*/
	int evidence_index = this->find_evidence_by_id(id);
	if (evidence_index == -1)
		throw "Id does not exist!";
	return this->evidences.at(evidence_index);
}
