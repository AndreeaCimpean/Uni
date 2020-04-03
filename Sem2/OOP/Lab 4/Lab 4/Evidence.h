#pragma once
#include <iostream>
class Evidence
{
private:
	std::string id;
	std::string measurement;
	double imageClarityLevel;
	int quantity;
	std::string photograph;
public:
	Evidence();
	Evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, int quantity, const std::string& photograph);
	bool operator==(Evidence& evidence);
	std::string get_id() const;
	std::string get_measurement() const;
	std::string get_photograph() const;
	double get_image_clarity_level() const;
	int get_quantity() const;

	void set_id(const std::string& id);
	void set_measurement(const std::string& measurement);
	void set_photograph(const std::string& photograph);
	void set_image_clarity_level(double imageClarityLevel);
	void set_quantity(int quantity);
};

