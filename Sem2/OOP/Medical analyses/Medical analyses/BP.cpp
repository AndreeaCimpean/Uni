#include "BP.h"

using namespace std;

bool BP::isResultOk() const
{
	if (this->systolicValue >= 90 && this->systolicValue <= 119 && this->diastolicValue <= 60 && this->diastolicValue <= 79)
		return true;
	return false;
}

std::string BP::toString() const
{
	string analysis = MedicalAnalysis::toString();
	analysis += " type: BP ";
	analysis += "systolic value: ";
	analysis += to_string(this->systolicValue);
	analysis += " diastolic value: ";
	analysis += to_string(this->diastolicValue);
	analysis += " result: ";
	if (this->isResultOk())
		analysis += "ok";
	else
		analysis += "not ok";
	return analysis;
}
