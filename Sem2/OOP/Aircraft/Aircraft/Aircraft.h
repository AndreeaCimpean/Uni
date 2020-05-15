#pragma once
#include <string>
#include <vector>

class Aircraft
{
protected:
	std::string id;
	std::string model;
	double maximumAltitude;
	std::vector<std::string> activities;
public:
	double get_maximum_altitude();
	std::string get_id();
	virtual std::string toString() const;
	std::vector<std::string> get_activities() const;
};

