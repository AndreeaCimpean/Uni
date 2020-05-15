#include "House.h"
#include <time.h>

using namespace std;

bool House::mustBeRestored() const
{
	time_t theTime = time(NULL);
	tm* now = localtime(&theTime);
	int year = now->tm_year + 1900;
	return (year - this->constructionYear > 100 );
}

bool House::canBeDemolished() const
{
	return (!this->isHistorical);
}

std::string House::toString() const
{
	string building = Building::toString();
	building += " type: House ";
	building += "type of house: ";
	building += this->type;
	building += " historical: ";
	if (isHistorical)
		building += "yes";
	else building += "no";
	return building;
}
