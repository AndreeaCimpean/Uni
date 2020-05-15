#include "Repository.h"
#include <exception>

using namespace std;

void Repository::addBuilding(std::shared_ptr<Building> building)
{
	if (this->findBuildingByAddress(building->get_address()))
		throw "Address already exists!";
	else
		this->buildings.push_back(building);
}

bool Repository::findBuildingByAddress(const std::string& address)
{
	for (auto building : this->buildings)
		if (building->get_address() == address)
			return true;
	return false;
}

std::vector<std::shared_ptr<Building>> Repository::getAllBuildings() const
{
	return this->buildings;
}
