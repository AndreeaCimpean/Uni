#pragma once
#include "Controller.h"

class Service
{
private:
	Controller& controller;
public:
	Service(Controller& controller) : controller{ controller } {};
	std::vector<std::shared_ptr<Appliance>> get_all_appliances();
	void add_refrigerator(const std::string& id, const double weight, const std::string& electricityUsageClass, const bool hasFreezer);
	void add_dish_washer(const std::string& id, const double weight, const double washingCycleLength, const double consumedElectricityForOneHour);
};

