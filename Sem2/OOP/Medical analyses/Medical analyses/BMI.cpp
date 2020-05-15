#include "BMI.h"

using namespace std;

bool BMI::isResultOk() const
{
	if (this->value >= 18.5 && this->value <= 25)
		return true;
	return false;
}

std::string BMI::toString() const
{
	string analysis = MedicalAnalysis::toString();
	analysis += " type: BMI";
	analysis += " value: ";
	analysis += to_string(this->value);
	analysis += " result: ";
	if (this->isResultOk())
		analysis += "ok";
	else
		analysis += "not ok";
	return analysis;
}
