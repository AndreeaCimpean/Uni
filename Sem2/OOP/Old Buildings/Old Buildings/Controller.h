#pragma once
#include "Repository.h"
#include "Building.h"

class Controller
{
private:
	Repository& repository;
public:
	Controller(Repository& repository) : repository{ repository } {};
	void addBuilding(std::shared_ptr<Building> building);
	std::vector<std::shared_ptr<Building>> getAllBuildings() const;
	std::vector<std::shared_ptr<Building>> getAllToBeRestored() const;
	std::vector<std::shared_ptr<Building>> getAllToBeDemolished() const;
	std::vector<std::shared_ptr<Building>> getAllBuildingsSortedByConstructionYear() const;
	void saveBuildings(const std::string& fileRestore, const std::string& fileDemolish) const;
	void writeToFile(const std::string& filename, std::vector<std::shared_ptr<Building>> buildings) const;
};

