#pragma once
#include "Evidence.h"

class EvidenceValidator
{
public:
	void validate(const Evidence& evidence);
	bool valid_measurement(const Evidence& evidence);
};
