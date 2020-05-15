#include "UI.h"
#include "Block.h"
#include "House.h"
#include <iostream>

using namespace std;

void UI::print_menu() const
{
	cout << endl;
	cout << "1 to add a new building" << endl;
	cout << "2 to show all buildings" << endl;
	cout << "3 to save buildings" << endl;
	cout << "x to exit" << endl;
	cout << endl;
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
			string address, type;
			int constructionYear;
			cout << "address: ";
			cin.ignore();
			getline(cin, address);
			cout << "construction year: ";
			cin >> constructionYear;
			cout << "type(block/house): ";
			cin >> type;
			if (type == "block")
			{
				int totalApartments, occupiedApartments;
				cout << "total apratments: ";
				cin >> totalApartments;
				cout << "occupied apartments: ";
				cin >> occupiedApartments;
				this->addBlock(address, constructionYear, totalApartments, occupiedApartments);
			}
			else
			{
				string houseType, answer;
				bool isHistorical;
				cout << "type: ";
				cin.ignore();
				getline(cin, houseType);
				cout << "historical? (y/n)";
				cin >> answer;
				if (answer == "y")
					isHistorical = true;
				else 
					isHistorical = false;
				this->addHouse(address, constructionYear, houseType, isHistorical);
			}
		}
		else if (choice == "2")
		{
			this->showAllbuildings();
		}
		else if (choice == "3")
		{
			string fileRestored, fileDemolished;
			cout << "file for restored: ";
			cin.ignore();
			getline(cin, fileRestored);
			cout << "file for demolished: ";
			getline(cin, fileDemolished);
			this->saveBuildings(fileRestored, fileDemolished);
		}
	}
}

void UI::showAllbuildings() const
{
	auto buildings = this->controller.getAllBuildings();
	for (auto building : buildings)
		cout << building->toString() << endl;
}

void UI::addBlock(const std::string& address, const int constructionYear, const int totalApartments, const int occupiedApartments)
{
	shared_ptr<Building> block = make_shared<Block>(address, constructionYear, totalApartments, occupiedApartments);
	try
	{
		this->controller.addBuilding(block);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

void UI::addHouse(const std::string& address, const int constructionYear, const std::string& type, const bool isHistorical)
{
	shared_ptr<Building> house = make_shared<House>(address, constructionYear, type, isHistorical);
	try
	{
		this->controller.addBuilding(house);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

void UI::saveBuildings(const std::string& fileRestored, const std::string& fileDemolished) const
{
	auto buildingsRestored = this->controller.getAllToBeRestored();
	auto buildingsDemolished = this->controller.getAllToBeDemolished();
	this->controller.writeToFile(fileRestored, buildingsRestored);
	this->controller.writeToFile(fileDemolished, buildingsDemolished);
}
