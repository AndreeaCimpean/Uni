#include "Service.h"

void Service::add_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, int quantity, const std::string& photograph)
{
	Evidence evidence{ id, measurement, imageClarityLevel, quantity, photograph };
	this->repository.add_evidence(evidence);
}

void Service::update_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, int quantity, const std::string& photograph)
{
	this->repository.update_evidence(id, measurement, imageClarityLevel, quantity, photograph);
}

void Service::delete_evidence(const std::string& id)
{
	this->repository.delete_evidence(id);
}

Evidence* Service::get_evidences() const
{
	return this->repository.get_evidences();
}

int Service::get_number_of_evidences() const
{
	return this->repository.get_number_of_evidences();
}

