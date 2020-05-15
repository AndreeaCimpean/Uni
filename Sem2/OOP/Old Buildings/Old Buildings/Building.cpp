#include "Building.h"

using namespace std;

std::string Building::get_address() const
{
	return this->address;
}

int Building::get_year_of_construction() const
{
	return this->constructionYear;
}

std::string Building::toString() const
{
	string building = "";
	building += "Building ";
	building += "address: ";
	building += this->address;
	building += " year of construction: ";
	building += to_string(this->constructionYear);
	building += "\n";
	return building;
}
