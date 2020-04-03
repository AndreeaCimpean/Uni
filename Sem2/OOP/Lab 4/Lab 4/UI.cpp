#include "UI.h"
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void UI::run()
{
	cout << "Choose the mode"<<'\n';
	string mode;
	while (true)
	{
		getline(cin, mode); 
		if (mode != "mode A" && mode != "mode B")
			continue;
		else
			break;
	}
	string command = "";
	cin >> command;
	while (command != "exit")
	{
		if (mode == "mode A")
		{
			if (command == "add")
			{
				string id, measurement, imageClarityLevel, quantity, photograph;
				this->read_evidence(id, measurement, imageClarityLevel, quantity, photograph);
				try
				{
					this->check_measurement(measurement);
					this->check_image_clarity_level(imageClarityLevel);
					this->check_quantity(quantity);
					this->add_evidence(id, measurement, stod(imageClarityLevel), stoi(quantity), photograph);
				}
				catch (const char* message)
				{
					cout << message << endl;
				}
			}
			else if (command == "update")
			{
				string id, measurement, imageClarityLevel, quantity, photograph;
				this->read_evidence(id, measurement, imageClarityLevel, quantity, photograph);
				try
				{
					this->check_measurement(measurement);
					this->check_image_clarity_level(imageClarityLevel);
					this->check_quantity(quantity);
					this->update_evidence(id, measurement, stod(imageClarityLevel), stoi(quantity), photograph);
				}
				catch (const char* message)
				{
					cout << message << endl;
				}
			}
			else if (command == "delete")
			{
				string id;
				cin.ignore();
				getline(cin, id);
				this->delete_evidence(id);
			}
			else if (command == "list")
			{
				this->list_evidences();
			}
		}
		if (mode == "mode B")
		{
			if (command == "list")
				this->list_evidences();
		}
		cin >> command;
	}
}

void UI::check_measurement(const std::string& measurement) const
{
	int count_x = count(measurement.begin(), measurement.end(), 'X');
	if (count_x != 2)
		throw "Invalid measurement!";
	if (!isdigit(measurement[0]))
		throw "Invalid measurement!";
	for (int i = 1; i < measurement.length(); ++i)
	{
		if (!isdigit(measurement[i]))
		{
			if (measurement[i] != 'X' || (measurement[i] == 'X' && !isdigit(measurement[i - 1])))
				throw "Invalid measurement!";
		}
		else if (measurement[i] == '0' && measurement[i - 1] == 'X')
			throw "Invalid measurement!";
	}
}

void UI::check_image_clarity_level(const std::string& imageClarityLevel) const
{
	if (!isdigit(imageClarityLevel[0]))
		throw "Invalid image clarity level!";
	int count_dots = count(imageClarityLevel.begin(), imageClarityLevel.end(), '.');
	if (count_dots != 0 && count_dots != 1)
		throw "Invalid image clarity level!";
	for (int i = 0; i < imageClarityLevel.length(); ++i)
		if (!isdigit(imageClarityLevel[i]) && imageClarityLevel[i] != '.')
			throw "Invalid image clarity level!";
}

void UI::check_quantity(const std::string& quantity) const
{
	for (int i = 0; i < quantity.length(); ++i)
		if (!isdigit(quantity[i]))
			throw "Invalid quantity!";
	if (quantity == "0")
		throw "Invalid image clarity level!";
}

void UI::add_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph)
{
	try
	{
		this->service.add_evidence(id, measurement, imageClarityLevel, quantity, photograph);
	}
	catch (const char* message)
	{
		cout << message << endl;
	}
}

void UI::read_evidence(std::string& id, std::string& measurement, std::string& imageClarityLevel, std::string& quantity, std::string& photograph) const
{
	string parameters_read;
	getline(cin, parameters_read);
	parameters_read.erase(remove(parameters_read.begin(), parameters_read.end(), ' '), parameters_read.end());
	int index = 0, previous_index;
	while (parameters_read[index] != ',')
		index++;
	id = parameters_read.substr(0, index);
	index += 1;
	previous_index = index;

	while (parameters_read[index] != ',')
		index++;
	measurement = parameters_read.substr(previous_index, index - previous_index);
	index += 1;
	previous_index = index;

	while (parameters_read[index] != ',')
		index++;
	imageClarityLevel = parameters_read.substr(previous_index, index - previous_index);
	index += 1;
	previous_index = index;

	while (parameters_read[index] != ',')
		index++;
	quantity = parameters_read.substr(previous_index, index - previous_index);

	photograph = parameters_read.substr(index + 1);
}

void UI::update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph)
{
	try
	{
		this->service.update_evidence(id, measurement, imageClarityLevel, quantity, photograph);
	}
	catch (const char* message)
	{
		cout << message << endl;
	}
}

void UI::delete_evidence(const std::string& id)
{	
	try
	{
		this->service.delete_evidence(id);
	}
	catch (const char* message)
	{
		cout << message << endl;
	}
}

void UI::list_evidences() const
{
	Evidence* evidences =  this->service.get_evidences();
	for (int i = 0; i < this->service.get_number_of_evidences(); ++i)
	{
		Evidence current_evidence = *(evidences + i);
		cout << "Id: "<< current_evidence.get_id() << " Measurement: "<<current_evidence.get_measurement()<<" Image clarity level: " << current_evidence.get_image_clarity_level() <<" Quantity: "<< current_evidence.get_quantity() <<" Photograph: "<< current_evidence.get_photograph()<<endl;
	}
}
