#include "Repository.h"

void Repository::add_evidence(const Evidence& evidence)
{
	if (this->find_evidence_index_by_id(evidence.get_id()) == -1)
		this->evidences.add_element(evidence);
	else
		throw "Duplicate evidence!";
}

int Repository::find_evidence_index_by_id(const std::string& id)
{
	for (int i = 0; i < this->evidences.get_size(); ++i)
		if (this->evidences.get_element(i).get_id() == id)
			return i;
	return -1;
}

void Repository::update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph)
{
	int evidence_index = this->find_evidence_index_by_id(id);
	if (evidence_index != -1)
		this->evidences.update_element(evidence_index, measurement, imageClarityLevel, quantity, photograph);
	else
		throw "Invalid id!";
}

void Repository::delete_evidence(const std::string& id)
{
	int evidence_index = this->find_evidence_index_by_id(id);
	if (evidence_index != -1)
		this->evidences.delete_element(evidence_index);
	else
		throw "Invalid id!";
}

Evidence* Repository::get_evidences() const
{
	return this->evidences.get_elements();
}

int Repository::get_number_of_evidences() const
{
	return this->evidences.get_size();
}
