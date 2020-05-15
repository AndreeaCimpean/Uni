#include "UI.h"
#include "MedicalAnalysis.h"
#include "BMI.h"
#include "BP.h"
#include <iostream>
#include <sstream>

using namespace std;

vector<string> tokenize(const string& line_read, char delimiter)
{
	vector <string> parameters_read;
	stringstream stream(line_read);
	string token;
	while (getline(stream, token, delimiter))
		parameters_read.push_back(token);
	return parameters_read;
}


void UI::run()
{
	string command="", line_read;
	while (command != "exit")
	{
		cin >> command;
		if (command == "list")
		{
			this->list_analyses();
		}
		else if (command == "add")
		{
			cin.ignore();
			getline(cin, line_read);
			vector<string> parameters = tokenize(line_read, ',');
			string date = parameters[1];
			string type = parameters[0];
			if (type == "BP")
			{
				int systolicValue = stoi(parameters[2]);
				int diastolicValue = stoi(parameters[3]);
				this->add_bp(date, systolicValue, diastolicValue);
			}
			else
			{
				double value = stoi(parameters[2]);
				this->add_bmi(date, value);
			}
		}
		else if (command == "ill")
		{
			cin.ignore();
			getline(cin, line_read);
			int month = stoi(line_read);
			this->is_ill(month);
		}
		else if (command == "save")
		{
			cin.ignore();
			getline(cin, line_read);
			vector<string> parameters = tokenize(line_read, ',');
			string file = parameters[0], date1 = parameters[1], date2 = parameters[2];
			this->service.write_to_file(file, date1, date2);
		}
	}
}

void UI::list_analyses() const
{
	auto analyses = this->service.get_all_analyses();
	for (auto analysis : analyses)
		cout << analysis->toString() << endl;
}

void UI::add_bp(const std::string& date, const int systolicValue, const int diastolicValue)
{
	shared_ptr<MedicalAnalysis> bp = make_shared<BP>(date, systolicValue, diastolicValue);
	this->service.add_analysis(bp);
}

void UI::add_bmi(const std::string& date, const double value)
{
	shared_ptr<MedicalAnalysis> bmi = make_shared<BMI>(date, value);
	this->service.add_analysis(bmi);
}

void UI::is_ill(const int month) const
{
	if (this->service.isIll(month))
		cout << "Is ill" << endl;
	else
		cout << "Not ill" << endl;
}
