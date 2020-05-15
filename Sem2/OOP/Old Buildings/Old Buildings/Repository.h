#pragma once
#include "Building.h"
#include <vector>
#include <memory>

class Repository
{
private:
	std::vector<std::shared_ptr<Building>> buildings;
public:
	void addBuilding(std::shared_ptr<Building> building);
	bool findBuildingByAddress(const std::string& address);
	std::vector<std::shared_ptr<Building>> getAllBuildings() const;
};

