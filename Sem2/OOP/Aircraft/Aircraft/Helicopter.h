#pragma once
#include "Aircraft.h"

class Helicopter : public Aircraft
{
private:
	bool isPrivate;
public:
	Helicopter(const std::string& id, const std::string& model, const bool isPrivate);
	std::string toString() const override;
};

