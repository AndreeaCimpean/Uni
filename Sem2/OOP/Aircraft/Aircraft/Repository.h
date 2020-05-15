#pragma once
#include "Aircraft.h"
#include <vector>
#include <memory>

class Repository
{
private:
	std::vector<std::shared_ptr<Aircraft>> aircrafts;
public:
	std::vector<std::shared_ptr<Aircraft>> get_aircarfts();
	bool find_aircraft_by_id(const std::string& id) const;
	void add_aircraft(std::shared_ptr<Aircraft> aircraft);
};

