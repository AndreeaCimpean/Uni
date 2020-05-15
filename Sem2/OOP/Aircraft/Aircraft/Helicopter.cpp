#include "Helicopter.h"

using namespace std;

Helicopter::Helicopter(const std::string& id, const std::string& model, const bool isPrivate)
{
	this->id = id;
	this->model = model;
	this->isPrivate = isPrivate;
	vector <string> activities;
	if (this->isPrivate == true)
		activities.push_back("leisure time");
	activities.push_back("military");
	activities.push_back("medical emergencies");
	activities.push_back("public transformation");
	this->activities = activities;
	this->maximumAltitude = 12;
}

std::string Helicopter::toString() const
{
	string aircraft = Aircraft::toString();
	aircraft += " Helicopter: ";
	if (this->isPrivate)
		aircraft += "is private";
	else
		aircraft += "is not private";
	return aircraft;
}
