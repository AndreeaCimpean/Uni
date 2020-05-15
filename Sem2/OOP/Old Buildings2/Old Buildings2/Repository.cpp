#include "Repository.h"

using namespace std;

bool Repository::findBuildingByAddress(const std::string& address) const
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

void Repository::addBuilding(std::shared_ptr<Building> building)
{
	if (this->findBuildingByAddress(building->get_address()))
		throw "Duplicate address!";
	else
		this->buildings.push_back(building);
}
