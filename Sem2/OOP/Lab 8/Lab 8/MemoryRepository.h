#pragma once
#include "RepositoryInterafce.h"
#include "Evidence.h"
#include <vector>

#define MAX_DIMENSION_LIST_EVIDENCES 100

class MemoryRepository : public RepositoryInterface
{
private:
	std::vector<Evidence> evidences;
public:
	MemoryRepository() : RepositoryInterface{} {};
	void add_evidence(const Evidence& evidence) override;
	int find_evidence_by_id(const std::string& id) const override;
	void update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph) override;
	void delete_evidence(const std::string& id) override;
	std::vector<Evidence> get_evidences() const override;
	int get_number_of_evidences() const override;
	Evidence next_evidence() override;
	Evidence get_evidence_by_id(const std::string& id) const override;
};

