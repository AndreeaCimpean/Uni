#include "Evidence.h"

Evidence::Evidence() : id(""), measurement(""), imageClarityLevel(0.0), quantity(0), photograph("")
{
}

Evidence::Evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, int quantity, const std::string& photograph) : id{id}, measurement{measurement}, quantity{quantity}, imageClarityLevel{imageClarityLevel}, photograph{ photograph }
{
}

bool Evidence::operator==(Evidence& evidence)
{
	if (this->id == evidence.id && this->measurement == evidence.measurement && this->imageClarityLevel == evidence.imageClarityLevel && this->quantity == evidence.quantity && this->photograph == evidence.photograph)
		return true;
	return false;
}

std::string Evidence::get_id() const
{
	return this->id;
}

std::string Evidence::get_measurement() const
{
	return this->measurement;
}

std::string Evidence::get_photograph() const
{
	return this->photograph;
}

double Evidence::get_image_clarity_level() const
{
	return this->imageClarityLevel;
}

int Evidence::get_quantity() const
{
	return this->quantity;
}

void Evidence::set_id(const std::string& id)
{
	this->id = id;
}

void Evidence::set_measurement(const std::string& measurement)
{
	this->measurement = measurement;
}

void Evidence::set_photograph(const std::string& photograph)
{
	this->photograph = photograph;
}

void Evidence::set_image_clarity_level(double imageClarityLevel)
{
	this->imageClarityLevel = imageClarityLevel;
}

void Evidence::set_quantity(int quantity)
{
	this->quantity = quantity;
}
