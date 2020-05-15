#pragma once
#include <string>

class Building
{
protected:
	std::string address;
	int constructionYear;
public:
	Building(const std::string& address, const int constructionYear) : address{ address }, constructionYear{ constructionYear }{};
	virtual bool mustBeRestored() const = 0;
	virtual bool canBeDemolished() const = 0;
	virtual std::string toString() const;
	std::string get_address() const;
	int get_construction_year() const;
};

