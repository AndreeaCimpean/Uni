#pragma once
#include "Repository.h"
#include "MedicalAnalysis.h"

class Service
{
private:
	Repository& repository;
public:
	Service(Repository& repository) : repository{ repository } {};
	void add_analysis(std::shared_ptr<MedicalAnalysis> analysis);
	std::vector<std::shared_ptr<MedicalAnalysis>> get_all_analyses() const;
	std::vector<std::shared_ptr<MedicalAnalysis>> get_all_analyses_by_month(const int month) const;
	bool isIll(const int month) const;
	std::vector<std::shared_ptr<MedicalAnalysis>> get_analyses_between_two_dates(const std::string& date1, const std::string& date2);
	void write_to_file(const std::string& filename, const std::string& date1, const std::string& date2);
};

