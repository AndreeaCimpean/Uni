#pragma once
#include "Repository.h"
#include "Evidence.h"
#include "DynamicVector.h"
class Service
{
private:
	Repository& repository;
	DynamicVector<Evidence> physicalCopies;
public:
	Service(Repository& repository) : repository{repository} {}
	void add_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, double quantity, const std::string& photograph);
	void update_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, double quantity, const std::string& photograph);
	void delete_evidence(const std::string& id);
	Evidence* get_evidences() const;
	int get_number_of_evidences() const;
	Evidence next_evidence();
	void save_physical_copy(const std::string& id);
	int find_evidence_index_in_physical_copies_by_id(const std::string& id);
	Evidence* get_physical_copies() const;
	int get_number_of_physical_copies() const;
	void filter_evidences_by_measurement_and_quantity(Evidence filtered_list[], int &length_filtered_list, const std::string& measurement, const double quantity) const;
};

