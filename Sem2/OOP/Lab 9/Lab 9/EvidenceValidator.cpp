#include "EvidenceValidator.h"
#include "MyExceptions.h"
#include <string>

using namespace std;

void EvidenceValidator::validate(const Evidence& evidence)
{
	string errors;
	if (!valid_measurement(evidence))
		errors += string("Invalid measurement!\n");
	if (evidence.get_quantity() <= 0)
		errors += string("Invalid quntity!\n");
	if (evidence.get_image_clarity_level() <= 0)
		errors += string("Invalid image clarity level!\n");
	if (errors.size() > 0)
		throw ValidationException(errors);
}

bool EvidenceValidator::valid_measurement(const Evidence& evidence)
{
	/*
	Check if a given measurement has the correct format
	return: false if
				- the measurement does not have the form: ...X...X..., where ... is a natural number
				- one measurement is 0
			true otherwise
	*/
	string measurement = evidence.get_measurement();
	int count_x = count(measurement.begin(), measurement.end(), 'X');
	if (count_x != 2)
		return false;
	if (!isdigit(measurement[0]))
		return false;
	string previous_character = "";
	for (auto character : measurement)
	{
		if (!isdigit(character) && previous_character != "")
		{
			if (character != 'X' || (character == 'X' && !isdigit(previous_character[0])))
				return false;
		}
		else if (character == '0' && previous_character == "X")
			return false;
		previous_character = character;
	}
	return true;
}


