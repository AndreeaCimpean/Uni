#pragma once
#include "Service.h"
class UI
{
private:
	Service& service;
public:
	UI(Service& service) : service{ service } {};
	void run();
	void list_analyses() const;
	void add_bp(const std::string& date, const int systolicValue, const int diastolicValue);
	void add_bmi(const std::string& date, const double value);
	void is_ill(const int month) const;
};

