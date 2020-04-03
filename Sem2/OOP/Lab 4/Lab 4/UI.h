#pragma once
#include "Service.h"

class UI
{
private:
	Service service;
public:
	UI(const Service& service) : service{service} {}
	void run();
	void check_measurement(const std::string& measurement) const;
	void check_image_clarity_level(const std::string& imageClarityLevel) const;
	void check_quantity(const std::string& quantity) const;
	void add_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph);
	void read_evidence(std::string& id, std::string& measurement, std::string& imageClarityLevel, std::string& quantity, std::string& photograph) const;
	void update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph);
	void delete_evidence(const std::string& id);
	void list_evidences() const;
};

