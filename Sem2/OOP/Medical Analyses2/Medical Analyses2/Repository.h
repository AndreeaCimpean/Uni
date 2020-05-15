#pragma once
#include <vector>
#include <memory>
#include "MedicalAnalysis.h"

class Repository
{
private:
	std::vector<std::shared_ptr<MedicalAnalysis>> analyses;
public:
	std::vector<std::shared_ptr<MedicalAnalysis>> get_all_analyses() const;
	void add_analysis(std::shared_ptr<MedicalAnalysis> analysis);
	void write_to_file(const std::string& filename, std::vector<std::shared_ptr<MedicalAnalysis>> analyses) const;
};

