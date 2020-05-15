#include "House.h"
#include <time.h>

using namespace std;

bool House::mustBeRestored() const
{
	time_t theTime = time(NULL);
	tm* time = localtime(&theTime);
	int year = time->tm_year;
	if (year - this->constructionYear > 100)
		return true;
	return false;
}

bool House::canBeDemolished() const
{
	if (!this->isHistorical)
		return true;
	return false;
}

std::string House::toString() const
{
	string building = Building::toString();
	building += "\tHouse: ";
	building += "type: ";
	building += this->type;
	building += " historical: ";
	if (this->isHistorical)
		building += "yes";
	else
		building += "no";
	return building;
}
