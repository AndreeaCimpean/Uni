#include "Controller.h"
#include <algorithm>
#include <fstream>

using namespace std;

void Controller::addBuilding(std::shared_ptr<Building> building)
{
	this->repository.addBuilding(building);
}

std::vector<std::shared_ptr<Building>> Controller::getAllBuildings() const
{
	return this->repository.getAllBuildings();
}

std::vector<std::shared_ptr<Building>> Controller::getAllToBeRestored() const
{
	vector<shared_ptr<Building>> buildings = this->getAllBuildings();
	for (int i = 0; i < buildings.size(); ++i)
		if (!buildings[i]->mustBeRestored())
			buildings.erase(buildings.begin() + i);
	return buildings;
}

std::vector<std::shared_ptr<Building>> Controller::getAllToBeDemolished() const
{
	vector<shared_ptr<Building>> buildings = this->getAllBuildings();
	for (int i = 0; i < buildings.size(); ++i)
		if (!buildings[i]->canBeDemolished())
			buildings.erase(buildings.begin() + i);
	return buildings;
}

std::vector<std::shared_ptr<Building>> Controller::getAllBuildingsSortedByConstructionYear() const
{
	vector<shared_ptr<Building>> buildings = this->getAllBuildings();
	sort(buildings.begin(), buildings.end(), [](const shared_ptr<Building>building1, const shared_ptr<Building> building2) {return building1->get_year_of_construction() < building2->get_year_of_construction(); });
	return buildings;
}

void Controller::saveBuildings(const std::string& fileRestore, const std::string& fileDemolish) const
{
	vector<shared_ptr<Building>> buildings_to_restore = this->getAllToBeRestored();
	vector<shared_ptr<Building>> buildings_to_demolish = this->getAllToBeDemolished();
	this->writeToFile(fileRestore, buildings_to_restore);
	this->writeToFile(fileDemolish, buildings_to_demolish);
}

void Controller::writeToFile(const std::string& filename, std::vector<std::shared_ptr<Building>> buildings) const
{
	ofstream file(filename);
	for (auto building : buildings)
		file << building->toString() << endl;
	file.close();
}

