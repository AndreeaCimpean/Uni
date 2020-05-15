#include "UI.h"
#include <sstream>
#include "HospitalDepartment.h"
#include"NeonatalUnit.h"
#include "Surgery.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>


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
	string command = "", line_read;
	while (command != "exit")
	{
		cin >> command;

		if (command == "add")
		{
			cin.ignore();
			getline(cin, line_read);
			line_read.erase(remove(line_read.begin(), line_read.end(), ' '), line_read.end());
			vector<string> parameters_read = tokenize(line_read, ',');
			string hospitalName, departmentType;
			hospitalName = parameters_read[0];
			departmentType = parameters_read[1];
			string numberOfDoctors = parameters_read[2];
			if (departmentType == "NeonatalUnit")
			{
				string numberOfMothers = parameters_read[3];
				string numberOfNewborns = parameters_read[4];
				string averageGarde = parameters_read[5];
				this->add_neonatal_unit(hospitalName, stoi(numberOfDoctors), stoi(numberOfMothers), stoi(numberOfNewborns), stod(averageGarde));

			}
			else
			{
				string numberOfPatients = parameters_read[3];
				this->add_surgery(hospitalName, stoi(numberOfDoctors), stoi(numberOfPatients));
			}
		}
		else if (command == "list")
		{
			getline(cin, line_read);
			if (line_read == " efficent")
			{
				this->list_efficent();
			}
			else
			{
				if (this->service.is_file())
					this->service.write_to_file();
				else
					this->list_departments();
			}
				
		}
		else if (command == "fileLocation")
		{
			getline(cin, line_read);
			this->service.set_file(line_read);
		}
	}
}

void UI::add_neonatal_unit(const std::string& hospitalName, const int numberOfDoctors, const int numberOfMothers, const int numberOfNewborns, const double averageGrade)
{
	shared_ptr<HospitalDepartment> department = make_shared<NeonatalUnit>(hospitalName, numberOfDoctors, numberOfMothers, numberOfNewborns, averageGrade);
	this->service.add_department(department);
}

void UI::add_surgery(const std::string& hospitalName, const int numberOfDoctors, const int numberOfPatients)
{
	shared_ptr<HospitalDepartment> department = make_shared<Surgery>(hospitalName, numberOfDoctors, numberOfPatients);
	this->service.add_department(department);
}

void UI::list_departments() const
{
	auto departments = this->service.get_all_departments();
	for (auto department : departments)
	{
		cout << department->toString() << endl;
	}
}

void UI::list_efficent()
{
	auto departments = this->service.get_all_efficent();
	for (auto department : departments)
	{
		cout << department->toString() << endl;
	}
}
