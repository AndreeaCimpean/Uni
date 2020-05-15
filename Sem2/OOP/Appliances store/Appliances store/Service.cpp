#include "Service.h"
#include "Refrigerator.h"
#include "DishWasher.h"

using namespace std;

std::vector<std::shared_ptr<Appliance>> Service::get_all_appliances()
{
	return this->controller.get_all_appliances();
}

void Service::add_refrigerator(const std::string& id, const double weight, const std::string& electricityUsageClass, const bool hasFreezer)
{
	shared_ptr<Appliance> refrigerator = make_shared<Refrigerator>(id, weight, electricityUsageClass, hasFreezer);
	this->controller.add_appliance(refrigerator);
}

void Service::add_dish_washer(const std::string& id, const double weight, const double washingCycleLength, const double consumedElectricityForOneHour)
{
	shared_ptr<Appliance> dishWasher = make_shared<DishWasher>(id, weight, washingCycleLength, consumedElectricityForOneHour);
	this->controller.add_appliance(dishWasher);
}
