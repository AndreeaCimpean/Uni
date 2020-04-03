#pragma once
#include "Evidence.h"
#include "DynamicVector.h"

#define MAX_DIMENSION_LIST_EVIDENCES 100

class Repository
{
private:
	DynamicVector<Evidence> evidences;
	DynamicVector<Evidence>::iterator evidencesIterator = evidences.begin();
public:
	Repository() {}
	void add_evidence(const Evidence& evidence);
	int find_evidence_index_by_id(const std::string& id) const;
	void update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph);
	void delete_evidence(const std::string& id);
	Evidence* get_evidences() const;
	int get_number_of_evidences() const;
	Evidence next_evidence();
	Evidence& get_evidence_by_id(const std::string& std) const;
};

