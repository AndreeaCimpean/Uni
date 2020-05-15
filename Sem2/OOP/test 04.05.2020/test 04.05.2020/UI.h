#pragma once
#include "Service.h"

class UI
{
private:
	Service& service;
public:
	UI(Service& service) : service{ service } {};
	void run();
	void add_neonatal_unit(const std::string& hospitalName, const int numberOfDoctors, const int numberOfMothers, const int numberOfNewborns, const double averageGrade);
	void add_surgery(const std::string& hospitalName, const int numberOfDoctors, const int numberOfPatients);
	void list_departments() const;
	void list_efficent();
};

