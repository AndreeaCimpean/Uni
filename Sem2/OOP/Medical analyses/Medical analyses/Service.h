#pragma once
#include "Repository.h"

class Service
{
private:
	Repository& repository;
	std::string name;
public:
	Service(Repository& repository, const std::string& name) : repository{ repository }, name { name } {};
	void addAnalysis(std::shared_ptr<MedicalAnalysis> analysis);
	std::vector<std::shared_ptr<MedicalAnalysis>> getAllAnalyses() const;
	std::vector<std::shared_ptr<MedicalAnalysis>> getAnalysesByMonth(const int month) const;
	bool isIll();
	std::vector<std::shared_ptr<MedicalAnalysis>> getAnalysesBetweenDates(const std::string& date1, const std::string& date2);
	void writeToFile(const std::string& filename, const std::string& date1, const std::string& date2);
};

