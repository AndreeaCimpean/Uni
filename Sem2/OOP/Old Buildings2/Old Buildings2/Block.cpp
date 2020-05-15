#include "Block.h"
#include <time.h>

using namespace std;

bool Block::mustBeRestored() const
{
	time_t theTime = time(NULL);
	tm* now = localtime(&theTime);
	int year = now->tm_year + 1900;
	return (year - this->constructionYear > 40 && (double)(this->occupiedApartments * 100) / (double)(this->totalApartments) > 80);
}

bool Block::canBeDemolished() const
{
	return (double)(this->occupiedApartments * 100) / (double)(this->totalApartments) < 5;
}

std::string Block::toString() const
{
	string building = Building::toString();
	building += " type: Block ";
	building += "total apartments: ";
	building += to_string(this->totalApartments);
	building += " occupied apartments: ";
	building += to_string(this->occupiedApartments);
	return building;
}
