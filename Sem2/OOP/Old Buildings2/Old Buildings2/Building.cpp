#include "Building.h"

using namespace std;

std::string Building::toString() const
{
	string building="";
	building += "address: ";
	building += this->address;
	building += " year of construction: ";
	building += to_string(this->constructionYear);
	return building;
}

std::string Building::get_address() const
{
	return this->address;
}

int Building::get_construction_year() const
{
	return this->constructionYear;
}
