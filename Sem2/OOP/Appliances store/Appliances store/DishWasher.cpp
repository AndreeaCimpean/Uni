#include "DishWasher.h"

using namespace std;

double DishWasher::consumedElectricity()
{
    return this->consumedElectricityForOneHour * this->washingCycleLength * 8;
}

std::string DishWasher::toString()
{
	string appliance = Appliance::toString();
	appliance += ", ";
	appliance += to_string(this->washingCycleLength);
	appliance += ", ";
	appliance += to_string(this->consumedElectricityForOneHour);
	return appliance;
}
