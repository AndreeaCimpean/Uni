#include "UI.h"
#include "MedicalAnalysis.h"
#include "BMI.h"
#include "BP.h"
#include<iostream>

using namespace std;

void UI::print_menu()
{
	cout << endl;
	cout << "1 for adding a new analysis" << endl;
	cout << "2 to show all analyses" <<endl;
	cout << "3 to show if ill person" << endl;
	cout << "4 to save analyses" << endl;
	cout << "x to exit" << endl;
	cout << endl;
}

void UI::run()
{
	string choice = "";
	while (choice != "x")
	{
		this->print_menu();
		cout << "your choice: ";
		cin >> choice;
		if (choice == "1")
		{
			string type, date;
			cout << "type (BP/BMI): ";
			cin >> type;
			cout<<"date: ";
			cin >> date;
			if (type == "BMI")
			{
				double value;
				cout << "value: ";
				cin >> value;
				this->addBMI(date, value);
			}
			else
			{
				int systolicValue, diatolicValue;
				cout << "systolicValue: ";
				cin >> systolicValue;
				cout << "diatolic value: ";
				cin >> diatolicValue;
				this->addBP(date, systolicValue, diatolicValue);
			}
		}
		else if (choice == "2")
		{
			this->showAllAnalyses();
		}
		else if (choice == "3")
		{
			this->isIll();
		}
		else if (choice == "4")
		{
			string file, date1, date2;
			cout << "file: ";
			cin >> file;
			cout << "date1: ";
			cin >> date1;
			cout << "date2: ";
			cin >> date2;
			this->saveToFile(file, date1, date2);
		}
	}
}

void UI::addBMI(const std::string& date, const double value)
{
	shared_ptr<MedicalAnalysis> analysis = make_shared<BMI>(date, value);
	this->service.addAnalysis(analysis);
}

void UI::addBP(const std::string& date, const int systolicValue, const int diatolicValue)
{
	shared_ptr<MedicalAnalysis> analysis = make_shared<BP>(date, systolicValue, diatolicValue);
	this->service.addAnalysis(analysis);
}

void UI::showAllAnalyses() const
{
	auto analyses = this->service.getAllAnalyses();
	for (auto analysis : analyses)
		cout << analysis->toString() << endl;
}

void UI::saveToFile(const std::string& file, const std::string& date1, const std::string& date2) const
{
	this->service.writeToFile(file, date1, date2);
}

void UI::isIll() const
{
	if (this->service.isIll())
		cout << "Is ill" << endl;
	else
		cout << "Is not ill" << endl;
}
