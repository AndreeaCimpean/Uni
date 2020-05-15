#pragma once
#include "Controller.h"


class UI
{
private:
	Controller& controller;
public:
	UI(Controller& controller) : controller{ controller } {};
	void print_menu() const;
	void run();
	void showAllbuildings() const;
	void addBlock(const std::string& address, const int constructionYear, const int totalApartments, const int occupiedApartments);
	void addHouse(const std::string& address, const int constructionYear, const std::string& type, const bool isHistorical);
	void saveBuildings(const std::string& fileRestored, const std::string& fileDemolished) const;
};

