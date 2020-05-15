#pragma once
#include "Aircraft.h"
#include<string>

class HotAirBalloon : public Aircraft
{
private:
	double weightLimit;
public:
	HotAirBalloon(const std::string& id, const std::string& model, const double weightLimit);
	std::string toString() const override;
};

