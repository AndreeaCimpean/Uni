#pragma once
#include "Repository.h"
#include "Evidence.h"
class Service
{
private:
	Repository& repository;
public:
	Service(Repository& repository) : repository{repository} {}
	void add_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, int quantity, const std::string& photograph);
	void update_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, int quantity, const std::string& photograph);
	void delete_evidence(const std::string& id);
	Evidence* get_evidences() const;
	int get_number_of_evidences() const;
};

