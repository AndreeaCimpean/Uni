#include "HotAirBalloon.h"

using namespace std;

HotAirBalloon::HotAirBalloon(const std::string& id, const std::string& model, const double weightLimit)
{
	this->id = id;
	this->model = model;
	this->maximumAltitude = 21;
	this->weightLimit = weightLimit;
	vector<string> activities;
	activities.push_back("leisure time");
	this->activities = activities;
}

std::string HotAirBalloon::toString() const
{
	string aircraft = Aircraft::toString();
	aircraft += " Hot air balloon: ";
	aircraft += "weight limit: ";
	aircraft += to_string(this->weightLimit);
	return aircraft;
}
