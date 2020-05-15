#pragma once
#include "Building.h"


class House : public Building
{
private:
	std::string type;
	bool isHistorical;
public:
	House(const std::string& address, const int constructionYear, const std::string& type, const bool isHistorical) : Building{ address, constructionYear }, type{ type }, isHistorical{ isHistorical } {};
	bool mustBeRestored() const override;
	bool canBeDemolished() const override;
	std::string toString() const override;
};

