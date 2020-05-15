#pragma once
#include "Aircraft.h"
#include <string>

class Plane : public Aircraft
{
private:
	bool isPrivate;
	std::string mainWings;
public:
	Plane(const std::string& id, const std::string& model, const bool isPrivate, const std::string& mainWings);
	std::string toString() const override;
};

