#include "Service.h"

using namespace std;

void Service::add_analysis(std::shared_ptr<MedicalAnalysis> analysis)
{
	this->repository.add_analysis(analysis);
}

std::vector<std::shared_ptr<MedicalAnalysis>> Service::get_all_analyses() const
{
	return this->repository.get_all_analyses();
}

std::vector<std::shared_ptr<MedicalAnalysis>> Service::get_all_analyses_by_month(const int month) const
{
	auto analyses = this->get_all_analyses();
	std::vector<std::shared_ptr<MedicalAnalysis>> filteredAnalyses;
	for (auto analysis : analyses)
	{
		int analysis_month = stoi(analysis->get_date().substr(5, 2));
		if (month == analysis_month)
			filteredAnalyses.push_back(analysis);
	}
	return filteredAnalyses;
}

bool Service::isIll(const int month) const
{
	auto analyses = this->get_all_analyses_by_month(month);
	for (auto analysis : analyses)
		if (analysis->isResultOk())
			return false;
	return true;
}

std::vector<std::shared_ptr<MedicalAnalysis>> Service::get_analyses_between_two_dates(const std::string& date1, const std::string& date2)
{
	auto analyses = this->get_all_analyses();
	std::vector<std::shared_ptr<MedicalAnalysis>> filteredAnalyses;
	for (auto analysis : analyses)
		if(analysis->get_date() >= date1 && analysis->get_date() <= date2)
			filteredAnalyses.push_back(analysis);
	return filteredAnalyses;
}

void Service::write_to_file(const std::string& filename, const std::string& date1, const std::string& date2)
{
	this->repository.write_to_file(filename, this->get_analyses_between_two_dates(date1, date2));
}
