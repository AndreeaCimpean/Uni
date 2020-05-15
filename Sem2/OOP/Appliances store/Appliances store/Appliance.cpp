#include "Appliance.h"

using namespace std;

std::string Appliance::toString()
{
	string appliance = "";
	appliance += this->id;
	appliance += ", ";
	appliance += to_string(weight);
	return appliance;
}
