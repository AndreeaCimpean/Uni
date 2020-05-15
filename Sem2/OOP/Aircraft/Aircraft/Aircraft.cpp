#include "Aircraft.h"

using namespace std;

double Aircraft::get_maximum_altitude()
{
	return this->maximumAltitude;
}

std::string Aircraft::get_id()
{
	return this->id;
}

std::string Aircraft::toString() const
{
	string aircraft = "Aircraft id: ";
	aircraft += this->id;
	aircraft += " model: ";
	aircraft += this->model;
	aircraft += " maximum altitude: ";
	aircraft += to_string(this->maximumAltitude);
	aircraft += " activities: ";
	for (int i = 0; i < this->activities.size() - 1; ++i)
	{
		aircraft += this->activities[i];
		aircraft += ", ";
	}
	aircraft += this->activities[this->activities.size() - 1];
	return aircraft;
}

std::vector<std::string> Aircraft::get_activities() const
{
	return this->activities;
}
