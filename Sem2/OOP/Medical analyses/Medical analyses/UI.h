#pragma once
#include "Service.h"

class UI
{
private:
	Service& service;
public:
	UI(Service& service) : service{ service } {};
	void print_menu();
	void run();
	void addBMI(const std::string& date, const double value);
	void addBP(const std::string& date, const int systolicValue, const int diatolicValue);
	void showAllAnalyses() const;
	void isIll() const;
	void saveToFile(const std::string& file, const std::string& date1, const std::string& date2) const;
};

