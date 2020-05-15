#include "Block.h"
#include <time.h>

using namespace std;

bool Block::mustBeRestored() const
{
	time_t theTime = time(NULL);
	tm* time = localtime(&theTime);
	int year = time->tm_year;
	if (year - this->constructionYear > 40 && (double)(this->occupiedApartments * 100) / (double)(this->totalApartments) > 80)
		return true;
	return false;
}

bool Block::canBeDemolished() const
{
	if ((double)(this->occupiedApartments * 100) / (double)(this->totalApartments) < 5)
		return true;
	return false;
}

std::string Block::toString() const
{
	string building = Building::toString();
	building += "\tBlock: ";
	building += "total apartments: ";
	building += to_string(this->totalApartments);
	building += " occupied apartments: ";
	building += to_string(this->occupiedApartments);
	return building;
}
