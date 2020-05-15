#pragma once
#include "Building.h"
#include <memory>
#include <vector>

class Repository
{
private:
	std::vector<std::shared_ptr<Building>> buildings;
public:
	Repository() {};
	bool findBuildingByAddress(const std::string& address) const;
	std::vector<std::shared_ptr<Building>> getAllBuildings() const;
	void addBuilding(std::shared_ptr<Building> building);
};

