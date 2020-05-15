#include "BMI.h"

using namespace std;

std::string BMI::toString() const
{
	string analysis = MedicalAnalysis::toString();
	analysis += " type: BMI ";
	analysis += "value: ";
	analysis += to_string(this->value);
	return analysis;
}

bool BMI::isResultOk() const
{
	return (this->value >= 18.5 && this->value <= 25);
}
