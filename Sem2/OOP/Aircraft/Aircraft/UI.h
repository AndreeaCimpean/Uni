#pragma once
#include "Service.h"

class UI
{
private:
	Service& service;
public:
	UI(Service& service) : service{ service } {};
	void menu();
	void run();
	void display_aircraft_reaching_altitude(const double altitude);
	void add_helicopter(const std::string& id, const std::string& model, const bool isPrivate);
	void add_plane(const std::string& id, const std::string& model, const bool isPrivate, const std::string& mainWings);
	void add_hot_air_balloon(const std::string& id, const std::string& model, const double weightLimit);
	void display_aircrafts_with_activity(const std::string& activity) const;
};

