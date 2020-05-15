#pragma once
#include <string>

class MedicalAnalysis
{
protected:
	std::string date;
public:
	MedicalAnalysis(const std::string& date) : date{ date } {};
	virtual bool isResultOk() const = 0;
	virtual std::string toString() const;
	std::string get_date();
};

