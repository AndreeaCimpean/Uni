#pragma once
#include "Appliance.h"

class DishWasher : public Appliance
{
private:
	double washingCycleLength;
	double consumedElectricityForOneHour;
public:
	DishWasher(const std::string& id, const double weight, const double washingCycleLength,
		const double consumedElectricityForOneHour) : Appliance{ id, weight }, washingCycleLength{ washingCycleLength }, consumedElectricityForOneHour{ consumedElectricityForOneHour } { };
	double consumedElectricity() override;
	std::string toString() override;
};

