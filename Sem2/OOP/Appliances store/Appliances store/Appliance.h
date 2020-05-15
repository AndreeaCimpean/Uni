#pragma once
#include <string>

class Appliance
{
protected:
	std::string id;
	double weight;
public:
	Appliance(const std::string& id, const double weight) : id{ id }, weight{ weight } {};
	virtual double consumedElectricity() = 0;
	virtual std::string toString();
	std::string get_id() const { return this->id; };
	double get_weight() const { return this->weight; };
};

