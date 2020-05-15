#pragma once
#include "Repository.h"

class Service
{
private:
	Repository& repository;
public:
	Service(Repository& repository) : repository{ repository } {};
	std::vector<std::shared_ptr<Aircraft>> get_aircraft_reaching_altitude(const double altitude) const;
	std::vector<std::shared_ptr<Aircraft>> get_aircrafts() const;
	void add_helicopter(const std::string& id, const std::string& model, const bool isPrivate);
	void add_plane(const std::string& id, const std::string& model, const bool isPrivate, const std::string& mainWings);
	void add_hot_air_balloon(const std::string& id, const std::string& model, const double weightLimit);
	std::vector<std::shared_ptr<Aircraft>> get_aircrafts_with_activity(const std::string& activity) const;
};