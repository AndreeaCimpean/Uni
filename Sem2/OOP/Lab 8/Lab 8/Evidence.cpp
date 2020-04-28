#include "Evidence.h"
#include "Validations.h"
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

vector<string> tokenize(const string& line_read, char delimiter)
{
	/*
	Split a line read into parameters
	parameters: line_read - the line read from a stream
				delimiter - the character that delimits the parameters
	Return the parameters
	*/
	vector <string> parameters_read;
	stringstream stream(line_read);
	string token;
	while (getline(stream, token, delimiter))
		parameters_read.push_back(token);
	return parameters_read;
}

Evidence::Evidence() : id(""), measurement(""), imageClarityLevel(0.0), quantity(0.0), photograph("")
{
}

Evidence::Evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, double quantity, const std::string& photograph) : id{id}, measurement{measurement}, quantity{quantity}, imageClarityLevel{imageClarityLevel}, photograph{ photograph }
{
}

bool Evidence::operator==(Evidence& evidence)
{
	/*
	Check if two evidences are equal
	*/
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

double Evidence::get_quantity() const
{
	return this->quantity;
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

void Evidence::set_quantity(double quantity)
{
	this->quantity = quantity;
}

std::istream& operator>>(std::istream& istream, Evidence& evidence)
{
	/*
	Extraction operator to read an evidence
	*/
	string line_read;
	getline(istream, line_read);
	if(line_read != "")
		line_read.erase(remove(line_read.begin(), line_read.end(), ' '), line_read.end());
	vector<string> parameters_read = tokenize(line_read, ',');
	if (parameters_read.size() != 5)
		return istream;
	string id = parameters_read[0];
	string measurement = parameters_read[1];
	string imageClarityLevel = parameters_read[2];
	string quantity = parameters_read[3];
	string photograph = parameters_read[4];
	check_measurement(measurement);
	check_image_clarity_level(imageClarityLevel);
	check_quantity(quantity);
	evidence.id = id;
	evidence.measurement = measurement;
	evidence.imageClarityLevel = stod(imageClarityLevel);
	evidence.quantity = stod(quantity);
	evidence.photograph = photograph;
	return istream;
}

std::ostream& operator<<(std::ostream& ostream, const Evidence& evidence)
{
	/*
	Insertion operator to write an evidence
	*/
	ostream << evidence.id << ", " << evidence.measurement << ", " << evidence.imageClarityLevel << ", " << evidence.quantity << ", " << evidence.photograph;
	return ostream;
}






