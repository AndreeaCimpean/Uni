#include "UI.h"
#include <iostream>

using namespace std;

void UI::menu()
{
	cout << endl;
	cout << "1 to add a new refrigerator\n";
	cout << "2 to add a new dish washer\n";
	cout << "3 to show all the appliances\n";
	cout << "4 to save in a file appliances\n";
	cout << "x to exit\n";
	cout << endl;
}

void UI::run()
{
	string choice = "";
	while (choice != "x")
	{
		this->menu();
		cout << "your choice: ";
		cin >> choice;
		if (choice == "1")
		{
			string id;
			double weight;
			string electricityUsageClass;
			bool hasFreezer;
			cout << "id: ";
			cin >> id;
			cout << "weight: ";
			cin >> weight;
			cout << "electricity usage class (A/A+/A++): ";
			cin >> electricityUsageClass;
			cout << "has freezer? (y/n): ";
			string answer;
			cin >> answer;
			if (answer == "y")
				hasFreezer = true;
			else hasFreezer = false;
			this->add_refrigerator(id, weight, electricityUsageClass, hasFreezer);
		}
		else if (choice == "2")
		{
			string id;
			double weight, washingCycleLength, consumedElectricityForOneHour;
			cout << "id: ";
			cin >> id;
			cout << "weight: ";
			cin >> weight;
			cout << "washing cycle length: ";
			cin >> washingCycleLength;
			cout << "consumed electricity for one hour: ";
			cin >> consumedElectricityForOneHour;
			this->add_dish_washer(id, weight, washingCycleLength, consumedElectricityForOneHour);
		}
		else if (choice == "3")
		{
			this->list_appliances();
		}
	}
}

void UI::add_refrigerator(const std::string& id, const double weight, const std::string& electricityUsageClass, const bool hasFreezer)
{
	try
	{
		this->service.add_refrigerator(id, weight, electricityUsageClass, hasFreezer);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

void UI::add_dish_washer(const std::string& id, const double weight, const double washingCycleLength, const double consumedElectricityForOneHour)
{
	try
	{
		this->service.add_dish_washer(id, weight, washingCycleLength, consumedElectricityForOneHour);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

void UI::list_appliances()
{
	vector<shared_ptr<Appliance>> appliances = this->service.get_all_appliances();
	for (int i = 0; i < appliances.size(); ++i)
	{
		cout << appliances[i]->toString() << endl;
	}
}
