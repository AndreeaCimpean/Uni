#pragma once
#include <string>
#include "Appliance.h"

class Refrigerator : public Appliance
{
private:
	std::string electricityUsageClass;
	bool hasFreezer;
public:
	Refrigerator(const std::string& id, const double weight, const std::string& electricityUsageClass,
		const bool hasFreezer) : Appliance{ id, weight }, electricityUsageClass{ electricityUsageClass }, hasFreezer{ hasFreezer } {};
	double consumedElectricity() override;
	std::string toString() override;
	std::string get_electricity_usage_class();

};

