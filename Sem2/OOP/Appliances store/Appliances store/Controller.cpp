#include "Controller.h"
#include <exception>
#include <algorithm>
#include <vector>

using namespace std;

bool Controller::find_appliance_by_id(std::string id)
{
	for (int i = 0; i < this->appliances.size(); ++i)
		if (this->appliances[i]->get_id() == id)
			return true;
	return false;
}

void Controller::add_appliance(std::shared_ptr<Appliance> appliance)
{
	if (this->find_appliance_by_id(appliance->get_id()))
		throw "Appliance already exists!\n";
	else
		this->appliances.push_back(appliance);
}

std::vector<std::shared_ptr<Appliance>> Controller::get_all_appliances() const
{
	vector<shared_ptr<Appliance>> appliances= this->appliances;
	sort(appliances.begin(), appliances.end(), [](shared_ptr<Appliance> a, shared_ptr<Appliance> b) { return a->get_weight() > b->get_weight();  });
	return appliances;
}
/*
std::vector<std::shared_ptr<Appliance>> Controller::get_all_with_consumed_electricity_less_than(double maxElectricity)
{
}

void Controller::writeToFile(std::string fileName)
{
}
*/