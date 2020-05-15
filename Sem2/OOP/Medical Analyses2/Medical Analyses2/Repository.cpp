#include "Repository.h"
#include <fstream>

using namespace std;

std::vector<std::shared_ptr<MedicalAnalysis>> Repository::get_all_analyses() const
{
	return this->analyses;
}

void Repository::add_analysis(std::shared_ptr<MedicalAnalysis> analysis)
{
	this->analyses.push_back(analysis);
}

void Repository::write_to_file(const std::string& filename, std::vector<std::shared_ptr<MedicalAnalysis>> analyses) const
{
	ofstream file(filename);
	for (auto analysis : analyses)
		file << analysis->toString()<<endl;
	file.close();
}
