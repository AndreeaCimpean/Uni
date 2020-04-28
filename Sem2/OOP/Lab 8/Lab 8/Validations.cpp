#include "Validations.h"
#include <vector>
#include <string>
#include <sstream>

using namespace std;

void check_measurement(const std::string& measurement)
{
	/*
	Check if a given measurement has the correct format
	Throw an exception if:
		- the measurement does not have the form: ...X...X..., where ... is a natural number
		- one measurement is 0
	*/
	int count_x = count(measurement.begin(), measurement.end(), 'X');
	if (count_x != 2)
		throw "Invalid measurement!";
	if (!isdigit(measurement[0]))
		throw "Invalid measurement!";
	string previous_character = "";
	for (auto character : measurement)
	{
		if (!isdigit(character) && previous_character != "")
		{
			if (character != 'X' || (character == 'X' && !isdigit(previous_character[0])))
				throw "Invalid measurement!";
		}
		else if (character == '0' && previous_character == "X")
			throw "Invalid measurement!";
		previous_character = character;
	}
}

void check_image_clarity_level(const std::string& imageClarityLevel)
{
	/*
	Check if an image clarity level is a double
	Throw an exception if it is not
	*/
	int count_dots = count(imageClarityLevel.begin(), imageClarityLevel.end(), '.');
	if (count_dots != 0 && count_dots != 1)
		throw "Invalid image clarity level!";
	for (auto character : imageClarityLevel)
		if (!isdigit(character) && character != '.')
			throw "Invalid image clarity level!";
}

void check_quantity(const std::string& quantity)
{
	/*
	Check if a quantity is a double
	Throw an exception if it is not
	*/
	int count_dots = count(quantity.begin(), quantity.end(), '.');
	if (count_dots != 0 && count_dots != 1)
		throw "Invalid quantity!";
	for (auto character : quantity)
		if (!isdigit(character) && character != '.')
			throw "Invalid image clarity level!";
}

