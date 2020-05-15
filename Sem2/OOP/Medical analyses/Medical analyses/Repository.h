#pragma once
#include "MedicalAnalysis.h"
#include <vector>
#include <memory>

class Repository
{
private:
	std::vector<std::shared_ptr<MedicalAnalysis>> analyses;
public:
	Repository() {};
	void addAnalysis(std::shared_ptr<MedicalAnalysis> analysis);
	std::vector<std::shared_ptr<MedicalAnalysis>> getAllAnalyses() const;
	void writeToFile(const std::string& filename, std::vector<std::shared_ptr<MedicalAnalysis>> analyses);
};

