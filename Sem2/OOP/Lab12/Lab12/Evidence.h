#pragma once
#include <string>

class Evidence
{
private:
	std::string id;
	std::string measurement;
	double imageClarityLevel;
	double quantity;
	std::string photograph;
public:
	Evidence();
	Evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, double quantity, const std::string& photograph);
	bool operator==(Evidence& evidence);
	std::string get_id() const;
	std::string get_measurement() const;
	std::string get_photograph() const;
	double get_image_clarity_level() const;
	double get_quantity() const;

	void set_measurement(const std::string& measurement);
	void set_photograph(const std::string& photograph);
	void set_image_clarity_level(double imageClarityLevel);
	void set_quantity(double quantity);

	friend std::istream& operator>>(std::istream& istream, Evidence& evidence);
	friend std::ostream& operator<<(std::ostream& ostream, const Evidence& evidence);

	void to_html(std::string html_file);
	std::string toString() const;
};

