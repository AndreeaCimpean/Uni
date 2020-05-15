#pragma once
#include "Controller.h"

class UI
{
private:
	Controller& controller;
public:
	UI(Controller& controller) : controller{ controller } {};
	void print_menu();
	void run();
	void addBlock(const std::string& addresss, const int constructionYear, const int totalApartments, const int occupiedAppartments);
	void addHouse(const std::string& addresss, const int constructionYear, const std::string& type, const bool isHistorical);
	void showAllbuildings() const;
	void saveBuildings(const std::string& fileRestore, const std::string& fileDemolish) const;
};

