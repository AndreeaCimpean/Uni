#include "Controller.h"
#include <algorithm>
#include <fstream>
using namespace std;

std::vector<std::shared_ptr<Building>> Controller::getAllBuildings() const
{
	auto buildings = this->repository.getAllBuildings();
	sort(buildings.begin(), buildings.end(), [](shared_ptr<Building> building1, shared_ptr<Building> building2) {return building1->get_construction_year() < building2->get_construction_year(); });
	return buildings;
}

void Controller::addBuilding(std::shared_ptr<Building> building)
{
	this->repository.addBuilding(building);
}

std::vector<std::shared_ptr<Building>> Controller::getAllToBeDemolished() const
{
	auto buildings = this->repository.getAllBuildings();
	std::vector<std::shared_ptr<Building>> filteredBuildings;
	for (auto building : buildings)
		if (building->canBeDemolished())
			filteredBuildings.push_back(building);
	return filteredBuildings;
}

std::vector<std::shared_ptr<Building>> Controller::getAllToBeRestored() const
{
	auto buildings = this->repository.getAllBuildings();
	std::vector<std::shared_ptr<Building>> filteredBuildings;
	for (auto building : buildings)
		if (building->mustBeRestored())
			filteredBuildings.push_back(building);
	return filteredBuildings;
}

void Controller::writeToFile(const std::string& filename, std::vector<std::shared_ptr<Building>> buildings) const
{
	ofstream file(filename);
	for (auto building : buildings)
		file << building->toString() << endl;
	file.close();
}



