#include "Repository.h"

using namespace std;

std::vector<std::shared_ptr<Aircraft>> Repository::get_aircarfts()
{
	return this->aircrafts;
}

bool Repository::find_aircraft_by_id(const std::string& id) const
{
	for (auto aircraft : this->aircrafts)
		if (aircraft->get_id() == id)
			return true;
	return false;
}

void Repository::add_aircraft(std::shared_ptr<Aircraft> aircraft)
{
	if (this->find_aircraft_by_id(aircraft->get_id()))
		throw "Invalid id!\n";
	this->aircrafts.push_back(aircraft);
}
