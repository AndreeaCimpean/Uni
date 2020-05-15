#pragma once
#include "tests.h"
#include "Controller.h"
#include "Building.h"
#include "Block.h"
#include "House.h"
#include <memory>
#include <assert.h>

using namespace std;

void test_all()
{
	addBuilding_duplicateAddress_buildingNotAdded();
	addBuilding_block_buildingAdded();
	addBuilding_house_buildingAdded();
	getAllBuildingsSortedByConstructionYear_validInput_getSortedBuildings();
}


void addBuilding_duplicateAddress_buildingNotAdded()
{
	shared_ptr<Building> building = make_shared<Block>("Str. Ana nr. 4", 1999, 60, 45);
	Repository someRepository;
	Controller someController{ someRepository };
	someController.addBuilding(building);
	try
	{
		someController.addBuilding(building);
		assert(false);
	}
	catch (...)
	{
		assert(true);
	}
}

void addBuilding_block_buildingAdded()
{
	shared_ptr<Building> building = make_shared<Block>("Str. Ana nr. 4", 1999, 60, 45);
	Repository someRepository;
	Controller someController{ someRepository };
	someController.addBuilding(building);
	auto buildings = someController.getAllBuildings();
	assert(buildings[0]->get_address() == "Str. Ana nr. 4");
}

void addBuilding_house_buildingAdded()
{
	shared_ptr<Building> building = make_shared<House>("Str. Rina nr. 4", 1999, "duplex", true);
	Repository someRepository;
	Controller someController{ someRepository };
	someController.addBuilding(building);
	auto buildings = someController.getAllBuildings();
	assert(buildings[0]->get_address() == "Str. Rina nr. 4");
}

void getAllBuildingsSortedByConstructionYear_validInput_getSortedBuildings()
{
	shared_ptr<Building> house = make_shared<House>("Str. Rina nr. 4", 1998, "duplex", true);
	shared_ptr<Building> block = make_shared<Block>("Str. Ana nr. 4", 1999, 60, 45);
	Repository someRepository;
	Controller someController{ someRepository };
	someController.addBuilding(house);
	someController.addBuilding(block);
	auto buildingsSorted = someController.getAllBuildingsSortedByConstructionYear();
	assert(buildingsSorted[0]->get_address() == "Str. Rina nr. 4" && buildingsSorted[1]->get_address() == "Str. Ana nr. 4");
}
