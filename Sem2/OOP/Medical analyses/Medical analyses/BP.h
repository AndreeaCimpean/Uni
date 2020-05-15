#pragma once
#include "MedicalAnalysis.h"

class BP : public MedicalAnalysis
{
private:
	int systolicValue;
	int diastolicValue;
public:
	BP(const std::string& date, const int systolicValue, const int diastolicValue) : MedicalAnalysis{ date }, systolicValue{ systolicValue }, diastolicValue{ diastolicValue } {};
	bool isResultOk() const override;
	std::string toString() const override;
};

