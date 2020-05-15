#include "Repository.h"
#include <fstream>

using namespace std;

void Repository::addAnalysis(std::shared_ptr<MedicalAnalysis> analysis)
{
	this->analyses.push_back(analysis);
}

std::vector<std::shared_ptr<MedicalAnalysis>> Repository::getAllAnalyses() const
{
	return this->analyses;
}

void Repository::writeToFile(const std::string& filename, std::vector<std::shared_ptr<MedicalAnalysis>> analyses)
{
	ofstream output_file(filename);
	for (auto analysis : analyses)
		output_file << analysis->toString() << endl;
	output_file.close();
}
