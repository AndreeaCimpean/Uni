#pragma once
#include "Evidence.h"
#include <vector>

class RepositoryInterface
{
protected:
	int evidencesIterator;
public:
	RepositoryInterface() { this->evidencesIterator = 0; };
	virtual void add_evidence(const Evidence& evidence) = 0;
	virtual int find_evidence_by_id(const std::string& id) const = 0;
	virtual void update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph) = 0;
	virtual void delete_evidence(const std::string& id) = 0;
	virtual std::vector<Evidence> get_evidences() const = 0;
	virtual int get_number_of_evidences() const = 0;
	virtual Evidence next_evidence() = 0;
	virtual Evidence get_evidence_by_id(const std::string& id) const = 0;
	virtual ~RepositoryInterface() {};
};
