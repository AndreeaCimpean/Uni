#pragma once
#include "Service.h"

class UI
{
private:
	Service& service;
public:
	UI(Service& service) : service{ service } {};
	void menu();
	void run();
	void add_refrigerator(const std::string& id, const double weight, const std::string& electricityUsageClass, const bool hasFreezer);
	void add_dish_washer(const std::string& id, const double weight, const double washingCycleLength, const double consumedElectricityForOneHour);
	void list_appliances();
};

