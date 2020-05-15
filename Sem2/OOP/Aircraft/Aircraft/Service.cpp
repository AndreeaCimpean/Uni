#include "Service.h"
#include "Helicopter.h"
#include "Plane.h"
#include "HotAirBalloon.h"
#include <memory>
#include <vector>
#include <fstream>

using namespace std;

std::vector<std::shared_ptr<Aircraft>> Service::get_aircraft_reaching_altitude(const double altitude) const
{
	vector<shared_ptr<Aircraft>> aircrafts = this->get_aircrafts();
	for (int i = 0; i < aircrafts.size(); ++i)
		if (aircrafts[i]->get_maximum_altitude() < altitude)
			aircrafts.erase(aircrafts.begin() + i);
	return aircrafts;
}

std::vector<std::shared_ptr<Aircraft>> Service::get_aircrafts() const
{
	return this->repository.get_aircarfts();
}

void Service::add_helicopter(const std::string& id, const std::string& model, const bool isPrivate)
{
	shared_ptr<Aircraft> helicopter = make_shared<Helicopter>(id, model, isPrivate);
	this->repository.add_aircraft(helicopter);
}

void Service::add_plane(const std::string& id, const std::string& model, const bool isPrivate, const std::string& mainWings)
{
	shared_ptr<Aircraft> plane = make_shared<Plane>(id, model, isPrivate, mainWings);
	this->repository.add_aircraft(plane);
}

void Service::add_hot_air_balloon(const std::string& id, const std::string& model, const double weightLimit)
{
	shared_ptr<Aircraft> hotAirBalloon = make_shared<HotAirBalloon>(id, model, weightLimit);
	this->repository.add_aircraft(hotAirBalloon);
}

std::vector<std::shared_ptr<Aircraft>> Service::get_aircrafts_with_activity(const std::string& activity) const
{
	vector<shared_ptr<Aircraft>> aircrafts = this->get_aircrafts();
	vector<shared_ptr<Aircraft>> filteredArircrafts;
	for (int i = 0; i < aircrafts.size(); ++i)
	{
		vector<string> activities = aircrafts[i]->get_activities();
		for (int j = 0; j < activities.size(); ++j)
			if (activities[j] == activity)
				filteredArircrafts.push_back(aircrafts[i]);
	}
	string filename = activity;
	filename += ".txt";
	ofstream output_file(filename);
	for (int i = 0; i < filteredArircrafts.size(); ++i)
		output_file << filteredArircrafts[i]->toString()<<endl;
	output_file.close();
	return filteredArircrafts;
}
