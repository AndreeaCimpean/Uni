#include "Service.h"
#include <time.h>

using namespace std;

void Service::addAnalysis(std::shared_ptr<MedicalAnalysis> analysis)
{
	this->repository.addAnalysis(analysis);
}

std::vector<std::shared_ptr<MedicalAnalysis>> Service::getAllAnalyses() const
{
	return this->repository.getAllAnalyses();
}

std::vector<std::shared_ptr<MedicalAnalysis>> Service::getAnalysesByMonth(const int month) const
{
	auto analyses = this->getAllAnalyses();
	std::vector<std::shared_ptr<MedicalAnalysis>> filteredAnalyes;
	for (auto anaysis : analyses)
	{
		if (stoi(anaysis->get_date().substr(5, 2)) == month)
			filteredAnalyes.push_back(anaysis);
	}
	return filteredAnalyes;
}

bool Service::isIll()
{
	time_t theTime = time(NULL);
	tm* now = localtime(&theTime);
	int month = now->tm_mon + 1;
	auto analyses = this->getAnalysesByMonth(month);
	for (auto analysis : analyses)
		if (analysis->isResultOk())
			return false;
	return true;
}

std::vector<std::shared_ptr<MedicalAnalysis>> Service::getAnalysesBetweenDates(const std::string& date1, const std::string& date2)
{
	auto analyses = this->getAllAnalyses();
	std::vector<std::shared_ptr<MedicalAnalysis>> filteredAnalyes;
	for (auto anaysis : analyses)
	{
		if (anaysis->get_date() >= date1 && anaysis->get_date() <= date2 )
			filteredAnalyes.push_back(anaysis);
	}
	return filteredAnalyes;
}

void Service::writeToFile(const std::string& filename, const std::string& date1, const std::string& date2)
{
	auto analyses = this->getAnalysesBetweenDates(date1, date2);
	this->repository.writeToFile(filename, analyses);
}
