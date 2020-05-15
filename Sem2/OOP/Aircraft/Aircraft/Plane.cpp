#include "Plane.h"

using namespace std;

Plane::Plane(const std::string& id, const std::string& model, const bool isPrivate, const std::string& mainWings)
{
	this->id = id;
	this->model = model;
	this->isPrivate = isPrivate;
	this->maximumAltitude = 12;
	this->mainWings = mainWings;
	vector<string> activities;
	if (this->mainWings == "biplane")
		activities.push_back("leisure time");
	activities.push_back("military");
	activities.push_back("public transportation");
	this->activities = activities;
}

std::string Plane::toString() const
{
	string aircraft = Aircraft::toString();
	aircraft += " Plane: ";
	if (this->isPrivate)
		aircraft += "is private";
	else
		aircraft += "is not private";
	aircraft += " main wings: ";
	aircraft += this->mainWings;
	return aircraft;
}
