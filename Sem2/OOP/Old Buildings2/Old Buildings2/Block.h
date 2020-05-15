#pragma once
#include "Building.h"

class Block : public Building
{
private:
	int totalApartments;
	int occupiedApartments;
public:
	Block(const std::string& address, const int constructionYear, const int totalApartments, const int occupiedApartments) : Building{ address, constructionYear }, totalApartments{ totalApartments }, occupiedApartments{ occupiedApartments } {};
	bool mustBeRestored() const override;
	bool canBeDemolished() const override;
	std::string toString() const override;
};

