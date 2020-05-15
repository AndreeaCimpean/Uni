#pragma once
#include "Repository.h"


class Controller
{
private:
	Repository& repository;
public:
	Controller(Repository& repository) : repository{ repository } { };
	std::vector<std::shared_ptr<Building>> getAllBuildings() const;
	void addBuilding(std::shared_ptr<Building> building);
	std::vector<std::shared_ptr<Building>> getAllToBeDemolished() const;
	std::vector<std::shared_ptr<Building>> getAllToBeRestored() const;
	void writeToFile(const std::string& filename, std::vector<std::shared_ptr<Building>> buildings) const;
};

