#include "UI.h"
#include "House.h"
#include "Block.h"
#include <iostream>

using namespace std;

void UI::print_menu()
{
	cout << endl;
	cout << "1 to add a block\n";
	cout << "2 to add a house\n";
	cout << "3 to show all buildings\n";
	cout << "4 to save buildings\n";
	cout << "x to exit\n";
	cout << endl << endl;
}

void UI::run()
{
	string choice = "";
	while (choice != "x")
	{
		this->print_menu();
		cout << "your choice: ";
		cin >> choice;
		if (choice == "1")
		{
			string address;
			int constructionYear, occupiedApartments,totalApartments;
			cout << "address: ";
			cin.ignore();
			getline(cin, address);
			cout << "construction year: ";
			cin >> constructionYear;
			cout << "total appartments: ";
			cin >> totalApartments;
			cout << "occupied appartments: ";
			cin >> occupiedApartments;
			this->addBlock(address, constructionYear, totalApartments, occupiedApartments);
		}
		else if (choice == "2")
		{
			string address, type, answer;
			bool isHistorical;
			int constructionYear;
			cout << "address: ";
			cin.ignore();
			getline(cin, address);
			cout << "construction year: ";
			cin >> constructionYear;
			cout << "type (one story/two story/duplex): ";
			cin.ignore();
			getline(cin, type);
			cout << "historical? (y/n): ";
			cin >> answer;
			if (answer == "y")
				isHistorical = true;
			else
				isHistorical = false;
			this->addHouse(address, constructionYear, type, isHistorical);
		}
		else if (choice == "3")
		{
			this->showAllbuildings();
		}
		else if (choice == "4")
		{
			string fileRestore, fileDemolish;
			cout << "file for saving buildings to restore: ";
			cin.ignore();
			getline(cin, fileRestore);
			cout << "file for saving buildings to demolish: ";
			getline(cin, fileDemolish);
			this->saveBuildings(fileRestore, fileDemolish);
		}
	}
}

void UI::addBlock(const std::string& addresss, const int constructionYear, const int totalApartments, const int occupiedAppartments)
{
	shared_ptr<Building> building = make_shared<Block>(addresss, constructionYear, totalApartments, occupiedAppartments);
	try
	{
		this->controller.addBuilding(building);
	}
	catch(const char* message)
	{
		cout << message;
	}
}

void UI::addHouse(const std::string& addresss, const int constructionYear, const std::string& type, const bool isHistorical)
{
	shared_ptr<Building> building = make_shared<House>(addresss, constructionYear, type, isHistorical);
	try
	{
		this->controller.addBuilding(building);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

void UI::showAllbuildings() const
{
	vector<shared_ptr<Building>> buildings = this->controller.getAllBuildingsSortedByConstructionYear();
	for (auto building : buildings)
		cout << building->toString() << endl;
}

void UI::saveBuildings(const std::string& fileRestore, const std::string& fileDemolish) const
{
	this->controller.saveBuildings(fileRestore, fileDemolish);
}
