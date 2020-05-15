#pragma once
# include "Appliance.h"
#include <vector>
#include <string>
#include <memory>
class Controller
{
private:
	std::vector<std::shared_ptr<Appliance>> appliances;
public:
	bool find_appliance_by_id(std::string id);
	void add_appliance(std::shared_ptr<Appliance> appliance);
	std::vector<std::shared_ptr<Appliance>> get_all_appliances() const;
	//std::vector<std::shared_ptr<Appliance>> get_all_with_consumed_electricity_less_than(double maxElectricity);
	//void writeToFile(std::string fileName);

};

