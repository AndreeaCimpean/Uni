#include "MedicalAnalysis.h"

using namespace std;

std::string MedicalAnalysis::toString() const
{
	string analysis = "";
	analysis += "date: ";
	analysis += this->date;
	return analysis;
}

std::string MedicalAnalysis::get_date() const
{
	return this->date;
}
