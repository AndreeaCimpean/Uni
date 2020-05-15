#include "UI.h"
#include <iostream>
#include <string>

using namespace std;

void UI::menu()
{
	cout << endl;
	cout << "1 to add an helicopter\n";
	cout << "2 to add a plane\n";
	cout << "3 to add an hot air balloon\n";
	cout << "4 to show aircrafts for an activity\n";
	cout << "5 show all aircrafts that can reach ar least a given altitude\n";
	cout << "x to exit\n";
	cout << endl;
}

void UI::run()
{
	string command = "";
	while (command != "x")
	{
		this->menu();
		cout << "your choice: ";
		cin >> command;
		if (command == "1")
		{
			string id, model, answer;
			bool isPrivate;
			cout << "id: ";
			cin >> id;
			cout << "model: ";
			cin >> model;
			cout << "is private? (y/n): ";
			cin >> answer;
			if (answer == "y")
				isPrivate = true;
			else
				isPrivate = false;
			this->add_helicopter(id, model, isPrivate);
		}
		else if (command == "2")
		{
			string id, model, answer, mainWings;
			bool isPrivate;
			cout << "id: ";
			cin >> id;
			cout << "model: ";
			cin >> model;
			cout << "is private? (y/n): ";
			cin >> answer;
			if (answer == "y")
				isPrivate = true;
			else
				isPrivate = false;
			cout << "main wings (monoplane/biplane): ";
			cin >> mainWings;
			this->add_plane(id, model, isPrivate, mainWings);
		}
		else if (command == "3")
		{
			string id, model;
			double weightLimit;
			cout << "id: ";
			cin >> id;
			cout << "model: ";
			cin >> model;
			cout << "weight limit: ";
			cin >> weightLimit;
			this->add_hot_air_balloon(id, model, weightLimit);
		}
		else if (command == "4")
		{
			string activity;
			cout << "activity: ";
			cin.ignore();
			getline(cin, activity);
			this->display_aircrafts_with_activity(activity);
		}
		else if (command == "5")
		{
			string altitude;
			cout << "altitude: ";
			cin >> altitude;
			this->display_aircraft_reaching_altitude(stod(altitude));
		}
	}
}

void UI::display_aircraft_reaching_altitude(const double altitude)
{
	auto aircrafts = this->service.get_aircraft_reaching_altitude(altitude);
	for (auto aircraft : aircrafts)
		cout << aircraft->toString() << endl;
}

void UI::add_helicopter(const std::string& id, const std::string& model, const bool isPrivate)
{
	try
	{
		this->service.add_helicopter(id, model, isPrivate);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

void UI::add_plane(const std::string& id, const std::string& model, const bool isPrivate, const std::string& mainWings)
{
	try
	{
		this->service.add_plane(id, model, isPrivate, mainWings);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

void UI::add_hot_air_balloon(const std::string& id, const std::string& model, const double weightLimit)
{
	try
	{
		this->service.add_hot_air_balloon(id, model, weightLimit);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

void UI::display_aircrafts_with_activity(const std::string& activity) const
{
	auto aircrafts = this->service.get_aircrafts_with_activity(activity);
	for (auto aircraft : aircrafts)
		cout << aircraft->toString() << endl;
}

