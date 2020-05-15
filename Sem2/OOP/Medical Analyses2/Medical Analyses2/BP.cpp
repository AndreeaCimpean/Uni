#include "BP.h"

using namespace std;

bool BP::isResultOk() const
{
	return (this->systolicValue >= 90 && this->systolicValue <= 119 && this->diastolicValue >= 60 && this->diastolicValue <= 79);
}

std::string BP::toString() const
{
	string analysis = MedicalAnalysis::toString();
	analysis += " type: BP ";
	analysis += "systolic value: ";
	analysis += to_string(this->systolicValue);
	analysis += " diastolic value: ";
	analysis += to_string(this->diastolicValue);
	return analysis;
}
