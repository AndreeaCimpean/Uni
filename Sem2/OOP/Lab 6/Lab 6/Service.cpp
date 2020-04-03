#include "Service.h"

void Service::add_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, double quantity, const std::string& photograph)
{
	Evidence evidence{ id, measurement, imageClarityLevel, quantity, photograph };
	this->repository.add_evidence(evidence);
}

void Service::update_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, double quantity, const std::string& photograph)
{
	this->repository.update_evidence(id, measurement, imageClarityLevel, quantity, photograph);
	int evidence_index_in_physical_copies = this->find_evidence_index_in_physical_copies_by_id(id);
	if (evidence_index_in_physical_copies != -1)
		this->physicalCopies.update_element(evidence_index_in_physical_copies, measurement, imageClarityLevel, quantity, photograph);
}

void Service::delete_evidence(const std::string& id)
{
	this->repository.delete_evidence(id);
	int evidence_index_in_physical_copies = this->find_evidence_index_in_physical_copies_by_id(id);
	if (evidence_index_in_physical_copies != -1)
		this->physicalCopies.delete_element(evidence_index_in_physical_copies);
}

Evidence* Service::get_evidences() const
{
	return this->repository.get_evidences();
}

int Service::get_number_of_evidences() const
{
	return this->repository.get_number_of_evidences();
}

Evidence Service::next_evidence()
{
	return this->repository.next_evidence();
}

void Service::save_physical_copy(const std::string& id)
{
	Evidence copy_evidence = this->repository.get_evidence_by_id(id);
	this->physicalCopies.add_element(copy_evidence);
}

int Service::find_evidence_index_in_physical_copies_by_id(const std::string& id)
{
	for (int i = 0; i < this->physicalCopies.get_size(); ++i)
		if (this->physicalCopies.get_element(i).get_id() == id)
			return i;
	return -1;
}

Evidence* Service::get_physical_copies() const
{
	return this->physicalCopies.get_elements();
}

int Service::get_number_of_physical_copies() const
{
	return this->physicalCopies.get_size();
}

void Service::filter_evidences_by_measurement_and_quantity(Evidence filtered_list[], int& length_filtered_list, const std::string& measurement, const double quantity) const
{
	Evidence* evidences = this->get_evidences();
	int number_of_evidences = this->get_number_of_evidences();

	if (measurement != "" && quantity != -1)
	{
		for (int i = 0; i < number_of_evidences; ++i)
		{
			Evidence current_evidence = *(evidences + i);
			if (current_evidence.get_measurement() == measurement && current_evidence.get_quantity() >= quantity)
			{
				filtered_list[length_filtered_list] = current_evidence;
				length_filtered_list++;
			}
		}
	}
	else if (measurement == "")
	{
		for (int i = 0; i < number_of_evidences; ++i)
		{
			Evidence current_evidence = *(evidences + i);
			if (current_evidence.get_quantity() >= quantity)
			{
				filtered_list[length_filtered_list] = current_evidence;
				length_filtered_list++;
			}
		}
	}
	else
	{
		for (int i = 0; i < number_of_evidences; ++i)
		{
			Evidence current_evidence = *(evidences + i);
			if (current_evidence.get_measurement() == measurement)
			{
				filtered_list[length_filtered_list] = current_evidence;
				length_filtered_list++;
			}
		}
	}
}
