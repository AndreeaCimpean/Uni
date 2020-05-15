#include "Refrigerator.h"

using namespace std;

double Refrigerator::consumedElectricity()
{
	double consumedElectricity = 30;
	if (this->electricityUsageClass == "A")
		consumedElectricity *= 3;
	else if (this->electricityUsageClass == "A+")
		consumedElectricity *= 2.5;
	consumedElectricity *= 2;
	if (this->hasFreezer)
		consumedElectricity += 20;
	return consumedElectricity;
}

std::string Refrigerator::toString()
{
	string appliance = Appliance::toString();
	appliance += ", ";
	appliance += this->electricityUsageClass;
	appliance += ", ";
	appliance += to_string(this->hasFreezer);
	return appliance;
}

std::string Refrigerator::get_electricity_usage_class()
{
	return this->electricityUsageClass;
}
